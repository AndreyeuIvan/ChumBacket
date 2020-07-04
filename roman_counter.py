'''Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000'''

def solution(number:int):
    sentence = str()
    roman = {
        1 : 'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        40 : 'XL',
        50 : 'L',
        90 : 'LC',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'DM',
        1000 : 'M'
        }
    
    while lengh_of_number == 4:
        number -= 1000
        sentence += roman.get(1000)
    while len(str(number)) == 3:
        if number // 900 == 1:
            number -= 900
            sentence += roman.get(900)
        elif number >= 500:
            number -= 500
            sentence += roman.get(500)
    while len(str(number)) == 2:
        pass
    else:
        pass
    return sentence, number, lenght_of_number

print(solution(1000))

