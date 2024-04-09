# you can write to stdout for debugging purposes, e.g.
# establish a dict of the connected nodes of each node
# have a list of bools, as a marker
# iterate over all the node, do dfs, and increase group_num if not visited
# number of operations = group_num - 1
print("This is a debug message")

def num_operations(edges, nodes) -> int:
    # empty edges
    if not edges:
        return -1 if nodes else 0

    if len(edges) < len(nodes) - 1:
        return -1

    # whether it is true or fasle
    mp = {}
    for nd1, nd2 in edges:
        if mp.get(nd1) == None:
            mp[nd1] = [nd2]
        else:
            mp[nd1].append(nd2)
        if mp.get(nd2) == None:
            mp[nd2] = [nd1]
        else:
            mp[nd2].append(nd1)

    # count the num_ops
    visited = [False] * len(mp)
    group_num = 0

    def dfs(nd):
        if visited[nd]:
            return

        visited[nd] = True

        for nb in mp[nd]:
            dfs(nb)

    for nd in mp:
        if group_num == 1 and all(visited):
            return 0
            
        if visited[nd]:
            continue

        group_num += 1
        dfs(nd) 

    return group_num - 1      
