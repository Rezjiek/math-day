import numpy as np
import matplotlib.pyplot


def snake(x,y,path):
    out_list = [(y,x)]
    for i in path:
        i = int(i)

        if i%2 == 0:
            y += 1-i
            if (y,x) in out_list:
                y -= 1-i
                x += 1-i
            out_list.append((y,x))

        if i%2 == 1:
            x += 2-i
            if (y,x) in out_list:
                x -= 2-i
                y += 2-i
            out_list.append((y,x))

    return out_list


def show(pos_list,sizes):
    field = np.zeros((sizes))
    for pos in pos_list:
        field[pos] = 1
    return field


def dif_base(num,base):
    b = len(base)
    if num<b:
        return base[num]
    else:
        return dif_base(num//b,base) + base[num%b]


def all_comb(length,base="012"):
    out_list = []
    for i in range(length):
        out_list.append(dif_base(i,base))

    return out_list


for i in range(100):
    print(" ")
    print(" ")
    path = all_comb(i)
    plot = show(snake(100,100,path),(200,200))
    plt.imshow(plot)
    plt.show()
