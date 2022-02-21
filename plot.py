import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.1, 6.5, 100)  # x座標
y = 1/x  # y座標

left = np.array([0, 1, 2, 3, 4, 5])
height = np.array([1, 1/2, 1/3, 1/4, 1/5, 1/6])

plt.plot(x, y, color='red')  # 点列(x,y)を黒線で繋いだプロット
plt.bar(left, height, width=1.0, align='edge',
        color='#fff1c1', edgecolor='black')

plt.yticks([0, 1, 2])
plt.xlim([0, 6.5])
plt.ylim([0, 2])
plt.savefig('harmonic_number.png', dpi=300)
plt.show()  # プロットを表示
