# 1. Write a script that will run through a list of tuples and replace the last value for each tuple. The list of tuples can be hardcoded. The "replacement" value is entered by user. The number of elements in the tuples must be different.

list_of_tuples = [(1,2,9,"ok"), ('hey', 3), ('hello'), (True), ('Yo.', 'value')]

new_element = input("Type some funny word: ")

list_of_tuples[-1] = new_element

print(list_of_tuples)