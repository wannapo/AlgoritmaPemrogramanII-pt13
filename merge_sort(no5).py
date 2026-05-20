def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort_descending(left_half)
    right_sorted = merge_sort_descending(right_half)
    
    return merge_descending(left_sorted, right_sorted)

def merge_descending(left, right):
    result = []
    left_ptr, right_ptr = 0, 0
    
    while left_ptr < len(left) and right_ptr < len(right):
        if left[left_ptr] >= right[right_ptr]: 
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1
            
    while left_ptr < len(left):
        result.append(left[left_ptr])
        left_ptr += 1
        
    while right_ptr < len(right):
        result.append(right[right_ptr])
        right_ptr += 1
        
    return result

angka = [64, 25, 12, 22, 11]
print("Sebelum diurutkan:", angka)
print("Setelah diurutkan (Descending):", merge_sort_descending(angka))
