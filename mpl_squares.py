import matplotlib.pyplot as plt
plt.style.available

squares = [1, 4, 9, 16, 25]


plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()