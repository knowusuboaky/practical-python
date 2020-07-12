# bounce.py
#
# Exercise 1.5
height = 100
bounce = 3/5

for i in range(10):
    height *= bounce
    print(round(height, 4))
