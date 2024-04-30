import torch
import numpy as np
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import TokenTextSplitter
from transformers import logging
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

logging.set_verbosity_error()

# -------------------------------------------------------------------------------------------------
# Document Loader
# -------------------------------------------------------------------------------------------------

loader = WebBaseLoader([
    'https://simple.wikipedia.org/wiki/Leonardo_da_Vinci',
    'https://simple.wikipedia.org/wiki/Frida_Kahlo',
    'https://simple.wikipedia.org/wiki/Filippo_Brunelleschi',
    'https://simple.wikipedia.org/wiki/El_Greco'
])

text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=100)
docs = text_splitter.split_documents(loader.load())

# -------------------------------------------------------------------------------------------------
# Text Embedding
# -------------------------------------------------------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-l6-v2",
    model_kwargs={'device':'cpu'},
    encode_kwargs={'normalize_embeddings': False}
)

# -------------------------------------------------------------------------------------------------
# Vector Stores
# -------------------------------------------------------------------------------------------------

db = FAISS.from_documents(docs, embeddings)

# -------------------------------------------------------------------------------------------------
# LLM Model
# -------------------------------------------------------------------------------------------------

# Specify the model name you want to use
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

# -------------------------------------------------------------------------------------------------
# LLM Answer extraction
# https://github.com/mcelikkaya/medium_articles2/blob/main/bert_question_answer.ipynb
# -------------------------------------------------------------------------------------------------

def get_top_answers(possible_starts,possible_ends,input_ids):
    answers = []
    for start,end in zip(possible_starts,possible_ends):
        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[start:end+1]))
        answers.append( answer )
    return answers  

def answer_question(question,context,topN):
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]
    text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    model_out = model(**inputs)
    answer_start_scores = model_out["start_logits"]
    answer_end_scores = model_out["end_logits"]

    possible_starts = np.argsort(answer_start_scores.cpu().detach().numpy()).flatten()[::-1][:topN]
    possible_ends = np.argsort(answer_end_scores.cpu().detach().numpy()).flatten()[::-1][:topN]
    
    answer_start = torch.argmax(answer_start_scores)  
    answer_end = torch.argmax(answer_end_scores) + 1  # Get the most likely end of answer with the argmax of the score
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    answers = get_top_answers(possible_starts,possible_ends,input_ids )

    return { "answer":answer,"answer_start":answer_start,"answer_end":answer_end,"input_ids":input_ids,
            "answer_start_scores":answer_start_scores,"answer_end_scores":answer_end_scores,"inputs":inputs,"answers":answers,
            "possible_starts":possible_starts,"possible_ends":possible_ends}

# -------------------------------------------------------------------------------------------------
# Retrievers
# -------------------------------------------------------------------------------------------------
questions=['When was Leonardo da vinci born?',
"What is Frida Kahlo husband's name?",
"who is considered an expressionist and cubist influencer?"
]
for question in questions:
  retriever = db.as_retriever(search_kwargs={"k": 1})
  docs = retriever.get_relevant_documents(question)
  text = ''
  for doc in docs:
    text += doc.page_content

answer_map = answer_question(question, text, 5)
print(f"Question: {question}")
print("Answers:")
[print((index+1)," ) ",ans) for index,ans in  enumerate(answer_map["answers"]) if len(ans) > 0 ]