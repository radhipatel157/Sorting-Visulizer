import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Data
print("Enter the array :")
l=list(map(int,input().split()))
y = np.array(l)
x = np.arange(len(y))

# Create a figure with five subplots
fig, ((ax_bubble, ax_selection, ax_insertion), (ax_merge, ax_quick, _)) = plt.subplots(2, 3, figsize=(15, 6))

# Bars for bubble sort
bars_bubble = ax_bubble.bar(x, y, color='b')

# Bars for selection sort
bars_selection = ax_selection.bar(x, y, color='g')

# Bars for insertion sort
bars_insertion = ax_insertion.bar(x, y, color='c')

# Bars for merge sort
bars_merge = ax_merge.bar(x, y, color='r')

# Bars for quick sort
bars_quick = ax_quick.bar(x, y, color='m')

# Function to update the bar heights
def update_bars(bars, y):
    for bar, height in zip(bars, y):
        bar.set_height(height)
    return bars

# Bubble sort with animation
def bubble_sort_animation(y):
    n = len(y)
    for i in range(n):
        for j in range(0, n - i - 1):
            if y[j] > y[j + 1]:
                y[j], y[j + 1] = y[j + 1], y[j]
            yield y.copy()

# Selection sort with animation
def selection_sort_animation(y):
    n = len(y)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if y[j] < y[min_idx]:
                min_idx = j
        y[i], y[min_idx] = y[min_idx], y[i]
        yield y.copy()

# Insertion sort with animation
def insertion_sort_animation(y):
    n = len(y)
    for i in range(1, n):
        key = y[i]
        j = i - 1
        while j >= 0 and key < y[j]:
            y[j + 1] = y[j]
            j -= 1
        y[j + 1] = key
        yield y.copy()

# Merge sort with animation
def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # Storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # If elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # If elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    yield from merge_sort(arr, low, mid)  # left half
    yield from merge_sort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves
    yield arr.copy()

def merge_sort_animation(arr):
    n = len(arr)
    return merge_sort(arr, 0, n - 1)

# Quick sort with animation
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        yield array.copy()
        yield from quick_sort(array, low, pi - 1)
        yield from quick_sort(array, pi + 1, high)
        yield array.copy()

def quick_sort_animation(arr):
    n = len(arr)
    return quick_sort(arr, 0, n - 1)

# Generators for the animation frames
sort_generator_bubble = bubble_sort_animation(y.copy())
sort_generator_selection = selection_sort_animation(y.copy())
sort_generator_insertion = insertion_sort_animation(y.copy())
sort_generator_merge = merge_sort_animation(y.copy())
sort_generator_quick = quick_sort_animation(y.copy())

# Combined generator to alternate between all sorts' updates
def combined_generator():
    while True:
        try:
            bubble_frame = next(sort_generator_bubble)
            yield 'bubble', bubble_frame
        except StopIteration:
            break

    while True:
        try:
            selection_frame = next(sort_generator_selection)
            yield 'selection', selection_frame
        except StopIteration:
            break

    while True:
        try:
            insertion_frame = next(sort_generator_insertion)
            yield 'insertion', insertion_frame
        except StopIteration:
            break

    while True:
        try:
            merge_frame = next(sort_generator_merge)
            yield 'merge', merge_frame
        except StopIteration:
            break

    while True:
        try:
            quick_frame = next(sort_generator_quick)
            yield 'quick', quick_frame
        except StopIteration:
            break

# Update function for the combined generator
def update(frame):
    sort_type, data = frame
    if sort_type == 'bubble':
        update_bars(bars_bubble, data)
    elif sort_type == 'selection':
        update_bars(bars_selection, data)
    elif sort_type == 'insertion':
        update_bars(bars_insertion, data)
    elif sort_type == 'merge':
        update_bars(bars_merge, data)
    elif sort_type == 'quick':
        update_bars(bars_quick, data)

# Create the animation
ani = FuncAnimation(fig, update, frames=combined_generator(), repeat=False, blit=False)

# Labels and title for bubble sort
ax_bubble.set_xlabel('Index')
ax_bubble.set_ylabel('Value')
ax_bubble.set_title('Bubble Sort')

# Labels and title for selection sort
ax_selection.set_xlabel('Index')
ax_selection.set_ylabel('Value')
ax_selection.set_title('Selection Sort')

# Labels and title for insertion sort
ax_insertion.set_xlabel('Index')
ax_insertion.set_ylabel('Value')
ax_insertion.set_title('Insertion Sort')

# Labels and title for merge sort
ax_merge.set_xlabel('Index')
ax_merge.set_ylabel('Value')
ax_merge.set_title('Merge Sort')

# Labels and title for quick sort
ax_quick.set_xlabel('Index')
ax_quick.set_ylabel('Value')
ax_quick.set_title('Quick Sort')

# Adjust layout to prevent overlap
fig.tight_layout()

# Display the plots
plt.show()


