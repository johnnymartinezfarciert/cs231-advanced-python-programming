
#maps a collecion of filtered out numbers who are divisible by three
#multiplies '.' times range

#instructor provided example
import math
print(
  *map(lambda n: '.'*n,
  filter(lambda n: not bool(n%3),
  range(10))),
  sep=' ')

# read the discussion, used the material from the instructor notes
# printes out the values of sin that helped immensely

print(
   *map(lambda n: ' ' * (n + 10),
   map(lambda n: int(math.sin(math.radians(n))* 10) ,
   filter(lambda n: not bool(n%20),
   range(360)))),
   sep='o\n'
)
print(
   *map(lambda n: n + 10, #int(sin(radian) * 10) some values will be negative ten this makes sure they are positive in order to appear on screen as a character
   map(lambda n: int(math.sin(math.radians(n))* 10) , # convert n to radians find the sin value of radian, multiply by 10 because sin value is a decimal between -1 and 1 convert to int
   filter(lambda n: not bool(n%10), #print all degrees divisible by 10 in the range of 360
   range(360)))),
   sep='\n'
)
# print(
#    *map(lambda s: ' ' * (s * 10),
#    map(lambda s: int(math.sin(math.radians(s)) * 10),
#    range(360))),
#    sep='o\n'
# )
