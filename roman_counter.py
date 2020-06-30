'''Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000'''

def solution(number:int):
    sentence = ''
    while number >= 1000:
        number -= 1000
        sentence += 'M'
        
    while number >= 500:
        number -= 500
        sentence += 'D'

    while number >= 100:
        number -= 100
        sentence += 'C'

    while number >= 50:
        number -= 50
        sentence += 'L'
        
    while number >= 10:
        number -= 10
        sentence += 'X'

    if number == 9:
        sentence += 'IX'
    else:
        while number >= 5:
            number -= 5
            sentence += 'V'

    while number >= 1:
        number -= 1
        sentence += 'I'
    

    return sentence, number

print(solution(1669))

