# задача 1
import math


def unique_elements(input_list):
    return list(set(input_list))


print(unique_elements([1, 2, 2, 3, 4, 5, 5]))

# задача 2


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_numbers(minimum, maximum):
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes


print(prime_numbers(1, 100))

# задача 3


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))
p1.set_coordinates(1, 1)
print(p1.get_coordinates())

# задача 4


def sort_strings_by_length(strings):
    return sorted(strings, key=len), sorted(strings, key=len, reverse=True)


strings = ["apple", "banana", "kiwi", "orange", "grape"]
ascending, descending = sort_strings_by_length(strings)
print(ascending)
print(descending)
