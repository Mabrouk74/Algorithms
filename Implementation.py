def DNF(array):
    low = 0
    mid = 0
    high = len(array) - 1

    while mid <= high:
        if array[mid] == 0:
            # Swap elements at low and mid pointers
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 1:
            # Move mid pointer forward
            mid += 1
        elif array[mid] == 2:
            # Swap elements at mid and high pointers
            array[mid], array[high] = array[high], array[mid]
            high -= 1

# Example usage:
input_array = [2, 0, 1, 2, 1, 0, 2, 1, 0]
print("Unsorted Array:", input_array)
DNF(input_array)
print("Sorted Array:", input_array)
