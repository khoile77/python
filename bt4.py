#01: C
#02: A
#03: B
#04: D
#05: B

import random
import time


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_time(search_function, arr, x):
    start_time = time.time()
    result = search_function(arr, x)
    end_time = time.time()
    return result, end_time - start_time


def main():
  
    sizes = [20, 100, 1000, 10000, 100000]
    

    for size in sizes:
       
        arr = random.sample(range(size * 10), size)
        x = random.choice(arr) 

        print(f"\nKích thước mảng: {size}")

   
        result, duration = measure_time(linear_search, arr, x)
        print(f"Linear Search - Kết quả: {result}, Thời gian: {duration:.6f} giây")

        arr.sort()
        result, duration = measure_time(binary_search, arr, x)
        print(f"Binary Search - Kết quả: {result}, Thời gian: {duration:.6f} giây")

if __name__ == "__main__":
    main()