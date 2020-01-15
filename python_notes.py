# iterate over two lists simultaneously
xs = [1, 3, 5, 7]
ys = [2, 4, 6, 8]
for x, y in zip(xs, ys):
    print(x, y)

# strings
import re
mystring = "-my input string, which has 1,2,3 ,4 & lots of other stuff!  "
mystring.lstrip("-")
mystring.replace("1", "one")
re.findall(",", mystring)

# numbers
import decimal
decimal.Decimal('2.5') + decimal.Decimal('2.6')
round(47584, -1)

# file I/O
import os
dirnames = [name for name in os.listdir('/Users/ptv/') if os.path.isdir(os.path.join('/Users/ptv', name))]

import gzip
with gzip.open("myfile.gz", 'rt') as f:
    text = f.read()
with gzip.open("otherfile.gz", 'wt', compresslevel=5) as f:
    f.write(text)