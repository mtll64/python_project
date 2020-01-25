import time


def execution_time(fn):

    def dec_fun(data):
        start_time = time.time()
        k = fn(data)
        print("Function Execution Time in seconds: ", time.time() - start_time)
        return k

    return dec_fun

# Bubble sort

unsorted_list = list(range(0, 10000))

@execution_time
def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for comp in range(1, n):
        k = 0
        i = 0
        while i < n - comp:
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                i += 1
                k = 1
            else:
                i += 1
        if k == 0:
            break
    return unsorted_list


print(bubble_sort(unsorted_list))

