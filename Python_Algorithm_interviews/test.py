import re

a = 'Bob hit a ball, the hit BALL fle  far after it  as hit.'
b = re.sub('[\W]', ' ', a)
print(b)