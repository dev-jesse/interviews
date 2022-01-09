# Big-O Notation
### Overview
Big-O notation is a mathematical way of determining how efficent your code can run (notice I didn't say fast, as it could be based upon **time complexity** or **space complexity**).
### Big-O, the Warrior of Worst Case
When talking about runtime and space complexity, there are only three greek letters that are talked about. These include Omega (Ω), Theta (Θ) and Omicron (Ο). Respectively, these denote the best, average and worst runtimes/space complexity. 
### Rules with Big-O Notation
- Drop constants - This means that if something is O(2n) (i.e. runs 2n times), then it can be simplified to be O(n)
- Drop non-dominants - Drop the smaller runtimes within the internal of the function (i.e. one for-loop is O(n<sup>2</sup>) and the other is O(n), then we have the function with Big-O of O(n<sup>2</sup>) since O(n) is not the dominant term here).
## O(n)
An algorithm of O(n) has **proportional** operations done for the number of inputs (n). Therefore, it will always be a straight line on the graph.

![O(n) chart](https://lukasmestan.com/assets/images/o-n.png)

## O(n<sup>2</sup>)
An algorithm of O(n<sup>2</sup> is far less efficient. It means for any input given, there is a exponentially greater amount of operations done for that input. Further, note that O(n<sup>3</sup>), O(n<sup>4</sup>), ... simplifies to O(n<sup>2</sup>).

![O(n) chart](https://www.101computing.net/wp/wp-content/uploads/Big-O-Notation-Polynomial-Algorithm.png)

## O(1)
The most optimal runtime. This means that everytime this algorithm will always be the same (and the most optimal) for every run you do.

![O(n) chart](https://miro.medium.com/max/1400/1*FkQzWqqIMlAHZ_xNrEPKeA.png)
