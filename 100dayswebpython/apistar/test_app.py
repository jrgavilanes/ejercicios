import pdb  # Para debuggear

from apistar import test

from app import app, cars, CAR_NOT_FOUND

client = test.TestClient(app)


def test_list_cars():
    response = client.get('/')
    assert response.status_code == 200

    json_resp = response.json()
    car_count = len(cars)
    assert len(json_resp) == car_count

    expected = {'id': 1, 'manufacturer': 'Mercedes-Benz',
                'model': '500SEC', 'year': 1993,
                'vin': '1FTEW1CM9CF529793'}
    assert json_resp[0] == expected
    # pdb.set_trace()
    

def test_create_car():
    # pdb.set_trace()
    car_count = len(cars)
    data = {'manufacturer': 'Honda',
            'model': 'some_model',
            'year': 2018}

    response = client.post('/', data=data)

    assert response.status_code == 201
    assert len(cars) == car_count + 1

    response = client.get('/1001/')
    expected = {'id': 1001, 'manufacturer': 'Honda',
                'model': 'some_model', 'year': 2018, 'vin': ''}
    assert response.json() == expected

    data = {'manufacturer': 'Lotus',
            'model': 'some_other_model',
            'year': 2019,
            'vin': 123}
    response = client.post('/', data=data)
    assert response.status_code == 201
    expected = {'id': 1002, 'manufacturer': 'Lotus',
                'model': 'some_other_model', 'year': 2019,
                'vin': '123'}

    response = client.get('/1002/')
    assert response.json() == expected
    assert len(cars) == car_count + 2   
