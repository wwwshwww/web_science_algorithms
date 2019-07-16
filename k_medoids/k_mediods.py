import numpy as np

def main():
    dis = np.zeros([5,5], dtype=int)
    m = np.zeros([25, 25], dtype=int)

    e = int(len(m)**(1/2))
    for i in range(len(m)):
        if i-1 >= 0:
            m[i,i-1] = 1
        if i+1 <= len(m)-1:
            m[i,i+1] = 1
        if i-e >= 0:
            m[i,i-e] = 1
        if i+e <= len(m)-1:
            m[i,i+e] = 1
    print(m)
    conv = [(2,2), (4,0)]
    pre_dis = np.full_like(dis, len(m.shape)**2+1)
    print(get_dis(pre_dis, conv))

    mat = np.zeros_like(dis)

    mini = 0
    for i in range(len(dis)):
        for j in range(len(dis[0])):
            tdis = np.full_like(dis, len(m.shape)**2+1)
            tconv = [(i,j)]
            tdis = get_dis(tdis, tconv)
            res = tdis - pre_dis
            res[res>0] = 0
            mat[i,j] = np.sum(res)
            print(f"node {i*len(dis)+(j+1)}: \t{np.sum(res)}")

def get_dis(arr, pp):
    for p in pp:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                di = abs(p[0]-i)
                dj = abs(p[1]-j)
                arr[i,j] = min(arr[i,j],di+dj)
    return arr

if __name__ == "__main__":
    main()