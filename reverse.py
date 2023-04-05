# def reverse(array):
#     return array[::-1]

# array=[1,2,3,4,5,6,7,8]
# array=reverse(array)
# print(array)



def reverse_array(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr) 

