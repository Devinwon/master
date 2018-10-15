"""
W    T    L
1.1  2.5  1.7
1.2  3.1  1.6
4.1  1.2  1.1
"""
rate=0.65
ig1,first_T,ig3=input().strip().split()
ig1,second_T,ig3=input().strip().split()
third_W,*ig3=input().strip().split()

rel=2*(float(first_T)*float(second_T)*float(third_W)*rate-1)

print("T T W {:.2f}".format(rel))