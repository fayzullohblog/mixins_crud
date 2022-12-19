import requests

endpoint=requests.get('http://127.0.0.1:8000/get/1/')
yes_or_no=input(f'{endpoint.json()}\n\n siz haqiqatdan yuqoridagi datani uchirmoqchimisiz? yes/no')

if yes_or_no=='yes':
    destroy=requests.delete('http://127.0.0:8000/destroy/1/')
    get_pk=requests.get('http://127.0.0:8000/get/1/')
    print(f'{get_pk.json()}\n OK')
else:
    print('O\'chirlmadi!!!')

# print(endpoint.json())