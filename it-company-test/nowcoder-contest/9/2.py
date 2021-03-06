'''
题目描述
珂朵莉给你一个有根树，求有多少个子树满足其内部节点编号在值域上连续
一些数在值域上连续的意思即其在值域上构成一个连续的区间
输入描述:
第一行有一个整数n，表示树的节点数。
接下来n–1行，每行两个整数x,y,表示存在一条从x到y的有向边。
输入保证是一棵有根树。
输出描述:
输出一个数表示答案

5
2 3
2 1
2 4
4 5

输出

5
节点1子树中编号为1，值域连续
节点3子树中编号为3，值域连续
节点5子树中编号为5，值域连续
节点4子树中编号为4,5，值域连续
节点2子树中编号为1,2,3,4,5，值域连续
'''
