#Version 1:
"""
for i in range(1, 101):
	if i%3 == 0:
		print("FizzBuzz") if i%5==0 else print("Fizz")
		continue
	if i%5 == 0:
		print("Buzz")
		continue
	print(i)
"""
#Version 2:
"""
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = i
    print(output)
"""
#Version 3:
"""
for i in range(1, 101):
    output = ''
    if i % 3 == 0: output += 'Fizz'
    if i % 5 == 0: output += 'Buzz'
    print(output or i)
"""
#Version 4: One Liner!!
for i in range(1,101):print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)
