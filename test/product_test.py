import requests
from requests.models import Response

BASEURL = "http://localhost:5000/api/v1"

def base_test_api_can_upsert(request_data:dict , isUpdate:bool = False):
    response_create_data:Response = None
    if isUpdate:
        response_create_data = request_api_update(request_data)
    else:
        response_create_data = request_api_create(request_data)
    assert check_status_code(response_create_data)
    
    data = response_create_data.json()

    assert data["name"] == request_data["name"]
    assert data["price"] == request_data["price"]
    assert data["qty"] == request_data["qty"]
    assert data["desc"] == request_data["desc"]

    response_get_data = request_api_get_one(data["id"])
    print(response_get_data.status_code)

    assert check_status_code(response_get_data)
    print("DATA SUCCESSFULY ADDED")

    print(data)

def test_api_can_update():
    request_data = init_upsert_api_request("c946f0fc238243a093eb90dce581095b")
    base_test_api_can_upsert(request_data , True)
    pass

def test_api_update_with_sql_injection():
    request_data = init_upsert_api_with_sql_injection("c946f0fc238243a093eb90dce581095b")
    base_test_api_can_upsert(request_data , True)
    pass

def test_api_update_with_wrong_format():
    request_data = init_upsert_api_with_wrong_format("c946f0fc238243a093eb90dce581095b")
    response_create_data = request_api_create(request_data)
    assert check_status_code(response_create_data)
    
    data = response_create_data.json()
    print("DATA SUCCESSFULY ADDED")
    pass

def test_api_can_create():
    request_data = init_upsert_api_request()
    base_test_api_can_upsert(request_data)
    pass

def test_api_create_with_sql_injection():
    request_data = init_upsert_api_with_sql_injection()
    base_test_api_can_upsert(request_data)
    pass

def test_api_create_with_wrong_format():
    request_data = init_upsert_api_with_wrong_format()
    response_create_data = request_api_create(request_data)
    assert check_status_code(response_create_data)
    
    data = response_create_data.json()
    print("DATA SUCCESSFULY ADDED")
    pass

def test_api_get_one():
    param_id = init_request_get_id()
    response = request_api_get_one(param_id)

    assert check_status_code(response)
    pass

def test_api_get_all():
    response = request_api_get_all({})

    assert check_status_code(response)
    assert len(response.json()) > 0
    pass

def check_status_code(response:Response):
    return response.status_code in [200 , 201]

def init_upsert_api_request(id:str=""):
    data = {
        "id" : id,
        "name" : "from test",
        "price" : 4,
        "qty" : 1,
        "desc" : "desc from test",
        "createdAt" : 0,
        "updatedAt" : 0
    }

    if id != "":
        data["name"] = "update from test 2"
        data["desc"] = "update from test 2"

    return data

def init_upsert_api_with_sql_injection(id:str=""):
    return {
        "id" : id,
        "name" : "; SHOW TABLES --",
        "price" : 4,
        "qty" : 1,
        "desc" : "; SHOW TABLES --",
        "createdAt" : 0,
        "updatedAt" : 0,
    }

def init_upsert_api_with_wrong_format(id:str=""):
    return {
        "id" : id,
        "name" : "from test",
        "price" : "",
        "qty" : "",
        "desc" : "desc from test",
        "createdAt" : "",
        "updatedAt" : "",
    }

def request_api_get_one(id:str):
    response = requests.get(BASEURL+f"/get-one?id={id}")
    print(f"<GET> {BASEURL}/get-one?id={id}")
    return response

def request_api_create(data:dict):
    response = requests.post(BASEURL+"/add" , json=data)
    print(f"<POST> {BASEURL}/add \n payload : {data}")
    return response

def request_api_update(data:dict):
    response = requests.put(BASEURL+"/update" , json=data)
    print(f"<PUT> {BASEURL}/update \n payload : {data}")
    return response

def request_api_get_all(param:dict):
    response = requests.post(BASEURL+"/get-all" , json=param)
    print(f"<POST> {BASEURL}/add \n payload : {param}")
    return response

def init_request_get_id():
    return "9455050a91ea4d2480ed239d70789921"