from sympy import *

with open('24/input.txt') as f:
    lines = f.read().splitlines()

class Snowflake():
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

    def getPosAtTime(self, t):
        return ( self.x+t*self.dx, self.y+t*self.dy)

    def crossingXY(self, other):
        divider = other.dy*self.dx - self.dy*other.dx
        if divider == 0:
            return False
        crossingTime1 = (other.dx*(self.y-other.y)+other.dy*(other.x-self.x))/divider
        crossingTime2 = (self.y-other.y+self.dy*crossingTime1)/other.dy
        if crossingTime1 > 0 and crossingTime2 > 0:
            # print(crossingTime1)
            # print(crossingTime2)
            selfPos = self.getPosAtTime(crossingTime1)
            otherPos = other.getPosAtTime(crossingTime2)
            # print(selfPos)
            # print(otherPos)
            xMin = 200000000000000
            xMax = 400000000000000
            if selfPos[0] >= xMin and selfPos[0] <= xMax and \
               selfPos[1]  >= xMin and selfPos[1] <= xMax and \
               otherPos[0] >= xMin and otherPos[0] <= xMax and \
               otherPos[1]  >= xMin and otherPos[1] <= xMax:
                return True


snowflakes = list()
for line in lines:
    posAndVel = line.split(' @ ')
    pos = posAndVel[0].split(',')
    vel = posAndVel[1].split(',')
    s = Snowflake(float(pos[0]), float(pos[1]), float(pos[2]), float(vel[0]), float(vel[1]), float(vel[2]))
    snowflakes.append(s)


x, y,z, dx, dy, dz, t1, t2, t3 = symbols('x,y,z, dx, dy, dz, t1, t2, t3')
s1 = snowflakes[0]
s2 = snowflakes[1]
s3 = snowflakes[2]
result = solve([Eq(x+dx*t1-s1.x-s1.dx*t1,0.0), \
Eq(y+dy*t1-s1.y-s1.dy*t1,0.0), \
Eq(z+dz*t1-s1.z-s1.dz*t1,0.0), \
Eq(x+dx*t2-s2.x-s2.dx*t2,0.0), \
Eq(y+dy*t2-s2.y-s2.dy*t2,0.0), \
Eq(z+dz*t2-s2.z-s2.dz*t2,0.0), \
Eq(x+dx*t3-s3.x-s3.dx*t3,0.0), \
Eq(y+dy*t3-s3.y-s3.dy*t3,0.0), \
Eq(z+dz*t3-s3.z-s3.dz*t3,0.0)], [x, y,z, dx, dy, dz, t1, t2, t3])
print(result[0])
print(result[0][0]+ result[0][1]+ result[0][2])