import sys
input = sys.stdin.readline

N = int(input())

orders = []

info = {'ADD' : 0, 'SUB' : 1, 'MOV' : 2,
        'AND' : 3, 'OR' : 4, 'NOT' : 5, 'MULT' : 6,
        'LSFTL' : 7, 'LSFTR' : 8, 'ASFTR' : 9,
        'RL' : 10, 'RR' : 11}

### bin() : 이진수로 바꿔주는 함수(문자열로 나옴)
### bin(6)하면 '0b110' 이런식으로 나오므로 bin(6)[2:] 이렇게 해야한다
### zfill() : 앞에 자릿수만큼 0으로 채워주는 함수(자릿수 정해주는 함수)
