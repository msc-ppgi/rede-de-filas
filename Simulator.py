import queueing_tool as qt
import numpy as np

def rate(t):
    return 0.5
def arr_f(t):
    return qt.poisson_random_measure(t,rate,0.5)

def ser_f(t):
    return t+ np.random.exponential(1.0)

q_classes = {1: qt.QueueServer}

q_args = {
    1: {
        'num_servers':1,
        'arrival_f': arr_f,
        'service_f': ser_f
    }
}

adja_list = {0: [1]}
edge_list = {0:{1:1}}

q = qt.adjacency2graph(adjacency=adja+list, edge_type=edgw_list)

qn = qt.QueueNetwork( g=h, q_classes=q_classes,q_args=q_args)