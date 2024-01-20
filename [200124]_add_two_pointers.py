def one(A, X):
    """Given a sorted array A (in ascending order)
        Find any pair (A[i], A[j]) such that their sum equals a given X"""
    
    for i in range(len(A)-1):
        if A[i+1] > A[i]:
            i +=1
        else: 
            return "array A is not sorted in ascending order"
# FIRST, Nếu để không có else: thì sẽ trả ra luôn là aray is not sorted
# SECOND, Để là just len(A), không có -1, thì sẽ list index out of range
# THIRD, Khi thêm vòng while nó sẽ chạy không dừng 
# Fourth, Nếu j start from i+1, return có thể sẽ output ra i=j trong trường hợp A[i]*2=X
    result =[]
    for i in range(len(A)):
        for j in range(i+1, len(A)-1):
           
            if A[i] + A[j] == X:
                result.append((A[i], A[j]))
                i += 1
                j += 1

    return f"FOUND: {result}"
                

# Nếu nó đã là dãy tăng dần thì chắc chắn sẽ có nhiều nhất 1 cặp, không thể xuất hiện cặp số thứ 2 trong array A có tổng bằng X

# Test
A = [10, 20, 35, 50, 75, 80]
X = 70
print(one(A, X))


# i,  j chính là two pointers

            