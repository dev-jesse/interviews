# Big-O Notation
### Overview
Big-O notation is a mathematical way of determining how efficent your code can run (notice I didn't say fast, as it could be based upon **time complexity** or **space complexity**).
### Big-O, the Warrior of Worst Case
When talking about runtime and space complexity, there are only three greek letters that are talked about. These include Omega (Ω), Theta (Θ) and Omicron (Ο). Respectively, these denote the best, average and worst runtimes/space complexity. 
### Rules with Big-O Notation
- Drop constants - This means that if something is O(2n) (i.e. runs 2n times), then it can be simplified to be O(n)
- Drop non-dominants - Drop the smaller runtimes within the internal of the function (i.e. one for-loop is O(n<sup>2</sup>) and the other is O(n), then we have the function with Big-O of O(n<sup>2</sup>) since O(n) is not the dominant term here).
### O(n) [Proportional]
An algorithm of O(n) has **proportional** operations done for the number of inputs (n). Therefore, it will always be a straight line on the graph.

![O(n) chart](https://lukasmestan.com/assets/images/o-n.png)

### O(n<sup>2</sup>) [Loop Inside a Loop]
An algorithm of O(n<sup>2</sup> is far less efficient. It means for any input given, there is a exponentially greater amount of operations done for that input. Further, note that O(n<sup>3</sup>), O(n<sup>4</sup>), ... simplifies to O(n<sup>2</sup>).

![O(n) chart](https://www.101computing.net/wp/wp-content/uploads/Big-O-Notation-Polynomial-Algorithm.png)

### O(1) [Constant time]
The most optimal runtime. This means that everytime this algorithm will always be the same (and the most optimal) for every run you do.

### O(log n) [Divide and Conquer]
This is an extremely optimal runtime. O(log n) basically seeing if an algorithm continually divides itself by a multiple (i.e. binary search). 

### O(nlog n) [Sorting Algos]
This is an extra... usually only used when describing a sorting algorithm at best runtime (fastest a sorting algo can be is O(nlog n)).

![O(n) chart](https://i.stack.imgur.com/Aq09a.png)

### Different terms for inputs
This is usually a coding got-ya, a little trick. Consider the following piece of code:
```python
def print_items(a, b):
  for i in len(a):
    print(i)
  for j in len(b):
    print(j)
```
Normally, we would think that this is O(n), since we drop the constants. However, since `a` and `b` are different inputs, that leaves us with a runtime of O(a)+O(b) = _O(a+b)_. As an extension consider the following code to determine the runtime:
```python
def print_items(a, b):
  for i in len(a):
    for j in len(b):
      print(i, j)
```
Now using basic runtime analysis, at first sight we may think this is O(n<sup>2</sup>) since we multiply the inner loops, however this is really O(a)\*O(b)=O(a\*b).

### Big-O of Lists
- Insertion/Deletion at end of a list is O(1) since we do not have to move the indices.
- Insertion/Deletion at the start/middle of a list is O(n) since we must move n indices (to the left for deletion, right for insertion).
- Searching for an item by value in a list is O(n), since we go from the first to the end linearly
- Searching by index in the list is O(1), since it is direct lookup by index.
