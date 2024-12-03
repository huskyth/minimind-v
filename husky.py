import matplotlib.pyplot as plt
import time

plt.ion()
ax, ay = [], []
for i in range(100):  # 遍历0-99的值
    ax.append(i)  # 添加 i 到 x 轴的数据中
    ay.append(i ** 3)  # 添加 i 的平方到 y 轴的数据中
    plt.clf()  # 清除之前画的图
    plt.plot(ax, ay)  # 画出当前 ax 列表和 ay 列表中的值的图形
    plt.pause(0.5)  # 暂停一秒
    plt.ioff()  # 关闭画图的窗口
