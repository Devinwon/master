#include <bits/stdc++.h>
#include <iostream>
using namespace std;

// ================= 代码实现开始 =================

/* 请在这里定义你需要的全局变量 */

// allOne:全1的二进制数,用于二进制"与运算",allOne=2^(n-1)-1
// vis:vis[i][u]表示从u出发值为i的边
//ans :答案
int allOne;
vector <bool> vis[2];
string ans;

//计算2^x
// x指数
//返回值:2^x
int twoPow(int x){
	return 1<<x;
}

//求欧拉回路
// u:当前所在节点

void dfs(int u){
	for (int i=0;i<2;++i)
		if(!vis[i][u]){
			int v=((u<<1)|i)&allOne;//将u左移一位(二进制相当于乘2),然后将最低位置为i,将最高位去掉
			vis[i][u]=1;
			dfs(v);
			ans.push_back('0'+i);	//递归v,将数字加到ans中
		}
}
// 本函数求解大转盘上的数，你需要把大转盘上的数按顺时针顺序返回
// n：对应转盘大小，意义与题目描述一致，具体见题目描述。
// 返回值：将大转盘上的数按顺时针顺序放到一个string中并返回
string getAnswer(int n) {
    /* 请在这里设计你的算法 */
	allOne=twoPow(n-1)-1;
	ans="";
	for(int i=0;i<2;++i)
		vis[i].resize(twoPow(n-1),0);
	dfs(0);
	return ans;

}

// ================= 代码实现结束 =================

int main() {
    int n;
    scanf("%d", &n);
    cout<<getAnswer(n)<<endl;
    return 0;
}
