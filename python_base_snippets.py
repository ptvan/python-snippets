
#################
# DATA STRUCTURES
#################
# sets DO NOT ALLOW DUPLICATES, items cannot be changed, but can be added
first_set = {1, "two", 3.0, 4}
second_set = {1.0, "two", "three", 4.0}
third_set = set(("one", 2.0, "three", 4))
third_set.add("five")
third_set.remove("one")

first_set - second_set
small_union = first_set | second_set
big_union = first_set.union(second_set, third_set)

# lists are ordered, and allow duplicates
hasdupes = [1, 25, 1, 80, 100, 125]
nodupes = set(hasdupes)
sorted = hasdupes.sort()

# tuples are ordered, allow duplicates and are IMMUTABLE, but can be modified by turning into list
Beatles = ("Ringo", "George", "John", "Paul")
most_famous = Beatles[2]
(drums, bass, vocals, guitar) = Beatles

fake_Beatles = list(Beatles)
fake_Beatles.append("Bob")
fake_Beatles = tuple(fake_Beatles)

musicians = Beatles + fake_Beatles
clones = Beatles * 2

# dicts
ages = {
        'Mary': 20,
        'Bob': 56,
        'Alice': 9,
        'John': 15
}
adults = {key: value for key, value in ages.items() if value > 18}

DNAstring = "ATACACGGGGCGAGAGATCTATCATA"
DNAcomplement = {"A": "T", "C": "G", "G": "C", "T": "A"}
''.join([DNAcomplement[c] for c in DNAstring])

# find largest items
import heapq
nums = [i for i in range(1, 21)] + [22, 22, 23]
print(heapq.nlargest(3, nums))

# find most common items in a list
from collections import Counter
bagofwords = "it was the best of times it was the worst of times".split()
word_counts = Counter(bagofwords)
word_counts.most_common(3)

###########
# STRINGS
###########
# string's built-in functions returns new string, leaves original unmodified
mystring = "-my input string, which has numbers like 1,2,3, \"quotes\" & lots of other stuff!  "
otherstring = "my other string, which is cleaner"
len(mystring)
mystring_reversed = mystring[::-1]
mystring.lstrip("-")
mystring.count(",")
mystring.find("numbers")
mystring.replace("1", "one")
mystring.startswith("my")
mystring.casefold()
mystring.rjust(65, ".")
first_20_chars = mystring[:21]
last_10_chars = mystring[10:]
indexed_backwards = mystring[-3:]
mystring + '  ' + 'some other string'

actuallyint = "47683"
int(actuallyint)
actuallyfloat = "4583.014"
float(actuallyfloat)

## regular expressions
# `findall` returns matches, `search` returns match positions
import re
re.findall(",", mystring) 
hits = re.search("which", mystring)
print(hits.span())


#########
# NUMBERS
#########
import decimal
decimal.Decimal('2.5') + decimal.Decimal('2.6')
round(47584, -1)
longfloat = 57486734658493.45
format(longfloat, ',')
format(longfloat, 'e')

# ints are signed, so conversions will return signed
longint = -20585777365759353646463 
bin(longint)
oct(longint)

# format() omits 0b/0o/0x prefixes
format(longint, 'b')

# to produce unsigned value, add in maximum value, eg. 128-bit
format(2**128 + longint, 'b')

# handling fractions
from fractions import Fraction
a = Fraction(4, 7)
b = Fraction(10, 19)
print(a)
c = a + b
c.numerator
float(c)

########
# LOOPS
########
xs = [1, 3, 5, 7]
ys = [2, 4, 6, 8]
for x, y in zip(xs, ys):
    print(x, y)
list(range(1, 100, 2))

# `continue` skips one iteration
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# `break` stops loop
statenames = ['Alaska', 'Wyoming', 'Texas', 'Florida']
for s in statenames:
    print(s)
    if s == 'Texas':
        print('found Lonestar !')
        break

# elif and else
statetimezones = ['AKST', 'MST', 'CST', 'EST']
USstates = dict(zip(statenames, statetimezones))
for z in USstates.keys():
    print(z)
    if z == 'Alaska':
        print('too far west, too cold !')
    elif z == 'Wyoming' or z == 'Texas':
        print('just right !')
    else:
        print('HOT !!! TOO HOT !')             

#############
# FUNCTIONS
#############

# map() returns a map object in Python3, so list() is necessary
unsorted_numbers = [45, 1, -8, 7, 3.1415, 0, 15561]
def multiply_and_add(x):
    return x*2 + 1
new_numbers = list(map(multiply_and_add, unsorted_numbers))

# lambdas are small anonymous functions
new_numbers = list(map(lambda x : x*2 + 1, unsorted_numbers))


################
# DATES & TIMES
################
from datetime import datetime
startstring = '2011-12-01'
startdate = datetime.strptime(startstring, '%Y-%m-%d')
duration = datetime.now() - startdate


############
# FILE I/O
############
import os
dirnames = [name for name in os.listdir('/Users/ptv/') if os.path.isdir(os.path.join('/Users/ptv', name))]

import gzip
with gzip.open("myfile.gz", 'rt') as f:
    text = f.read()
with gzip.open("otherfile.gz", 'wt', compresslevel=5) as f:
    f.write(text)
# for binary mode and check existing file
with gzip.open("filethatalreadyexists.gz", 'xb', compresslevel=5) as f:
    f.write(text)

#########
# BASE64
#########
# base64 is meant for byte data
import base64
mybytes = b'notastring'
base64.b64encode(mybytes)

#########
# RANDOM
#########
# random() returns a float, randint() returns an int, sample() returns multiple items of an iterable
import random
random.seed(b'bytedata')
random.random()
random.randint(0, 5000)
fruits = ["apple", "pear", "kiwi", "orange", "plum"]
random.choice(fruits)
numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
num1, num2, num3 = random.sample(numbers, 3)

######################
# DYNAMIC PROGRAMMING
######################

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)