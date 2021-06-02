# combinadics
Combinatorial system of degree k ranking and unranking is a standalone simple (not necessarily the most efficient) module to compute the combinadics of a natural number (a.k.a unranking) and the inverse operation (a.k.a ranking)

Code is a commented python implementation of [James McCaffrey' concepts](https://docs.microsoft.com/en-us/archive/msdn-magazine/2004/july/using-combinations-to-improve-your-software-test-case-generation) of
1. Generating combinations through generating combination successors.
2. Calculating an arbitrary mathematical combination from a given lexicographical index (unranking) and, not explicit in McCaffrey' article,
2. Given a combination, calculate its lexicographical index (ranking).
 
Note that in the original article the author claims that the combinations he
presents are in lexicographic order, which is not true. However, both his
discussion and code are correct.
