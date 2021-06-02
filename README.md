# combinadics
Combinatorial system of degree k ranking and unranking is a standalone simple (not necessarily the most efficient) module to compute the combinadics of a natural number (a.k.a unranking) and the inverse operation (a.k.a ranking)

Code is a commented python implementation of [James McCaffrey' concepts](https://docs.microsoft.com/en-us/archive/msdn-magazine/2004/july/using-combinations-to-improve-your-software-test-case-generation) of
1. Generating combinations through generating combination successors.
2. Calculating an arbitrary mathematical combination from a given lexicographical index (unranking) and, not explicit in McCaffrey' article,
2. Given a combination, calculate its lexicographical index (ranking).
 
Note that in the original article the author claims that the combinations he
presents are in lexicographic order, which is not true. However, both his
discussion and code are correct.

## Installation

```python
pip install combinadics
```

## Use

```python
from combinadics import Choose, Combination

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
print("The rank of combination {} is {}".format(
    combination, combination.Rank()
    ))

combination = Combination(5, 3)
position = 3
print("In position {} we find combination {}".format(
    position, combination.Element(position)
    ))
```

outputs
```
Choose(5,3) results in 10 combinations
Combination(5, 3) is initially {0 1 2}
The lexicographic successor of combination {0 1 2} is {0 1 3}
Now we set the combination data to be {0 3 4}
The lexicographic successor of combination {0 3 4} is {1 2 3}
The rank of combination {2 3 4} is 9
In position 3 we find combination {0 2 3}
```
