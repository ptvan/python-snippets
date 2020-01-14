# iterate over two lists simultaneously
xs = [1, 3, 5, 7]
ys = [2, 4, 6, 8]

for x, y in zip(xs, ys):
    print(x, y)

# regex
import re

mystring = "my input string, which has 1,2,3 ,4 & lots of other stuff!"
re.findall(",", mystring)
