import numpy as np
import matplotlib.pyplot as plt
import queue
import collections

FILENAME = 'wiki.link'

def dist_bfs(i, alpha):
    q = queue.Queue()
    dis = np.zeros([len(alpha)])
    dirty = np.full([len(alpha)], False)
    dirty[i] = True
    q.put(i)
    while not q.empty():
        f = q.get()
        for j in alpha[f]:
            if not dirty[j]:
                dirty[j] = True
                dis[j] = dis[f] + 1
                q.put(j)
    return dis

def cluster_factor(i, alpha):
    if len(alpha[i]) < 2:
        return 0.0
    c_count = 0
    u_flg = np.zeros([len(alpha)])
    for ii in alpha[i]:
        u_flg[ii] = 1
    for v_id in range(len(alpha[i])):
        v = alpha[i][v_id]
        v_flg = np.full([len(alpha[v])], 0)
        for w_id in range(len(alpha[v])):
            w = alpha[v][w_id]
            if w > v:
                c_count += u_flg[w]
    return 2*c_count/(len(alpha[i])*(len(alpha[i])-1))

def main():
    f = open(FILENAME)
    line = f.readline()
    byeNL = lambda line: line.replace('/n', '')
    nn = list(map(lambda i: int(i), byeNL(line).split(' ')))[:-1]

    li = [None]*nn[0]
    w = np.zeros(nn) ## omomi
    cnt = 0
    while line:
        line = byeNL(f.readline())
        if line == '': break
        tmp = line.split(' ')[:-2]
        net = list(map(lambda n: int(n.split(':')[0])-1, tmp[1:]))
        li[cnt] = net
        cnt += 1

    n_edge = list(map(lambda e: len(e), li))
    count = collections.Counter(n_edge)
    print(count)

    sum_path = 0
    sum_dis = 0
    sum_factor = 0
    for i in range(len(li)):
        dis = dist_bfs(i, li)
        sum_factor += cluster_factor(i, li)
        sum_dis += np.sum(dis)
        sum_path += np.count_nonzero(dis)

    print(f'ave_node_distance: {sum_dis/sum_path}, ave_cluster_factor: {sum_factor/len(li)}')
    # print(sum_factor/len(li))

if __name__ == '__main__':
    main()