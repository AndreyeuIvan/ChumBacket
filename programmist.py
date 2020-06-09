'1 programmist, 2 programmista, 5 programmistov and so on, 0<=n<=100'
while True:
    a = int(input('Enter number o f people in the room:'))
    if (a - 11) % 100 == 0 or (a - 12) % 100 == 0 or (a - 13) % 100 == 0 or (a - 14) % 100 == 0:
        b = 'o'        
    elif (a - 1) % 10 == 0: # done
        b = '1'
    elif (a - 2) % 10 == 0 or (a - 3) % 10 == 0 or (a - 4) % 10 == 0:
        b = 'a'
    else:
        b = 'ov'
        
    print(f'{a} Programmist' + b)

#if str(a).endswith('1') is True:
    #b = ''
# 22\23\24\32\33\34 % X =
'we have following numbers: 11,12,13,14,111,112,113,114,211,212,213,214,311,312,313,314 we need to connect them with programm'
# a - 11 = 0, 100 
