from math import atan, acos, degrees, atan2, sqrt
from operator import gt, abs
from operator import abs
class P_test():
    def __init__(self, x, y, a,b):
        self.x, self.y, self.a, self.b = x, y, a, b
    
    def Region(self):
        if self.x**2/self.a**2 + self.y**2/self.b**2 >1:
            return 1
        
    def Slope(self):
        x, y = self.x, self.y
        A, B, C = self.a**2-self.x**2, 2*self.x*self.y, self.b**2-self.y**2
        D = sqrt(B**2-4*A*C)
        m1, m2 = (-B+D)/(2*A), (-B-D)/(2*A)
        return m1, m2
        
class Datasource():
    def __init__(self, cordinate, radius, pq):
        self.xy, self.r, self.pq = cordinate, radius, pq

    def a_b_of_ellipse(self):
        x1, x2, y, r = self.xy[0], self.xy[1], self.xy[2], self.r
        H, K = x1+(x2-x1)/2, y
        mx, my = x1-H, K
        gx, gy = x2-H, y-K
        ae = (mx-gx)/2
        a = gx + (r-(x2-x1))/2
        b = sqrt(a**2-ae**2)
        return a, b

    def G_angle(self):
        return degrees(atan(self.pq[0]/self.pq[1]))
    
    
def Touchpoint(x,y,m1,m2,a,b):
    c1,c2 = y-m1*x, y-m2*x
    return -a**2*m1/c1, b**2/c1, -a**2*m2/c2, b**2/c2

xy_cord = list(map(int, input().split()))
radius = int(input())
pq = list(map(int, input().split()))
r1 = Datasource(xy_cord, radius, pq)
aa, bb, G = r1.a_b_of_ellipse()[0], r1.a_b_of_ellipse()[1], r1.G_angle()
#print(aa,bb)
#print(G)
count = 0
for x in range(0, 10000):
    for y in range(0, 10000):
        r2 = P_test(x,y,aa,bb)
        if r2.Region():
            slope1, slope2 = r2.Slope()[0], r2.Slope()[1]
            #if r2.T_angle()>=G:
            Z = Touchpoint(x,y,slope1,slope2, aa, bb)
            px1,py1,px2,py2 = Z[0], Z[1], Z[2], Z[3]
            M = [degrees(atan2((y-py1),(x-px1))), degrees(atan2((y-py2),(x-px2)))]
            if abs(M[1]-M[0])>=G:
            #    print(x,y, abs(M[1]-M[0]))
                if x*y==0:
                    count += 2
                else:
                    count +=4
            else: break
print(count)
