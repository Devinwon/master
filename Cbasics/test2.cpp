
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
 int main(){
//分析：是其中一个数的倍数
//NOIP2017,不能表示的最大数是ab-a-b,惭愧
//sumofab%a==0||sumofab%b==0

//好大一串证明

long long a, b;
  while((cin >> a)) {
    cout << min(a,b) << "\n";
  }
 return 0;
}

