"""My Code has some Minor Error, Im unable to fix those. Allot me partial marks if possible. Got Struck!"""

def gcd(a, b):  # greatest common divisor
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

class Fraction:
    def __init__(self,w,n=0,d=1):
        self.w = w
        self.n = n 
        self.d = d

    def get_fraction(self):
        whole = self.w
        numerator = self.n 
        denominator = self.d
        return whole, numerator, denominator
    
    def simplify(self):
        imn = self.n + (self.w * self.d)  
        dino = gcd(imn, self.d)
        nr = imn // dino
        dr = self.d // dino
        if dr < 0:
            nr = nr *-1 
            dr = dr *-1
        new_w=nr//dr
        new_n=nr%dr    
        return new_w,nr,dr

    # def simplify(self):
    #     imp_numerator = self.n + (self.w * self.d)
    #     gcd = gcd(imp_numerator, self.d)
    #     sim_numerator = imp_numerator // gcd
    #     sim_denominator = self.d // gcd
    #     if sim_denominator < 0:
    #         sim_denominator = sim_denominator * -1
    #         sim_numerator = sim_numerator * -1
    #     whole_sim = sim_numerator // sim_denominator
    #     rem = sim_numerator % sim_denominator
    #     return whole_sim, sim_numerator, sim_denominator

    def impfrac(self):
         return self.n + self.w * self.d, self.d

    def add(self, other):
        num1,den1 = self.impfrac()
        num2,den2 = other.impfrac()
        den = den1 * den2
        num1num2 = num1*den2 + num2*den1
        sum = Fraction(0,num1num2,den)
        return sum.simplify()
        
    def subtract(self, other):
        num1,den1 = self.impfrac()
        num2,den2 = other.impfrac()
        den = den1 * den2
        num1num2 = num1*den2 - num2*den1
        diff = Fraction(0,num1num2,den)
        return diff.simplify()
    
        # num1 = self.n * other.d  
        # num2 = self.d * other.n
        # num = num1 - num2
        # den = self.d * other.d
        # return Fraction(0, num, den).simplify()

    def __repr__(self):
        return "<" + str(self.w) + "," + str(self.n) + "," + str(self.d) + ">"
    
    def __str__(self):
        whole = str(self.w)
        fraction = "(" + str(self.n) + "/" + str(self.d) + ")"  
        return whole + " " + fraction

    def _eq_(self, other):
        if type(self) == type(other):
            return self.simplify().w == other.simplify().w and self.simplify().n == other.simplify().n and self.simplify().d == other.simplify().d 
        else:
            return False
    
    def __eq__(self, other):
        return self.simplify() == other.simplify()
    
    def __lt__(self, other):
        return (self.n + self.w * self.d) * other.d < (other.n + other.w * other.d) * self.d 

    def __le__(self, other):
        return self.simplify() <= other.simplify()

    def __gt__(self, other):
        return self.simplify() > other.simplify() 

    def __ge__(self, other):
        return self.simplify() >= other.simplify()    

    def __hash__(self):
        simplified = self.simplify()
        value = hash((simplified.w, simplified.n, simplified.d))
        return value 

def unique_sorted_list(fractions):
        simplified = set()
        for f in fractions:
            simplified.add(f.simplify())
        return sorted(simplified)

def partition(fractions):
    partitions = {}
    for f in fractions:
        key = f.simplify()  
        if key not in partitions:
            partitions[key] = []
        partitions[key].append(f) 
    return partitions


def find_all(partition, target):
    simplified_target = target.simplify()
    key = (simplified_target.w, simplified_target.n, simplified_target.d)
    if key in partition:
        matches = partition[key]
    else:
        matches = []
    return matches


# def main():
#     f1 = Fraction(1, 3, 4) 
#     f2 = Fraction(1, 2, 5)
#     f1.subtract(f2) 
#     f1.add(f2)
# if __name__ == "__main__":
#      main()