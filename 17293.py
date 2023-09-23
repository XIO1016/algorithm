import sys

input = sys.stdin.readline

n = int(input())

for i in range(n + 1):
    if i == n:
        if n == 1:
            print("No more bottles of beer on the wall, no more bottles of beer.\n"
                  "Go to the store and buy some more, %d bottle of beer on the wall." % n)
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.\n"
                  "Go to the store and buy some more, %d bottles of beer on the wall." % n)
    else:
        if i == n - 1:
            print("%d bottle of beer on the wall, %d bottle of beer." % (n - i, n - i))
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            print("%d bottles of beer on the wall, %d bottles of beer." % (n - i, n - i))
            if i == n - 2:
                print("Take one down and pass it around, %d bottle of beer on the wall." % (n - i - 1))
            else:
                print("Take one down and pass it around, %d bottles of beer on the wall." % (n - i - 1))
        print()
