import random
import statistics as s

number_list = []
def gaussian_distribution():
    for i in range(1000):
        number = random.gauss(100, 10)
        number_list.append(number)
    return number_list

list_numbers = gaussian_distribution()
print("Mean:", s.mean(list_numbers))
print("Standard Deviation:", s.stdev(list_numbers))