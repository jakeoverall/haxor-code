import requests


def createCar():
    response = requests.post('http://bcw-sandbox.herokuapp.com/api/cars', json={
        "make": "Chevy",
        "model": "Carol",
        "year": 1999,
        "price": 12100,
        "color": "#f48225",
        "description": "it runs..... most days",
        "imgUrl": "https://www.popsci.com/uploads/2019/03/18/OKMPE5HF26V2BEBRKOCNO3S5T4.jpg?auto=webp"
    }, headers={"charset": "utf-8", "Content-Type": "application/json"})
    handleResponse(response)
    return response.json()


def deleteCar(id: str):
    response = requests.delete(
        f'http://bcw-sandbox.herokuapp.com/api/cars/{id}')
    handleResponse(response)


def handleResponse(response):
    if response.status_code == 200:
        print(f"✅ it worked {response.text}")
    else:
        print(f'❌ Request Failed {response.status_code} {response.text}')


car = createCar()
print('JSON', car)
deleteCar(car['id'])
