import time

class Sort:
    def _sort(self, arr):
        pass

    def _time(self, arr):
        start_time = time.time()
        self._sort(arr)
        end_time = time.time()
        return end_time - start_time

class BubbleSort(Sort):
    def _sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]