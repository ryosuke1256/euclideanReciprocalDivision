def euclideanReciprocalDivision(x,y):
    remainder = x % y
    if remainder == 0:
        return y 
    return euclideanReciprocalDivision(y, remainder)
x,y = map(int, input('正の整数を2つ入力してください: ').split())
print('最大公約数は: ' + str(euclideanReciprocalDivision(x,y)))
