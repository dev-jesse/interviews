# Linked Lists

### A Quick Note on Pointers:
In python, when we alias a immutable object, then when the original variable is the changed, the aliased variable stays unaffected. However, if it aliases a mutable object, then we **point** to the mutable object, so all changes will also affect the mutable object. Take the following for example:
```python
num1 = 11
num2 = num1  # Currently num2 == 11

num1 = 22 # This leaves us with num1 == 22 and num2 == 11
```
However, when we deal with a immutable object
```python
item1 = {'num1': 11}  # item1 points to the dict
item2 = item1  # item2 points at item1, hence it points at the dict

item1['num1'] = 22  # Now the dict changes, so both item1 and item2 are modified
```

### Differences Between Python Lists and Linked Lists
- Python list are contingous, meaning items are stored together in memory. Linked lists on the other hand, are not contingous, and have nodes connected with "links".
- Python lists are index based, since the memory address for each item is contigous. Linked lists on the other hand have no indices.

### Big-O of Linked Lists
|   |Linked Lists|Why|Respective Big-O for Lists|
|---|------------|-----|---|
|Append|O(1)|Add item after self.tail|O(1)|
|Pop|O(n)|Must reset self.tail, needs to iterate list to find previous node|O(1)|
|Prepend|O(1)|New self.head|O(n)|
|Pop first|O(1)|Self.head is just the old self.head.next|O(n)
|Insert|O(n)|Iterate to find node wanted|O(n)|
|Remove|O(n)|Iterate to find previous to node wanted|O(n)|
|Lookup by Value|O(n)|Iterate to find value of node|O(n)|
|Lookup by Index|O(n)|Must traverse linked list node by node|O(1)|
