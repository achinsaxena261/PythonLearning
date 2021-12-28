class Sorting:

    def __init__(self, arr):
        self.arr = arr

    # keyword - PIVOT -> element for which we will find the correct place in the array/sub-array
    def quicksort(self, start, end):

        if start > end:
            return

        # get the pivot item index which is mostly the position of the maximum value in a sub-array
        pi = self.quicksort_partition(start, end)
        # keep finding the correct place of the maximum value (pivot) in sub-arrays
        self.quicksort(start, pi - 1)
        self.quicksort(pi + 1, end)

    # not sure if this is a correct way to do partition, but it works
    def quicksort_partition(self, i, j):

        if i > j:
            return j

        # find correct position for elements pointed by 'i' until last item of array is visited
        if self.arr[i] >= self.arr[j]:
            temp = self.arr[i]
            self.arr[i] = self.arr[j]
            self.arr[j] = temp

        return self.quicksort_partition(i + 1, j)

    def mergesort(self, start, end):
        # terminate recursion
        if start >= end:
            return

        # find middle index to break into sub arrays
        mid = int((start + end) / 2)
        self.mergesort(start, mid)
        self.mergesort(mid + 1, end)
        # start merging back once both recursive calls are made and waiting in stack from last call to execute the
        # remaining last line
        self.merge_back(start, end, mid)

    def merge_back(self, i, j, m):
        # create subsets using middle index
        L = self.arr[i: m + 1]
        R = self.arr[m + 1:j + 1]

        self.merge_sets(L, R, 0, 0, i)

    def merge_sets(self, set1, set2, x, y, z):

        # break the recursion
        if x >= len(set1) and y >= len(set2):
            return

        # case: copy remaining items of set 1 back to main array since set 2 is already copied
        if x <= len(set1) - 1 and y >= len(set2):
            self.arr[z] = set1[x]
            return self.merge_sets(set1, set2, x + 1, y, z + 1)

        # case: copy remaining items of set 2 back to main array since set 1 is already copied
        if y <= len(set2) - 1 and x >= len(set1):
            self.arr[z] = set2[y]
            return self.merge_sets(set1, set2, x, y + 1, z + 1)

        # pointer will iterate over set 1 and set 2 both, smaller value between current positions of pointers will
        # be copied to the main array
        if set1[x] <= set2[y]:
            self.arr[z] = set1[x]
            return self.merge_sets(set1, set2, x + 1, y, z + 1)

        if set1[x] >= set2[y]:
            self.arr[z] = set2[y]
            return self.merge_sets(set1, set2, x, y + 1, z + 1)
