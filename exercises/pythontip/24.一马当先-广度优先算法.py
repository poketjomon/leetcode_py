# 下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），
# 现在想象一下，给你一个n行m列网格棋盘， 棋盘的左下角有一匹马，
# 请你计算至少需要几步可以将它移动到棋盘的右上角，
# 若无法走到，则输出-1. 如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
# 示例：
# 输入：n = 1 m = 2
#
# 输出：1
n=5
m=6
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]
vis1 = [ ([0]*(m+1))  for i in range(n+1)]
# print(vis1)
def bfs(n,m):
    vis = [ ([0]*(m+1))  for i in range(n+1)]
    q = [(0,0,0)]
    vis[0][0] = 1
    setp = 0xFFFFFFF
    while q:
        temp = q.pop(0)
        # print("---------temp:",temp)
        if temp[0] == n and temp[1] == m:
            if temp[2] < setp:
                setp = temp[2]
        for x,y in zip(dx,dy):
            curx = temp[0] + x
            cury = temp[1] + y
            if curx>n or cury>m or curx<0 or cury<0 or vis[curx][cury]:
                continue
            vis[curx][cury] = 1
            curstep = temp[2] + 1
            q.append((curx,cury,curstep))
    return -1 if setp == 0xFFFFFFF else setp
print(bfs(n,m))