#find the runner-up score in a given list
if __name__ == '__main__':
    
    n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        tmp = largest
        largest = x
        secondlargest = tmp
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)

