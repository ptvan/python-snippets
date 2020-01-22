########
# LOOPS
########
xs = [1, 3, 5, 7]
ys = [2, 4, 6, 8]
for x, y in zip(xs, ys):
    print(x, y)
list(range(1, 100, 2))

########
# RANDOM
########
import random
random.seed(b'bytedata')
random.random()
random.randint(0, 5000)
fruits = ["apple", "pear", "kiwi", "orange", "plum"]
random.choice(fruits)
numbers = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(numbers)
random.sample(numbers, 3)

#########
# STRINGS
#########
mystring = "-my input string, which has 1,2,3 ,4 & lots of other stuff!  "
mystring.lstrip("-")
mystring.replace("1", "one")
mystring.startswith("my")
mystring.rjust(65, ".")
mystring + '  ' + 'some other string'

import re
re.findall(",", mystring)

########
# DATES & TIMES
########
from datetime import datetime
startstring = '2011-12-01'
startdate = datetime.strptime(startstring, '%Y-%m-%d')
duration = datetime.now() - startdate


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

##########
# FILE I/O
##########
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

#################
# DATA STRUCTURES
#################
import heapq

# find largest items
nums = [i for i in range(1, 21)] + [22, 22, 23]
print(heapq.nlargest(3, nums))

# find most common items in a list
from collections import Counter
bagofwords = "it was the best of times it was the worst of times".split()
word_counts = Counter(bagofwords)
word_counts.most_common(3)

# sorting & handling duplicates
hasdupes = [1, 25, 1, 80, 100, 125]
nodupes = set(hasdupes)
sorted = hasdupes.sort()

# subset a dict
ages = {
        'Mary': 20,
        'Bob': 56,
        'Alice': 9,
        'John': 15
}
adults = {key:value for key, value in ages.items() if value > 18}

########
# BASE64
########
# base64 is meant for byte data
import base64
mybytes = b'notastring'
base64.b64encode(mybytes)
