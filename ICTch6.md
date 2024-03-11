# Aim of this file
To list all the python programme used in HKDSE ICT Elective C Chapter 6 Search and Sorting

# Search Programme
It is used to find a specific item in a list.

## Linear Search
Search the target item form the beginning of the list until the item is found or reach the end of the list.  
PROS: Can be applyed to unsorted list  
CONS: Not Effective(require (N+1)/2 step in general)  

Example:
```python
Def LinearSearch(target):
    for i in range(0,len(N)):
        if target == N[i]:
            return i
```

## Divide Search
Search the target item by keep divideing list into the possible half and the impossible half  
PROS: Effective(require logN/log2 step in general)
CONS: The list have to be sorted

Example:
```python
Def DivideSearch(target):
    start = 0
    end = len(N)-1
    while start <= end:
        mid = int((start + end)/2)
        if target == N[mid]:
            return mid
        elif target > mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1
```

# Sorting Programme
Before introduce diffent sorting method and it's python programme, we have to talk about how to swap item in two variable

## Swap
In python, we only have to `a,b = b,a` to swap item.
But HKDSE only accept version using a temporary variable like one below:
```python
temp = a
a = b
b = temp
```
So keep that in mind for your exam.
