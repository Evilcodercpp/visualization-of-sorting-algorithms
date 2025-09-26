import json
import os

def save_steps(steps, filename="data/steps.txt"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w") as f:
        for step in steps:
            f.write(" ".join(map(str, step)) + "\n")

def bubble_sort(arr):
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

def selection_sort(arr):
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

# можно добавить insertion_sort, merge_sort, quick_sort, heap_sort

if __name__ == "__main__":
    data = [5, 3, 8, 1, 4]
    steps = bubble_sort(data.copy())
    save_steps(steps)
