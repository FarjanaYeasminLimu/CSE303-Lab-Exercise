"""problm-01"""

numbers = [i for i in range(1,1001)]
find_all_the_numbers = [n for n in numbers if n % 8 == 0]
print(find_all_the_numbers)



"""Problem-02"""

numbers = [i for i in range(1,1001)]
numbers_having_6 = [n for n in numbers if "6" in str(n)]
print(numbers_having_6)

"""Problem-03"""

string = "Practice Problems to Drill List Comprehension in Your Head."
spaces = len([char for char in string if char == " "])
print(spaces)

""" Problem-04"""

string = "Practice Problems to Drill List Comprehension in Your Head."
removing_vowels = "".join([char for char in string if char not in ["a","e","i","o","u"]])
print(removing_vowels)

"""Problem-05"""

string = "Practice Problems to Drill List Comprehension in Your Head. "
words = string.split(" ")
less_than_5_characters = [word for word in words if len(word) < 5]
print(less_than_5_characters)

"""Problem-06"""

words = "Practice Problems to Drill List Comprehension in Your Head."
length_of_a_word = {word:len(word) for word in words}
print(length_of_a_word)



"""Problem-07"""

nums = [i for i in range(1,1001)]
output = [num for num in nums if True in [True for divisor in range(2,9) if num % divisor == 0]]
print(output)

"""Problem-08"""

nums = [i for i in range(1,1001)]
results = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}
print(results)