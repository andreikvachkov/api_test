import requests

numbers = []
with open('number.txt', 'r', encoding='utf-8') as file:
    for item in file:
        a = item.split(', ')
        a[1] = a[1][:-1]
        numbers.append(a)

match = 0
not_match = 0
no_response = 0
try:
    for item in range(0, len(numbers)):
        response = requests.get('http://rosreestr.subnets.ru/?get=num&format=json', params={'num': numbers[item][0]})
        if response:
            response.encoding = 'utf-8'
            json_response = response.json()
            numbers[item].append(json_response['0']['operator'])
            if numbers[item][1].lower() == numbers[item][2].lower():
                numbers[item].append('1')
                match += 1
            else:
                numbers[item].append('0')
                not_match += 1
        else:
            numbers[item].append('не получили ответ')
            numbers[item].append('2')
            no_response += 1
except:
    print('Ошибка запроса')

print(f'Совпало: {match}, Не совпало: {not_match}, Не получили ответ: {no_response}')

with open('number_result.txt', 'w', encoding='utf-8') as file:
    for item in numbers:
        file.write(str(item[0]) + ' | ' + str(item[1]) + ' | ' + item[2] + ' | ' + item[3] + '\n')