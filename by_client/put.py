import requests
endpoint=requests.get('http://127.0.0.1:8000/get/1')
yes_no=input(f'{endpoint.json()}\nsiz yuqoridagi malumotlarni uzgartirasizmi?')
if yes_no=='yes':
    data=''
    put_data=requests.put('http://127.0.01:8000/put/1/',json=data)
else:

    no_data=requests.put('http://127.0.0.1:8000/post/1/',json=endpoint)


print(requests.get('http://127.0.0.1:8000/get/1').json())


