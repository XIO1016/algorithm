for _ in range(int(input())):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 21):
        for j in range(1, i):
            if arr[j] > arr[i]:
                cnt += 1
                arr[i], arr[j] = arr[j], arr[i]
    print(arr[0], cnt)
