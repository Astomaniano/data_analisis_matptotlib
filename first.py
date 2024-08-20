import matplotlib.pyplot as plt

#ПРОСТОЙ ЛИНЕЙНЫЙ ГРАФИК
# x = [2, 6, 8, 14, 20]
# y = [6, 4 ,10, 12, 16]
#
# plt.plot(x, y)
# plt.title('Пример простого линейного графика')
#
# plt.xlabel('ось X')
# plt.ylabel('ось Y')
#
# plt.show()

#ГИСТОГРАММА
# data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]
#
# plt.hist(data, bins=3)
#
# plt.title('гистограмма количества часов сна')
# plt.xlabel('часы сна')
# plt.ylabel('количество людей')
#
# plt.show()

#ДИАГРАММА РАССЕИВАНИЯ
x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)
plt.title('Пример диаграммы рассеивания')

plt.xlabel('ось X')
plt.ylabel('ось Y')

plt.show()