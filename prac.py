import numpy as np

marks = np.array([65, 72, 88, 91, 55, 79, 84, 68, 95, 74])

print(marks)

print( marks.dtype)

print( marks.shape)

print( np.sum(marks))

print(np.mean(marks))

print( np.max(marks))

print( np.min(marks))

print( np.argmax(marks))

print( np.argmin(marks))


# //////////////////////////////
# task 2

import numpy as np

salary = np.array([25000, 32000, 28000, 45000, 50000, 38000, 42000, 30000])

print( salary[0])

print( salary[-1])

print( salary[:4])

print( salary[-3:])

print( salary[1:-1])

salary[2] = 35000

salary[-1] = 33000

print( salary)

print( salary[salary > 35000])