import numpy as np
import queue
from multiprocessing import Pool
import multiprocessing as multi

class nw():
    def __init__(self, alpha):
        self.alpha = alpha

    def dist_bfs(self, i):
        q = queue.Queue()
        dis = np.zeros([len(self.alpha)])
        dirty = np.full([len(self.alpha)], False)
        dirty[i] = True
        q.put(i)
        d = 0
        while not q.empty():
            f = q.get()
            d += 1
            for j in self.alpha[f]:
                if not dirty[j]:
                    dirty[j] = True
                    dis[j] = dis[f] + 1
                    q.put(j)
        print(dis)
        return dis

def main():
    nodes = np.zeros([6,6], dtype=int)
    nodes[0] = [0,1,0,0,1,0]
    nodes[1] = [1,0,1,0,1,0]
    nodes[2] = [0,1,0,1,0,0]
    nodes[3] = [0,0,1,0,1,1]
    nodes[4] = [1,1,0,1,0,0]
    nodes[5] = [0,0,0,1,0,0]

    alpha = []
    for i in range(len(nodes)):
        tmp = []
        for j in range(len(nodes[0])):
            if nodes[i,j] == 1:
                tmp.append(j)
        alpha.append(tmp)
    print(alpha)
    
    nn = nw(alpha)
    p = Pool(multi.cpu_count())
    print(np.sum(p.map(nn.dist_bfs, range(len(nn.alpha)))))
    p.close()
    
    for i in dist_bfs(alpha):
        print(i)
    gen = dist_bfs(alpha)
    for i in range(len(alpha)):
        print(f"node {i}: {next(gen)} {cluster_factor(i, alpha)}")
    
# def dist_bfs(alpha):
#     cost = np.zeros([len(alpha), len(alpha)])
#     for i in range(len(alpha)):
#         q = queue.Queue()
#         dirty = np.full([len(alpha)], False)
#         dirty[i] = True
#         q.put(i)
#         while not q.empty():
#             f = q.get()
#             for j in alpha[f]:
#                 if not dirty[j]:
#                     dirty[j] = True
#                     if cost[i,j] == 0: cost[i,j] = cost[i,f] + 1
#                     q.put(j)
#         cost[i:,i] = cost[i,i:].T
#         yield cost[i]

def dist_bfs(alpha):
    for i in range(len(alpha)):
        q = queue.Queue()
        dis = np.zeros([len(alpha)])
        dirty = np.full([len(alpha)], False)
        dirty[i] = True
        q.put(i)
        d = 0
        while not q.empty():
            f = q.get()
            d += 1
            for j in alpha[f]:
                if not dirty[j]:
                    dirty[j] = True
                    dis[j] = dis[f] + 1
                    q.put(j)
        yield dis

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
                # print(i,v,w, u_flg[w])
                c_count += u_flg[w]
    return 2*c_count/(len(alpha[i])*(len(alpha[i])-1))

if __name__ == "__main__":
    main()