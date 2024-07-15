import requests

response = requests.get('http://localhost:5000/tasks')
print(response.text, response.status_code)
print('------------------')

response = requests.get('http://localhost:5000/tasks/1')
print(response.text, response.status_code)
print('------------------')

response = requests.delete('http://localhost:5000/tasks/1')
print(response.text, response.status_code)
print('------------------')

response = requests.get('http://localhost:5000/tasks')
print(response.text, response.status_code)




#expected = 'creating new car'
#actual = response.text
#assert expected == actual, f'Exp {expected} act {actual}'

#expected = 201
#actual = response.status_code
#assert expected == actual, f'Exp {expected} act {actual}'

#print(response.text, response.status_code)