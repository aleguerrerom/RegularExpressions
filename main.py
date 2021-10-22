import re

email = "aleguemad94@gmail.com"
expression = '[a-z]+'
parts = email.split('@')
matches = re.findall(expression, email)
price = 'Price: $189.50'
expression2 = 'Price: \$([0-9].*.50)'

print(matches)

name = matches[0]
domain = f'{matches[1]}.{matches[2]}'

name1 = parts[0]
domain1 = parts[1]

print(name)
print(domain)

print(name1)
print(domain1)

matches1= re.search(expression2, price)
print(matches1.group(0))
print(matches1.group(1))

price_with_comma = matches1.group(1).replace('.', '')
price_number = float(price_with_comma)
print(price_number)