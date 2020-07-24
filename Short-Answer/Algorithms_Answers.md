#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The outer while loop is n^3 but the operation nested is n^2 and increments a + n^2. The n^2 of the operation cancels out the n^3 and reduces it to n.


b) O(n log n)
The for loop as a linear complexity. The inner while loop as a logarithmic complexity as the input is halved each time it runs. Since it is nested in the O(n) this function would have the O(log n) complexity


c) O(log n)
The base case is O(1). The recursive call runs for each bunny in bunnies O(n) - 1. Because the input is being halved it has a logarithmic complexity of O(log n)

## Exercise II

n-story building
eggs
f floor (constant)
need to find f floor by throwing eggs at each floo

f = 0
def eggtality(building):
    while f less than length of building
        throw egg
        if broken
            return f + 1
        f += 1

Runtime is O(n). The worst case is I have to go through every floor in the building before it breaks.
