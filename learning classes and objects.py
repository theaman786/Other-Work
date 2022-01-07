class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def to_string(self):
        return "({0},{1})".format(self.x,self.y)
    def halfway(self,target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx,my)
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
p = Point(3,4)
q = Point(5,12)
print(p.x,p.y)
print(q.x,q.y)
print(p.distance_from_origin())
print(p.to_string())
print(p)
print(q)