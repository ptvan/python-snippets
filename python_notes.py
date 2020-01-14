# iterate over two lists simultaneously
xs = [1, 3, 5, 7]
ys = [2, 4, 6, 8]

for x, y in zip(xs, ys):
    print(x, y)

# regex
import re

mystring = "my input string, which has 1,2,3 ,4 & lots of other stuff!"
mystring.replace("1", "one")
re.findall(",", mystring)

# file I/O
import os

dirnames = [name for name in os.listdir('/Users/ptv/') if os.path.isdir(os.path.join('/Users/ptv', name))]
