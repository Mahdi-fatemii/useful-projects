
def bubble_sort(x):
    n = len(x)
    #traverse through all elements
    for i in range(n):
        # Last i elements are already in place
        for j in range (0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
                         
    return x

#*************************************************************

def selection_sort(x):
    n = len(x)
    
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i+1, n):
            if x[j] < x[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        x[i], x[min_idx] = x[min_idx], x[i]
    
    return x

#************************************************************************

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

#************************************************************************

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged_arr = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_arr.append(left[left_index])
            left_index += 1
        else:
            merged_arr.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged_arr.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged_arr.append(right[right_index])
        right_index += 1

    return merged_arr

#*******************************************************

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

#*********************************************************
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_Sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


#***************************************************

def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a count array to store the count of each unique element
    count = [0] * (max_element + 1)
    
    # Count the occurrences of each element in the input array
    for num in arr:
        count[num] += 1
    
    # Calculate the cumulative sum of the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create a sorted output array
    output = [0] * len(arr)
    
    # Place each element from the input array into its correct position in the output array
    for num in arr:
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

#*****************************************************

def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_Sort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10

#***************************************************

def bucket_sort(arr):
    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]
    
    # Insert elements into their respective buckets
    for num in arr:
        index = int(num * len(arr))
        buckets[index].append(num)
    
    # Sort individual buckets
    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])
    
    # Concatenate sorted buckets into the final sorted array
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr


#**********************************************************

def enterlist():
    lisst = []
    n = int(input("enter the lenghs of your list:"))
    for i in range(n):
        vall = int(input(f'enter value number-{i}-:'))
        lisst.append(vall)
    return lisst

#**********************************************************

while True:
    print(f'{"<"*50}\n1: bubble sort\n2: selection sort\n3: insertion sort\n4: merge sort\
          \n5: quick sort\n6: heap Sort\n7: counting sort\n8: radix Sort\n9: bucket sort\n10: exit\n{">"*50}')
    choice = input('which sort you want to use?:')
    if choice == '1':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = bubble_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        print(f" your list: {lstq}")
        continue
    elif choice == '2':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = selection_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '3':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = insertion_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '4':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = merge_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '5':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = quick_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '6':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = heap_Sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '7':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = radix_Sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '8':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = bubble_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '9':
        lstq =  enterlist()
        print(f" your list: {lstq}")
        sortedlst = bucket_sort(lstq)
        print(f" your sorted list: {sortedlst}")
        continue
    elif choice == '10':
        print('good bye deer :)')
        break
