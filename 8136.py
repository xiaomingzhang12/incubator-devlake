def bubble_sort(arr):
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        # 最后i个元素已经是排好序的，无需再比较
        for j in range(0, n-i-1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 示例列表
numbers = [64, 34, 25, 12, 22, 11, 90]

print("未排序的列表:", numbers)

# 调用冒泡排序函数
bubble_sort(numbers)

print("排序后的列表:", numbers)
