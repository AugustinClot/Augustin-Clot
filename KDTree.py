from math import dist


# Question 1

def linear_scan(P,query):
    pass

# Question 2

def partition(P, query, coord):
    pass

# Question 3
def MoMSelect(P,coord,k):
    pass
            
        
class KDTree:
    
    # Question 4
    def __init__ (self,P,coord = 0):
        pass
    
    def __repr__(self):
        st = ""
        if not self.rootPoint is None:
            st += f"{self.rootPoint}(C{self.coord})("
            if not self.left is None:
                st += f"L:({self.left.__repr__()})"
            if not self.right is None:
                st += f"R:({self.right.__repr__()})"
            st += ")"
        return st
            
    def __str__(self, level=0):
        st = ""
        if self.rootPoint is None:
            st = "Empty"
        else:
            if level > 0:
                st = "|\t"*(level-1)+"|-->"
            st += f"{self.rootPoint} Coord= {self.coord}"
            if not self.left is None:
                st += f"\n {self.left.__str__(level+1)}"
            if not self.right is None:
                st += f"\n {self.right.__str__(level+1)}"
        return st

    def print_as_list(self):
        ll = [self.rootPoint]
        if not self.left is None:
            ll += self.left.give_list()
        if not self.right is None:
            ll += self.right.give_list()
        return ll
    
    # Question 5

    def NN_exhaustive_search(self, query):
        pass

    # Question 6

    def NN_defeatist_search(self, query):
        pass

    # Question 7

    def NN_backtracking_search(self,query, cand = None):
        pass
