numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_numbers = list(map(lambda x: x ** 2, even_numbers))

print(even_numbers)
print(squared_numbers)

############################################################

string_list = ["Apple", "Banana", "Cherry", "apricot", "Avocado"]

filtered_and_lowercased_list = list(map(lambda x: x.lower(), filter(lambda x: x[0] == 'A' and x[0].isupper(), string_list)))

print(filtered_and_lowercased_list)

####################################################################

original_dict = {'a': 3, 'b': 7, 'c': 2, 'd': 8, 'e': 10}

filtered_dict = dict(filter(lambda item: item[1] > 5, original_dict.items()))

cubed_dict = {key: value ** 3 for key, value in filtered_dict.items()}

print(cubed_dict)