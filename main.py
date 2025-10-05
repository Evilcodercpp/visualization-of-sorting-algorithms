import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

plt.style.use("dark_background")

# ---------- Алгоритмы сортировки ----------

def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a.copy()

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        yield a.copy()

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            yield a.copy()
        a[j + 1] = key
        yield a.copy()

def gnome_sort(arr):
    """Gnome Sort с генератором для визуализации"""
    a = arr.copy()
    index = 0
    n = len(a)
    while index < n:
        if index == 0 or a[index] >= a[index - 1]:
            index += 1
        else:
            a[index], a[index - 1] = a[index - 1], a[index]
            index -= 1
        yield a.copy()

def quick_sort(arr):
    a = arr.copy()
    def sort(start, end):
        if start >= end:
            return
        pivot = a[end]
        i = start
        for j in range(start, end):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
            yield a.copy()
        a[i], a[end] = a[end], a[i]
        yield a.copy()
        yield from sort(start, i - 1)
        yield from sort(i + 1, end)
    yield from sort(0, len(a) - 1)

def heap_sort(arr):
    a = arr.copy()
    def heapify(n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            yield a.copy()
            yield from heapify(n, largest)
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        yield a.copy()
        yield from heapify(i, 0)

# ---------- Визуализация ----------
def create_sorting_video(sort_func, name, output):
    arr = np.random.randint(1, 100, 40)
    generator = sort_func(arr)

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(range(len(arr)), arr, color=plt.cm.cool(np.linspace(0, 1, len(arr))))
    ax.set_title(name, fontsize=20, pad=20, color='white', fontweight='bold')
    ax.axis('off')
    fig.patch.set_facecolor('black')

    def update(a):
        for bar, val in zip(bars, a):
            bar.set_height(val)
            bar.set_color(plt.cm.plasma(val / max(arr)))
        return bars

    ani = animation.FuncAnimation(fig, update, frames=generator, interval=40, blit=False)
    ani.save(output, writer="ffmpeg", fps=30)
    plt.close(fig)

# ---------- Генерация видео ----------
sorting_algos = [
    (bubble_sort, "Bubble Sort"),
    (selection_sort, "Selection Sort"),
    (insertion_sort, "Insertion Sort"),
    (gnome_sort, "Gnome Sort"),
    (quick_sort, "Quick Sort"),
    (heap_sort, "Heap Sort")
]

video_files = []
for func, name in sorting_algos:
    filename = f"{name.replace(' ', '_').lower()}.mp4"
    print(f"Создаётся видео: {name}")
    create_sorting_video(func, name, filename)
    video_files.append(filename)

# ---------- Объединение ----------
clips = [VideoFileClip(v).fx(vfx.speedx, 1.8) for v in video_files]
final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("sorting_all.mp4", fps=30)
print("Финальное видео создано: sorting_all.mp4")
