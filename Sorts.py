'''
Submitted By:Sadia khanam
5th Batch
Department of Computer Science & Engineering
University Of Barisal
'''
X = list(map(int, input("Enter the unsorted array:").split()))
# X=[0 5 8 9 4 2 5 21 11]
def InsertionSort(X):
    for j in range(1, len(X)):
        key = X[j];
        i = j - 1
        while (i > -1 and X[i] > key):
            X[i + 1] = X[i]
            i -= 1
        X[i + 1] = key
    print("The Insertion Sorting is: ", *X)

InsertionSort(X)
def swap(x, y):
    tmp = x;
    x = y;
    y= tmp;

def MergeSort(X):
    if len(X) > 1:
        mid = len(X) // 2;
        left = X[:mid];
        right = X[mid:];
        MergeSort(left);
        MergeSort(right);
        i = j = k = 0;

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                X[k] = left[i];
                i += 1
            else:
                X[k] = right[j];
                j += 1
            k += 1
        # For all the remaining values
        while i < len(left):
            X[k] = left[i];
            i += 1;
            k += 1
        while j < len(right):
            X[k] = right[j];
            j += 1;
            k += 1


MergeSort(X)
print("The Merge Sorting is: ", *X)


def CountingSort(X):
    ma = max(X);
    ln = len(X)
    C = [0] * (ma + 1)
    for i in X:
        C[i] = C[i] + 1
    C[0] = C[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, ma + 1):
        C[i] = C[i] + C[i - 1]
    B = [0] * len(X)
    for a in reversed(X):
        B[C[a]] = a
        C[a] = C[a] - 1
    return B

def BubbleSort(X):
    for i in X:
        for j in range(i, len(X)):
            if (X[i] <= X[j]):
                swap(X[i], X[j])
    print("The Bubble Sorting is: ", *X)


BubbleSort(X)


def SelectionSort(X):
    C = []
    for i in range(len(X)):
        mn = min(X[i:])
        swap(X[i], X[X.index(mn)])
    print("The Selection Sorting is: ", *X)


SelectionSort(X)
print("The Counting Sorting is: ", *CountingSort(X))
