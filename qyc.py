import numpy as np
import matplotlib.pyplot as plt

# 阶跃函数
from numpy import exp


def step (t):
    u = 0
    if t < 1:
        u = 0
    else:
        u = 5
    return u
#系统函数

def system_pt1(t, x, u, flag):
    Tm = 10
    if flag == 0:
        x0 = 0
        sys = [1, 0, 1, 0, 0]
    elif flag == 1 :
        sys = -x/Tm + u/Tm
    elif flag == 3:
        sys = x
    else:
        sys = []
    return sys
Tm = 10
h = 0.1
t0 = 0
tf = 300
t = []
# t.append(1)
d = []
d.append(0)
u = []
# u.append(1)
y = []
# y.append(1)
ys = []
# ys.append(1)
x = []
x.append(0)



ti = t0
i = 0

while ti <= tf:
    # ys[i] = 5 * (1 - exp(-(ti - 1) / Tm))
    ys.append(5 * (1 - exp(-(ti - 1) / Tm)))
    # u[i] = step(ti)
    u.append(step(ti))
    u2 = step(ti + h / 2)
    u3 = step(ti + h)
    # y[i] = system_pt1(ti, x[i], u[i], 3)
    y.append(system_pt1(ti, x[i], u[i], 3))
    k1 = system_pt1(ti, x[i], u[i], 1)
    k2 = system_pt1(ti + h / 2, x[i] + h * k1 / 2, u2, 1)
    k3 = system_pt1(ti + h, x[i] - h * k1 + 2 * h * k2, u3, 1)
    # x[i+1] = x[i] + h * k2

    x.append(x[len(x)-1] + h * k2)
    # d[i+1] = h * (k1 - 2 * k2 + k3) / 6

    d.append(h * (k1 - 2 * k2 + k3) / 6)
    # t[i] = ti
    t.append(ti)
    ti = ti + h
    i = i + 1
c = [y[i]-ys[i] for i in range(0, len(y))]

#draw

fig = plt.figure(1)

# ax1 = plt.subplot(2, 2, 1)
# plt.plot(t, u)
# plt.xlabel("Zeit , s")
# plt.title("Eingang PT1-Glied")
#
# ax1 = plt.subplot(2, 2, 2)
# plt.plot(t, y)
# plt.xlabel("Zeit , s")
# plt.title("Ausgang PT1-Glied")
#
# ax1 = plt.subplot(2, 2, 3)
# plt.plot(t, c)
# plt.xlabel("Zeit , s")
# plt.title("GDF")

ax1 = plt.subplot(2, 2, 4)
plt.plot(t, d)
plt.xlabel("Zeit , s")
plt.title("LDF")

plt.show()






