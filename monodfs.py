#!/usr/bin/python3
# Monopoles Solved
# Matthew Spohrer

import sys


def dfs(rs, todo, n, ri):
    # base case, at the last index of rooms
    if ri == n:
        # we're done here, we're at the last value and the
        # last room.
        if len(todo) == 1:
            return "unsat"
        return rs

    # get the monopole to add to a room
    t = todo.pop(0)

    print("t: ", t, "ri: ", ri, "rs[ri]: ", rs[ri])
    # search the current room to see if the current monopole
    # can be added to it
    nflag, i, t2 = 0, 0, t/2
    while nflag == 0 and i < len(rs[ri]) and rs[i] < t2:
        to_check = t - rs[i]
        if to_check in rs[ri] and to_check != rs[i]:
            nflag = 1
        i += 1

    if nflag == 0:
        rs[ri].append(t)
        rs = dfs(rs, todo, n, 0)

    todo.insert(0, t)
    return dfs(rs, todo, n, ri + 1)



def main():
    m = int(sys.argv[1])
    n = int(sys.argv[2])

    ms = range(1, m + 1)
    rs = [[] for i in range(n)]
    todo = [*ms]

    rs = dfs(rs, todo, n, 0)
    print("doneso: ")
    print(rs)


if __name__ == '__main__':
    main()
