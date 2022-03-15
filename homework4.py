a = 35
b = 25
c = 75
if a > b and a > c:
	print('"a" is MAX')
if b > a and b > c:
	print('"b" is MAX')
elif c > a and c > b:
	print('"c" is MAX')
if a < b and a < c:
	print('"a" is MIN')
if b < a or b < c:
	print('"b" is MIN')
elif c < a or c < b:
	print('"c" is MIN')
else:
	print('FAILED')

