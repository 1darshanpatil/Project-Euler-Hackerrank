def f(x):
    n1, n2, n3 = x//3, x//5, x//15
    return int(3*(n1)*(n1+1)/2)+int(5*(n2)*(n2+1)/2)-int(15*(n3)*(n3+1)/2)
for i in range(int(input())):
    print(f(int(input())-1))
