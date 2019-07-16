import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    # サカタのタネ
    with open('stock_value.txt', 'r') as file:
        for i in range(2):
            file.readline()
        data = file.readline().split(' ')[:-2]
        data = np.array(list(map(int, data)))
    
    num = 20 ## 変化点数
    yy = get_y(data, 0, len(data))

    erea = [0, len(data)] ## 初期区切り

    for i in range(num):
        p = change(data, erea)
        print(p)
        for j in range(len(erea)):
            if erea[j] > p:
                erea.insert(j, p)
                break
    print(erea)

    res = np.zeros([len(data)])
    for i in range(1, len(erea)):
        s = erea[i-1]
        e = erea[i]
        ty = get_y(data, s, e)
        means = ty[-1]/(e-s)
        res[s:e] = means

    le = np.array(range(1,len(data)+1))
    plt.plot(le, data)
    plt.plot(le, res)
    plt.show()

## eps: like (start:0, .... end:len(data))
def change(data, eps):
    f_in = np.zeros([len(eps)], dtype=int)
    f = np.zeros_like(f_in, dtype=float)
    for e in range(1, len(eps)):
        k, kv = getp(data, eps[e-1], eps[e])
        f_in[e-1] = k
        f[e-1] = kv
    
    ma = np.argmax(f)
    return f_in[ma]

def get_y(data, s, e):
    tmp = data[s:e]
    y = np.zeros([len(tmp)+1], dtype=int)
    for i in range(len(tmp)):
        y[i+1] = y[i] + data[i+s]
    return y

def getp(data, s, e):
    tmp = data[s:e]
    y = get_y(data, s, e)

    f = np.zeros_like(y, dtype=float)
    e_f1 = ((y[-1]-y[1])**2)/(len(tmp)-1)

    for t in range(2, len(y)-1):
        e1 = ((y[t]-y[1])**2)/(t-1)
        e2 = ((y[-1]-y[t])**2)/(len(tmp)-t)
        f[t] = e1+e2-e_f1
    
    k = np.argmax(f)+s-1
    kv = np.max(f)

    return k, kv

if __name__ == "__main__":
    main()