def binary_search(list, target, bottom, top):
    if top < bottom:
        return None
    mid = (top + bottom) // 2
    if list[mid] == target:
        return mid
    if list[mid] > target:
        return binary_search(list, target, bottom, mid - 1)
    return binary_search(list, target, mid + 1, top)

def linary_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None



if __name__ == '__main__':
    import random
    import time
    import matplotlib.pyplot as plt

    time_linear = []
    time_binary = []
    size_vec = [round(10**(0.2*i)) for i in range(1, 35)]
    for size in size_vec:
        ran = 10 * size
        arr = [random.randint(0, ran) for i in range (size)]
        arr.sort()
        arr = list(dict.fromkeys(arr))
        target = random.randint(0, ran)

        start_lin = time.time()
        linary_search(arr, target)
        end_lin = time.time()
        time_linear.append(end_lin - start_lin)

        start_bin = time.time()
        binary_search(arr, target, 0, len(arr) - 1)
        end_bin = time.time()
        time_binary.append(end_bin - start_bin)

    fig1 = plt.figure(figsize = (10, 10))
    plt.scatter(size_vec, time_linear, label="Linear Search", color= "#ff0000")
    plt.scatter(size_vec, time_binary, label="Binary Search", color = "#00ff00")
    plt.xlabel("List size")
    plt.ylabel("Computation time")
    plt.legend(loc = "upper left")
    plt.show()