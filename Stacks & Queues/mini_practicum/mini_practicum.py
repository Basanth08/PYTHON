import math
class Circle:
    __slots__ = ['__center', '__radius']
    
    def __init__(self, center, radius):
        self.__center = center  
        self.__radius = radius
    
    def __repr__(self):
        center_str = str(self.__center)
        radius_str = str(self.__radius)
        return "Center: " + center_str + " Radius: " + radius_str

    def __lt__(self,another):
        return self.__radius < another.__radius
    
    def intersect(self,another):
        x1,y1 = self.__center
        x2,y2 = another.__center
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return dist <= self.__radius + another.__radius
    
def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True

if __name__ =="__main__":
    main()           
    
