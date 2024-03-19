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
def LinearSearch(N, target):
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
def DivideSearch(N, target):
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

# Sorting Programme(with lower efficiency)
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

## Select Sort
Use Linear Search to find the largest(or smallest) value in the unsorted part in the list.  
Swap that to the first slot of the unsorted part of the list and continue that until all the item of the list is sorted.  

Example:
```python
def SelectSort(N):
    for i in range(len(N)):
        max = i
        for j in range(i+1, len(N)):
            if N[j] > N[max]:
                max = j
        N[i], N[max] = N[max], N[i]
```

## Insert Sort
Save the value of the first item of the unsorted part of the list.  
Compare it to item in the sorted part.  
Find its position and insert it there.  

Example:
```python
def InsertSort(N):
    for i in range(1, len(N)):
        key = N[i]
        j = i - 1
        while j >= 0 and key > N[j]:
            N[j+1] = N[j]
        N[j+1] = key
```

## Bubble Sort


Example:
```python
for i in range(len(N)-1):
    for j in range(len(N)-1-i):
        if N[j] < N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]
```

# Sorting Programme(with lower efficiency)

## Merge two or more List
Example:
```python
def ListMerge(M, N, K):
    i = 0
    j = 0
    for k in range(len(N)+len(M)):
        if i < len(N) and (j == len(M) or N[i] < M[j]):
            H[k] = N[i]
            i += 1
        else:
            H[k] = M[j]
            j += 1
```

##
