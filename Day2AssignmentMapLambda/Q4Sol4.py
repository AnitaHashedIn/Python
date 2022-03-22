# lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
# Take the first two values, run the function on them. Then take the result and the next value and have a multiplication between them.
# etc. When no more values are left, return the last result.

import functools
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

print(functools.reduce(lambda a,b:a*b,lst1))

