import os

def save_steps(steps, filename="data/steps.txt"):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w") as f:
        for step in steps:
            f.write(" ".join(map(str, step)) + "\n")


# ---------- Алгоритмы сортировки ----------

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


def insertion_sort(arr):
    steps = [arr.copy()]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            steps.append(arr.copy())
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps


def merge_sort(arr):
    steps = [arr.copy()]

    def merge_sort_recursive(a, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(a, l, m)
            merge_sort_recursive(a, m+1, r)
            merge(a, l, m, r)

    def merge(a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = a[l:l+n1]
        R = a[m+1:m+1+n2]
        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
            steps.append(arr.copy())
        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1
            steps.append(arr.copy())
        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1
            steps.append(arr.copy())

    merge_sort_recursive(arr, 0, len(arr)-1)
    return steps


def quick_sort(arr):
    steps = [arr.copy()]

    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                steps.append(arr.copy())
        a[i+1], a[high] = a[high], a[i+1]
        steps.append(arr.copy())
        return i+1

    def quick_sort_recursive(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quick_sort_recursive(a, low, pi-1)
            quick_sort_recursive(a, pi+1, high)

    quick_sort_recursive(arr, 0, len(arr)-1)
    return steps


def heap_sort(arr):
    steps = [arr.copy()]

    def heapify(a, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            steps.append(arr.copy())
            heapify(a, n, largest)

    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        steps.append(arr.copy())
        heapify(arr, i, 0)
    return steps


# ---------- Тестовый запуск ----------

if __name__ == "__main__":
    arr = [5, 3, 8, 1, 4, 7, 2, 6]
    print("Исходный массив:", arr)

    # выбираем сортировку (меняйте название функции)
    steps = bubble_sort(arr.copy())
    # steps = selection_sort(arr.copy())
    # steps = insertion_sort(arr.copy())
    # steps = merge_sort(arr.copy())
    # steps = quick_sort(arr.copy())
    # steps = heap_sort(arr.copy())

    save_steps(steps)
    print("Шаги сохранены в data/steps.txt")
