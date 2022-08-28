def euclideanReciprocalDivision(x,y):
    if x >= y:
        largerValue = x
        smallerValue = y
    else:
        largerValue = y
        smallerValue = x
    remainder = largerValue % smallerValue
    if remainder == 0:
        return smallerValue
    return euclideanReciprocalDivision(smallerValue, remainder)
x,y = map(int, input('正の整数を2つ入力してください: ').split())
print('最大公約数は: ' + str(euclideanReciprocalDivision(x,y)))
