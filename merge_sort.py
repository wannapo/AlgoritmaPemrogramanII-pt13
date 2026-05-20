def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_ptr, right_ptr = 0, 0
    
    while left_ptr < len(left) and right_ptr < len(right):
        
        if left[left_ptr].lower() <= right[right_ptr].lower(): 
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

print("=== Program Pengurut Nama Buah dengan Merge Sort ===")
input_buah = input("Masukkan nama buah (pisahkan dengan koma, contoh: Mangga, Apel, Jeruk, Pisang): ")

list_buah = [buah.strip() for buah in input_buah.split(",") if buah.strip() != ""]

if len(list_buah) == 0:
    print("Daftar buah kosong, Bro.")
else:
    print("\nJumlah buah yang diinput:", len(list_buah))
    print("Daftar buah awal:", list_buah)
    
    buah_terurut = merge_sort(list_buah)
    print("Daftar buah setelah diurutkan (A-Z):", buah_terurut)
