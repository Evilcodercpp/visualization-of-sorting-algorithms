Нужно сделать визуализацию нескольких алгоритмов сортировки (5-6, можно со звуком, можно без). Вот некоторые примеры (можете легко найти очень много аналогов):

При работе в команде из трех человек. Придумайте, какой вариант визуализации вы хотите делать. Прочитайте пункты про этапы работы, договоритесь, кто какую роль берет, согласуйте форматы файлов и действуйте.

Сортировки. Вам нужны сами сортировки. СОдин человек их собирает или дописывает, проверяет работоспособность и делает вывод в файл. Как вы поняли из визуализаций, нужно записывать состояние массива по итерациям – возможно, как-то помечая изменения.
Отрисовка. Второй человек пишет код Python, который по текстовому файлу из пункта 0) генерирует набор кадров – стопку картинок (png/ppm).
Сборка. 

**Визуализация алгоритмов сортировки с Python**

Этот проект демонстрирует работу популярных алгоритмов сортировки с помощью анимации. Для наглядности создаются видео для каждого алгоритма, а затем объединяются в одно финальное видео sorting_all.mp4.

**Алгоритмы сортировки и их работа**
1. Пузырьковая сортировка (Bubble Sort)

Сравнивает соседние элементы и меняет их местами, если они в неправильном порядке.

Проходит по массиву несколько раз, пока массив полностью не отсортирован.

На графике можно увидеть, как большие элементы «всплывают» к концу массива.

Пример генератора для визуализации:

def bubble_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            yield a.copy()


yield a.copy() — возвращает текущее состояние массива для анимации.

2. Сортировка выбором (Selection Sort)

Находит минимальный элемент в неотсортированной части массива и перемещает его в начало.

Повторяет процесс для оставшейся части массива.

def selection_sort(arr):
    a = arr.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        yield a.copy()

3. Сортировка вставками (Insertion Sort)

Элементы вставляются по одному в отсортированную часть массива.

Хорошо работает на почти отсортированных массивах.

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

4. Сортировка Гнома (Gnome Sort)

Элементы перемещаются вперёд и назад («шагают как гном»), пока весь массив не отсортирован.

Использует один индекс и меняет соседние элементы при необходимости.

def gnome_sort(arr):
    a = arr.copy()
    index = 0
    while index < len(a):
        if index == 0 or a[index] >= a[index - 1]:
            index += 1
        else:
            a[index], a[index - 1] = a[index - 1], a[index]
            index -= 1
        yield a.copy()

5. Быстрая сортировка (Quick Sort)

Выбирается опорный элемент (pivot), массив делится на элементы меньше и больше pivot.

Рекурсивно сортируются части массива.

Очень эффективна для больших массивов.

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

6. Сортировка кучей (Heap Sort)

Превращает массив в кучу (дерево, где каждый родитель больше или меньше потомков).

Последовательно извлекает максимальный элемент и перестраивает кучу.

Гарантированная сложность O(n log n).

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

**Работа визуализации**

Генерация случайного массива

arr = np.random.randint(1, 100, 40)


Массив из 40 случайных чисел от 1 до 100.

Анимация с Matplotlib

Используется matplotlib.animation.FuncAnimation.

Каждый вызов yield из генератора обновляет график.

Цвет столбцов меняется в зависимости от значения:

bars = ax.bar(range(len(arr)), arr, color=plt.cm.cool(np.linspace(0, 1, len(arr))))


**Создание видео**

ani.save(output, writer="ffmpeg", fps=30)


Для каждого алгоритма создаётся отдельное mp4-видео.

**Объединение видео**

Библиотека moviepy позволяет ускорять и объединять видео:

clips = [VideoFileClip(v).fx(vfx.speedx, 1.8) for v in video_files]
final_clip = concatenate_videoclips(clips, method="compose")
final_clip.write_videofile("sorting_all.mp4", fps=30)


Все видео ускоряются (speedx=1.8) для динамичного просмотра.

Получается одно финальное видео со всеми алгоритмами.

**Используемые библиотеки**
Библиотека	Назначение
matplotlib.pyplot	Построение графиков и визуализация массивов
matplotlib.animation	Создание анимации сортировки
numpy	Генерация случайных массивов и удобная работа с числами
moviepy.editor	Объединение видео и ускорение видео
moviepy.video.fx.all.vfx	Визуальные эффекты для видео (ускорение)

![Sorting Algorithms Visualization](https://raw.githubusercontent.com/Evilcodercpp/visualization-of-sorting-algorithms/main/preview.gif)

Для просмотра полного видео с визуализацией всех алгоритмов сортировки, нажмите на изображение выше или перейдите по следующей ссылке:

[Полное видео: sorting_all.mp4](https://github.com/Evilcodercpp/visualization-of-sorting-algorithms/blob/main/sorting_all.mp4)
