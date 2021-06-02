#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 13:33:53 2021

@author: neoglez
Combinatorial system of degree k ranking and unranking is a standalone simple
 (not necessarily the most efficient) module to compute the combinadics of a
 natural number (a.k.a unranking) and the inverse operation (a.k.a ranking).

    Code is a commented python implementation of James McCaffrey' concepts of

    Generating combinations through generating combination successors.
    Calculating an arbitrary mathematical combination from a given
        lexicographical index (unranking) and, not explicit in
        McCaffrey' article,
    Given a combination, calculate its lexicographical index (ranking).

Note that in the original article the author claims that the combinations he
    presents are in lexicographic order, which is not true. However, both his
    discussion and code are correct.
"""

def Choose(n, k):
    """
    Efficient implementation (does not use factorial) of a function that 
    calculates the binomial coefficient (a.k.a. nChoosek).

    Parameters
    ----------
    n : integer
        Set size (number of elements)
    k : integer
        Subset size (choose k elements from n where order does not matter)

    Raises
    ------
    Exception

    Returns
    -------
    integer
        Number of possible combination of choosing k elements from a set of
        n elements.

    """
    # This three cases are selfexplanatory.
    if (n < 0 or k < 0):
        raise Exception("Invalid negative parameter in Choose()")
    if (n < k):
        return 0
    if (n == k):
        return 1
    
    result = None
    # Auxiliary variable to compute the partial product numerator.
    delta = None
    # Auxiliary variable to compute the partial product denominator.
    iMax = None
    # Choosing k elements from n equals choosing n-k elements from n.
    # Therefore, we can decide the most efficient implementation depending
    # on k by iterating to the least number to form the partial products. 
    if (k < n-k):
        # e.g., Choose(100,3).
        delta = n-k;
        iMax = k
    else:
        # e.g., Choose(100,97)
        delta = k
        iMax = n-k
    
    # Result is at least k + 1 (equivalently (n-k) + 1) when the number
    # of combination is not zero or one. This is difficult to see. Consider
    # the least nChoosek: 2Choose1 for if n=1 and k=1 then nChoosek = 1 and
    # we already ruled this case out. Then n=2, nChoosek = 2, which is at least
    # k + 1 = 1 + 1 = 2. We then fix k and increment n, e.g., 3Choose1 and
    # so on. Since n is always strictly bigger than k, it can then be seen
    # that the identity holds.
    result = delta + 1
    # Iterate over k to form the product denominator. Since range stops at
    # iMax - 1, we have to increment iMax (iMax + 1). Additionally, we start
    # at index 2 because dividing by zero is not defined and dividing by one
    # has no effect.  
    for i in range(2, iMax + 1):
        # e.g., 7Choose3.
        # result is alredy 5.
        # result accumulates. delta + 1 goes 6, 7. The formula is often
        # presented as n-1, n-2, ..., n-k-1 but the order of these products
        # does not matter (of course). i goes 2, 3 as usually presented:
        # 1, 2, ..., k.
        result = int((result * (delta + i)) / i)
    
    return result

def LargestV(a, b, x):
    """
    Return largest value v where v < a and  Choose(v,b) <= x.
    For example, if a = 8, b = 4 and x = 7, then v = 5 because
    5 < 8 and Choose (5,4)=5 <=7.

    Parameters
    ----------
    a : Integer
        DESCRIPTION.
    b : Integer
        DESCRIPTION.
    x : Integer
        DESCRIPTION.

    Returns
    -------
    Integer.

    """
    v = a-1
    c = Choose(v,b)
    while (c > x):
        v = v-1
        c = Choose(v,b)
    return v

class Combination:
    """
    Combination class. Represents a combination in a combination set generated
    by choosing in turn k elements from a set of n elements, where order
    does not matter.
    """
    def __init__(self, n, k, a=None):
        """
        Initialize combination.

        Parameters
        ----------
        n : Integer
            Set size
        k : Integer
            Combination size
        a : Array/List/Indexable optional
            A combination to initialize the combination's data.
            Default is None.

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        """
        if (n < 0 or k < 0):
            # normally n >= k
            raise Exception("Negative parameter in constructor")
        self.n = n
        self.k = k
        
        if (a and k != len(a)):
            raise Exception("Array length does not equal k");
        
        self.data = []
        if a is not None:
            for i in range(k):
               self.data.append(a[i])
        else:
            for i in range(k):
                self.data.append(i)
        
        if (not self.IsValid()):
            raise Exception("Bad value from array")
            
            
    def IsValid(self):
        
        if (len(self.data) != self.k):
            return False

        for i in range(self.k):
            if (self.data[i] < 0 or self.data[i] > self.n - 1):
                # value out of range
                return False
            if (i + 1 < self.k):
                if (self.data[i] >= self.data[i+1]):
                    # duplicate or not lexicographic
                    return False
        return True
    
    
    def __str__(self):
        string = "{"
        for i in range(self.k):
            string += str(self.data[i]) + " "
        string = string[:-1] + "}"
        return string
    
    def Successor(self):
        """
        Lexicographic successor of this combination

        Returns
        -------
        result : array
            The lexicographic successor

        """
        # If we reach the end, the are no successor. Therefore, return None.
        # Here self.data can not be empty otherwise there is no combination
        # to find the successor for and the last combination is the only one
        # where the first atom equals n-k. This is no easy to see! Because of
        # the lexicographic order the last combination must have as first
        # atom n-k, since values greater than n-k have been already used to
        # form combination with values less than n-k. Although atoms greater
        # than n-k where already chosen, they do not appear (and can not appear
        # ) in the first position. But how many elements are with n-k as first
        # atom? Note again that, becasue of the lexicograpgic order, other
        # elements in that combination must be strictly greather than n-k.
        # Furthermore, the second atom is n-k + 1 and it has been already used
        # in every other combination with first atom less than n-k, the second
        # atom is n-k + 2 and also has been used in every other combination
        # with first atom less than n-k and second atom n-k + 2 and so forth.
        # Thus, this is the only combination with first atom n-k, second atom
        # n-k+2, ... and k atom n-k + n-k.
        if (len(self.data) == 0 or self.data[0] == self.n - self.k):
            return None
        
        # This combination is the successor.
        result = Combination(self.n, self.k)
        
        # Copy the current combination in the result (combination is always
        # initialyzed with {1 2 3})
        for i in range(self.k):
            result.data[i] = self.data[i]
        
        # Start at the right-most atom and move left until we locate the
        # left-most atom which should be incremented. For example, if we
        # trying to find the successor of {0 3 4} in 5Choose3, we start at
        # index 2 and move left (decreasing i) until we reach the atom that
        # must be incremented.
        # Initialize index i with the greatest index value.
        i = self.k - 1
        
        # Again this is not easy to see. We have to look for the first
        # atom (starting from the left -last atom from
        # the right) that can be incremented IN LEXICOGRAPHIC ORDER.
        # When i=k-1, n-k + i is the
        # greatest atom (can not be further incremented), therefore we have to
        # keep looking at the left (by decrementing i and checking if the
        # element in the i position can be incremented, that is, equals
        # n-k + i - 1).
        # When the index has reached 1, the loop executes one last time and we
        # know we have to increment the atom in position 0.
        # For example, in the case {0 3 4}, we start at position 2, that is,
        # atom 4. Now, self.n - self.k + i = 4. This atom can not be further
        # incremented. Moving left i=1 and the atom is now 3. But incrementing
        # 3 would mean repeting 4, which is not allowed. We cycle until we
        # reach the penultimate (i > 0) atom because the atom in position 0
        # can always be incremented.
        while  i > 0 and result.data[i] == self.n - self.k + i:
            i = i - 1
            
        # Increment at the corresponding position.
        result.data[i] = result.data[i] + 1
        
        # The rest of the atoms are formed by incrementing the current atom
        # and moving to the right. This is easy to see. We just have to take
        # the immediately greater atom (successor) than the current.
        j = i
        while j < self.k - 1:
            result.data[j+1] = result.data[j] + 1
            j = j + 1
        
        return result
    
    def Element(self, m):
        """
        Returns the mth lexicographic (starting from 0) element of
        combination C(n,k).

        Parameters
        ----------
        m : Integer
            Combination position

        Returns
        -------
        A combination.

        """
        ans = []

        a = self.n
        b = self.k
        # x is the "dual" of m, duals sum to Choose(n,k) - 1
        x = (Choose(self.n, self.k) - 1) - m
  
        for i in range(self.k):
            # largest value v, where v < a and vCb < x 
            ans.append(LargestV(a, b, x))
          
            x = x - Choose(ans[i], b)
            a = ans[i]
            b = b-1
            
        for i in range(self.k):
            ans[i] = (self.n-1) - ans[i]

        return Combination(self.n, self.k, ans)
    
    def Rank(self):
        """
        Returns the rank of this combination

        Returns
        -------
        Integer. Rank of this combination (position of this combination
                in the lexicographic ordered list).

        """
        ans = []
        x = 0
        m = 0
        for i in range(self.k):
            ans.append(self.data[i])
        
        # Subtract each digit in the combinadic from n-1. We need this to
        # find the position m.
        for i in range(self.k):
            ans[i] = (self.n-1) - ans[i]
        
  
        for i in range(self.k):
            x = x + Choose(ans[i], self.k - i)
            

        # x is the "dual" of m, duals sum to Choose(n,k) - 1
        m = (Choose(self.n, self.k) - 1) - x
        return m

        
        
        

if __name__ == "__main__":
    combinations = Choose(5,3)
    print("Choose(5,3) results in {} combinations".format(combinations))
    
    combination = Combination(5,3)
    
    print("Combination(5, 3) is initially {}".format(Combination(5,3)))
    
    print("The lexicographic successor of combination {} is {}".format(
        combination, combination.Successor()
        ))
    
    print("Now we set the combination data to be {0 3 4}")
    
    combination.data = [0, 3, 4]
    print("The lexicographic successor of combination {} is {}".format(
        combination, combination.Successor()
        ))
    
    
    combination = Combination(5, 3, [2, 3, 4])
    print("Ranking: The rank of combination {} is {}".format(
        combination, combination.Rank()
        ))
    
    combination = Combination(5, 3)
    position = 3
    print("Unranking: in position {} we find combination {}".format(
        position, combination.Element(position)
        ))
    