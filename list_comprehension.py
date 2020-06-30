'''list_comprehension_practise'''

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

#dict comprehension
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

#walrus operator
import random
def get_weather_data():
    return random.randrange(90, 110)

#hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
#print(hot_temps)

cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}

#matrix
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
]
flat = [num for row in matrix for num in row]
print(flat)

# generators
print(sum([i * i for i in range(1000)]))
print(sum(i * i for i in range(1000000000)))



