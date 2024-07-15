import requests

response = requests.post('http://localhost:5000/cars')

expected = 'creating new car'
actual = response.text
assert expected == actual, f'Exp {expected} act {actual}'

expected = 201
actual = response.status_code
assert expected == actual, f'Exp {expected} act {actual}'

print(response.text, response.status_code)