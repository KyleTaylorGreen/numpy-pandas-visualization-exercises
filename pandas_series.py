import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#/******************************* EXCERCISE PT 1 *************************/

fruit_series = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# 1 Determine the number of elements in fruits.

print(fruit_series.size)

# 2 Output only the index from fruits.

print(fruit_series.index)

# 3 Output only the values from fruits.

print(fruit_series.values)

# 4 Confirm the data type of the values in fruits.

fruit_series.dtype

# 5 Output only the first five values from fruits.
#   Output the last three values. Output two random values from fruits.

print(f"First 5:\n {fruit_series.head(n=5)}")
print(f"Last three:\n {fruit_series.tail(n=3)}")
print(f"Two random values: \n{fruit_series.sample(n = 2)}")

# 6 Run the .describe() on fruits to see what information it returns 
#   when called on a Series with string values.

print(fruit_series.describe())

# 7 Run the code necessary to produce only the unique string values 
#   from fruits.

print(set(fruit_series))

# 8 Determine how many times each unique string value occurs in fruits

print(fruit_series.value_counts())

# 9 Determine the string value that occurs most frequently in fruits.

print(fruit_series.mode())

# 10 Determine the string value that occurs least frequently in fruits.
print(fruit_series.value_counts().nsmallest(n=1, keep='all'))


#/******************************* EXCERCISE PT 2 *************************/

# 1 Capitalize all the string values in fruits.

fruit_series = fruit_series.str.capitalize()
print(fruit_series)

# 2 Count the letter "a" in all the string values 
#   (use string vectorization).

print(f"# of 'a's in all of fruits: {fruit_series.str.count('a')}")

# 3 Output the number of vowels in each and every string value.

def count_vowels(pd_element):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in pd_element:
        if letter in vowels:
            count += 1
    return count

print(f"# of vowels in each word:\n {fruit_series.apply(count_vowels)}")

# 4 Write the code to get the longest string value from fruits.

print(f"Largest String: {fruit_series[fruit_series.apply(len).nlargest(n=1, keep='all').index]}")


# 5 Write the code to get the string values with 5 or more 
#   letters in the name.

print(fruit_series[fruit_series.apply(len) >= 5])

# 6 Use the .apply method with a lambda function to find the fruit(s) 
#   containing the letter "o" two or more times.

print(fruit_series.apply(lambda n: n if n.lower().count('o') >= 2 else None ))

# 7 Write the code to get only the string values
#   containing the substring "berry".

mask = ('berry' in fruit_series)
print(mask)

print(fruit_series[fruit_series.str.contains('berry')].values)

# 8 Write the code to get only the string 
# values containing the substring "apple".

print(fruit_series[fruit_series.str.contains('apple')].values)

# 9 Which string value contains the most vowels?

print("\nContains the most vowels: ")
print(fruit_series[fruit_series.apply(count_vowels).idxmax()])


#/******************************* EXCERCISE PT 3 *************************/

letters_series = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))

# 1 Which letter occurs the most frequently in the letters Series?

print(f"Most frequent letter: {letters_series.value_counts().nlargest(n=1)}")

# 2 Which letter occurs the Least frequently?

print(f"Least frequent letter: {letters_series.value_counts().nsmallest(n=1)}")

# 3 How many vowels are in the Series?
vowels = ['a', 'e', 'i', 'o', 'u']
print(f"# of vowels in series: {letters_series[letters_series.isin(vowels)].count()}")

# 4 How many consonants are in the Series?

print(f"# of consanants in series: {letters_series[~letters_series.isin(vowels)].count()}")

# 5 Create a Series that has all of the same letters but uppercased.

upper_cased_series = letters_series.str.upper()
print(upper_cased_series)

# 6 Create a bar plot of the frequencies of the 6 most 
#   commonly occuring letters.

letters_series.value_counts().nlargest(n=6, keep='all').plot.bar()

#plt.show()


numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# 7 What is the data type of the numbers Series?

print(numbers.dtype)
# string

# 8 How many elements are in the number Series?

print(numbers.size) # >> 20

# 9 Perform the necessary manipulations by accessing Series attributes 
#   and methods to convert the numbers Series to a numeric data type.

numbers = numbers.str.replace('$', "")
numbers = numbers.str.replace(',', "")
numbers = numbers.astype('float')
print(numbers)

# 10 Run the code to discover the maximum value from the Series.

print(numbers.max())

# 11 Run the code to discover the minimum value from the Series.

print(numbers.min())

# 12 What is the range of the values in the Series?

print(f"range: {numbers.max() - numbers.min()}")

# 13 Bin the data into 4 equally sized intervals or 
#    bins and output how many values fall into each bin.

print(f"Values in each bin: {numbers.value_counts(bins=4)}")

# 14 Plot the binned data in a meaningful way. Be sure to 
#    include a title and axis labels.

numbers.value_counts(bins=4).plot.bar()
number_bins = numbers.value_counts(bins=4)
print(4789988.16-3592560.777)
print(2395133.385 - 1197705.993)
plt.title('Distribution of Values in Numbers Series')
plt.xticks(rotation=45)
plt.xlabel('Number Ranges')
plt.ylabel('Frequency')
plt.show()
