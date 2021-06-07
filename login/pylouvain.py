import mysql.connector
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import networkx as nx
from django.db import connection


class PyLouvain:
    '''
        Builds a graph from _path.
        _path: a path to a file containing "node_from node_to" edges (one per line)
    '''
    @classmethod
    def from_sql(cls):
        cursor = connection.cursor()
        cursor.execute("use login")

        # 获取节点经纬度坐标
        info = {}
        cursor.execute("select SECTOR_ID, LONGITUDE, LATITUDE from tbcell;")
        result = cursor.fetchall()
        for x in result:
            info[x[0]] = [x[1], x[2]]

        cursor.execute("select SCELL, NCELL, C2I_Mean from tbc2i;")
        result = cursor.fetchall()
        nodes = {}
        edges = []
        for x in result:
            if x[0] not in info.keys() or x[1] not in info.keys():
                continue
            nodes[x[0]] = 1
            nodes[x[1]] = 1
            w = float(x[2])
            edges.append(((x[0], x[1]), w))
        # rebuild graph with successive identifiers
        node_dict, nodes_, edges_ = in_order(nodes, edges)
        print("%d nodes, %d edges" % (len(nodes_), len(edges_)))

        return cls(nodes_, edges_, info, node_dict)

    '''
        Initializes the method.
        _nodes: a list of ints
        _edges: a list of ((int, int), weight) pairs
    '''

    def __init__(self, nodes, edges, info, node_dict):
        self.nodes = nodes
        self.edges = edges
        self.info = info
        self.node_dict = node_dict
        # precompute m (sum of the weights of all links in network)
        #            k_i (sum of the weights of the links incident to node i)
        self.m = 0
        self.k_i = [0 for n in nodes]
        self.edges_of_node = {}
        self.w = [0 for n in nodes]
        for e in edges:
            self.m += e[1]
            self.k_i[e[0][0]] += e[1]
            self.k_i[e[0][1]] += e[1]  # there's no self-loop initially
            # save edges by node
            if e[0][0] not in self.edges_of_node:
                self.edges_of_node[e[0][0]] = [e]
            else:
                self.edges_of_node[e[0][0]].append(e)
            if e[0][1] not in self.edges_of_node:
                self.edges_of_node[e[0][1]] = [e]
            elif e[0][0] != e[0][1]:
                self.edges_of_node[e[0][1]].append(e)
        # access community of a node in O(1) time
        self.communities = [n for n in nodes]
        self.actual_partition = []

    '''
        Applies the Louvain method.
    '''

    def apply_method(self):
        network = (self.nodes, self.edges)
        best_partition = [[node] for node in network[0]]
        best_q = -1
        i = 1
        while 1:
            #print("pass #%d" % i)
            i += 1
            partition = self.first_phase(network)
            q = self.compute_modularity(partition)
            partition = [c for c in partition if c]
            #print("%s (%.8f)" % (partition, q))
            # clustering initial nodes with partition
            if self.actual_partition:
                actual = []
                for p in partition:
                    part = []
                    for n in p:
                        part.extend(self.actual_partition[n])
                    actual.append(part)
                self.actual_partition = actual
            else:
                self.actual_partition = partition
            if q == best_q:
                break
            network = self.second_phase(network, partition)
            best_partition = partition
            best_q = q
        return (self.actual_partition, best_q)

    def drawNetworkGraph(self, partition, q):
        node_dict = self.node_dict  # key是253916-2的形式，value是编号的形式
        reverse_node_dict = dict(
            zip(node_dict.values(),
                node_dict.keys()))  # key是编号的形式，value是253916-2的形式
        print(partition)
        print("模块度：", q)

        # 给各个社区节点分配颜色
        community_num = len(partition)
        print('community_num:', community_num)
        color_board = [
            'red', 'green', 'blue', 'pink', 'orange', 'purple', 'scarlet'
        ]
        color = {}
        for index in range(community_num):
            print("社区" + str(index + 1) + ":" + str(len(partition[index])))
            for node_id in partition[index]:
                color[node_id] = color_board[
                    index]  # color为一个字典，key为编号形式的节点，value为所属社区的颜色
        new_color_dict = sorted(color.items(),
                                key=lambda d: d[0],
                                reverse=False)  # 将color字典按照key的大小排序，并返回一个list
        node_list = [reverse_node_dict[item[0]]
                     for item in new_color_dict]  #存储编号从小到大顺序对应的253916-2的形式的节点
        color_list = [item[1] for item in new_color_dict]  #存储node_list中对应的节点颜色

        #构建networkx无向图
        G = nx.Graph()
        edge_list = []  #存储边列表
        edge_width = []  #存储边列表对应的边粗细
        edge_color = []  #存储边列表对应的边颜色
        for x in self.edges:
            G.add_edge(x[0][0], x[0][1], weight=x[1])
            edge_list.append([x[0][0], x[0][1]])
            if color[x[0][0]] == color[x[0][1]]:  #如果边的两端颜色相同
                edge_color.append(color[x[0][0]])  #则使用点的颜色作为边的颜色
            else:
                edge_color.append('c')  #否则使用其他颜色
            if float(x[1]) > 20.0:  #阈值
                edge_width.append(x[1] / 100.0)
            else:
                edge_width.append(0.0)

        # 可视化
        plt.figure(figsize=(20, 15), dpi=250)
        _node = [int(item.split("-")[-1]) % 4 for item in node_list]  #提取后缀模4取余
        node_0_index_list,node_1_index_list,node_2_index_list,node_3_index_list = [], [], [], []
        for index, item in enumerate(
                _node
        ):  #划分不同后缀余数的群，以便给每个群分配一个节点的形状 node_shape 防止都用圆形，导致同一经纬度的节点重叠在一起
            if item == 0:
                node_0_index_list.append(index)
            if item == 1:
                node_1_index_list.append(index)
            if item == 2:
                node_2_index_list.append(index)
            if item == 3:
                node_3_index_list.append(index)
        nx.draw_networkx_nodes(
            G,
            self.info,
            nodelist=[node_list[i] for i in node_0_index_list],
            node_shape=7,
            node_color=[color_list[i] for i in node_0_index_list],
            node_size=50)
        nx.draw_networkx_nodes(
            G,
            self.info,
            nodelist=[node_list[i] for i in node_1_index_list],
            node_shape=4,
            node_color=[color_list[i] for i in node_1_index_list],
            node_size=50)
        nx.draw_networkx_nodes(
            G,
            self.info,
            nodelist=[node_list[i] for i in node_2_index_list],
            node_shape=5,
            node_color=[color_list[i] for i in node_2_index_list],
            node_size=50)
        nx.draw_networkx_nodes(
            G,
            self.info,
            nodelist=[node_list[i] for i in node_3_index_list],
            node_shape=6,
            node_color=[color_list[i] for i in node_3_index_list],
            node_size=50)
        pos = {}
        for x in self.info.keys():
            if x not in node_dict.keys():
                continue
            pos[node_dict[x]] = self.info[x]
        nx.draw_networkx_edges(G,
                               pos,
                               edgelist=edge_list,
                               width=edge_width,
                               alpha=1,
                               edge_color=edge_color)
        # filename = hashlib.new(
        #     'md5', bytes(str(datetime.datetime.now()),
        #                  encoding="utf8")).hexdigest() + '.png'
        filename = "login/static/login/images/louvain.png"
        plt.savefig(filename, bbox_inches='tight', pad_inches=0.0)
        plt.close()
        # with open(filename, 'rb') as f:
        #     res = f.read()
        #     f.close()
        # os.remove(filename)
        # return res

    '''
        Computes the modularity of the current network.
        _partition: a list of lists of nodes
    '''

    def compute_modularity(self, partition):
        q = 0
        m2 = self.m * 2
        for i in range(len(partition)):
            q += self.s_in[i] / m2 - (self.s_tot[i] / m2)**2
        return q

    '''
        Computes the modularity gain of having node in community _c.
        _node: an int
        _c: an int
        _k_i_in: the sum of the weights of the links from _node to nodes in _c
    '''

    def compute_modularity_gain(self, node, c, k_i_in):
        return 2 * k_i_in - self.s_tot[c] * self.k_i[node] / self.m

    '''
        Performs the first phase of the method.
        _network: a (nodes, edges) pair
    '''

    def first_phase(self, network):
        # make initial partition
        best_partition = self.make_initial_partition(network)
        while 1:
            improvement = 0
            for node in network[0]:
                node_community = self.communities[node]
                # default best community is its own
                best_community = node_community
                best_gain = 0
                # remove _node from its community
                best_partition[node_community].remove(node)
                best_shared_links = 0
                for e in self.edges_of_node[node]:
                    if e[0][0] == e[0][1]:
                        continue
                    if e[0][0] == node and self.communities[
                            e[0][1]] == node_community or e[0][
                                1] == node and self.communities[
                                    e[0][0]] == node_community:
                        best_shared_links += e[1]
                self.s_in[node_community] -= 2 * (best_shared_links +
                                                  self.w[node])
                self.s_tot[node_community] -= self.k_i[node]
                self.communities[node] = -1
                communities = {
                }  # only consider neighbors of different communities
                for neighbor in self.get_neighbors(node):
                    community = self.communities[neighbor]
                    if community in communities:
                        continue
                    communities[community] = 1
                    shared_links = 0
                    for e in self.edges_of_node[node]:
                        if e[0][0] == e[0][1]:
                            continue
                        if e[0][0] == node and self.communities[
                                e[0][1]] == community or e[0][
                                    1] == node and self.communities[
                                        e[0][0]] == community:
                            shared_links += e[1]
                    # compute modularity gain obtained by moving _node to the community of _neighbor
                    gain = self.compute_modularity_gain(
                        node, community, shared_links)
                    if gain > best_gain:
                        best_community = community
                        best_gain = gain
                        best_shared_links = shared_links
                # insert _node into the community maximizing the modularity gain
                best_partition[best_community].append(node)
                self.communities[node] = best_community
                self.s_in[best_community] += 2 * (best_shared_links +
                                                  self.w[node])
                self.s_tot[best_community] += self.k_i[node]
                if node_community != best_community:
                    improvement = 1
            if not improvement:
                break
        return best_partition

    '''
        Yields the nodes adjacent to _node.
        _node: an int
    '''

    def get_neighbors(self, node):
        for e in self.edges_of_node[node]:
            if e[0][0] == e[0][1]:  # a node is not neighbor with itself
                continue
            if e[0][0] == node:
                yield e[0][1]
            if e[0][1] == node:
                yield e[0][0]

    '''
        Builds the initial partition from _network.
        _network: a (nodes, edges) pair
    '''

    def make_initial_partition(self, network):
        partition = [[node] for node in network[0]]
        self.s_in = [0 for node in network[0]]
        self.s_tot = [self.k_i[node] for node in network[0]]
        for e in network[1]:
            if e[0][0] == e[0][1]:  # only self-loops
                self.s_in[e[0][0]] += e[1]
                self.s_in[e[0][1]] += e[1]
        return partition

    '''
        Performs the second phase of the method.
        _network: a (nodes, edges) pair
        _partition: a list of lists of nodes
    '''

    def second_phase(self, network, partition):
        nodes_ = [i for i in range(len(partition))]
        # relabelling communities
        communities_ = []
        d = {}
        i = 0
        for community in self.communities:
            if community in d:
                communities_.append(d[community])
            else:
                d[community] = i
                communities_.append(i)
                i += 1
        self.communities = communities_
        # building relabelled edges
        edges_ = {}
        for e in network[1]:
            ci = self.communities[e[0][0]]
            cj = self.communities[e[0][1]]
            try:
                edges_[(ci, cj)] += e[1]
            except KeyError:
                edges_[(ci, cj)] = e[1]
        edges_ = [(k, v) for k, v in edges_.items()]
        # recomputing k_i vector and storing edges by node
        self.k_i = [0 for n in nodes_]
        self.edges_of_node = {}
        self.w = [0 for n in nodes_]
        for e in edges_:
            self.k_i[e[0][0]] += e[1]
            self.k_i[e[0][1]] += e[1]
            if e[0][0] == e[0][1]:
                self.w[e[0][0]] += e[1]
            if e[0][0] not in self.edges_of_node:
                self.edges_of_node[e[0][0]] = [e]
            else:
                self.edges_of_node[e[0][0]].append(e)
            if e[0][1] not in self.edges_of_node:
                self.edges_of_node[e[0][1]] = [e]
            elif e[0][0] != e[0][1]:
                self.edges_of_node[e[0][1]].append(e)
        # resetting communities
        self.communities = [n for n in nodes_]
        return (nodes_, edges_)


'''
    Rebuilds a graph with successive nodes' ids.
    _nodes: a dict of int
    _edges: a list of ((int, int), weight) pairs
'''


def in_order(nodes, edges):
    # rebuild graph with successive identifiers
    nodes = list(nodes.keys())
    nodes.sort()
    i = 0
    nodes_ = []
    d = {}
    for n in nodes:
        nodes_.append(i)
        d[n] = i
        i += 1
    edges_ = []
    for e in edges:
        edges_.append(((d[e[0][0]], d[e[0][1]]), e[1]))
    return (d, nodes_, edges_)
