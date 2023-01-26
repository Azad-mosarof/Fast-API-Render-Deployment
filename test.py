import json
import requests

# url = "https://flask-render-app-ngp1.onrender.com/predict"
url = 'http://127.0.0.1:8000/prediction'

input_data_for_model = {
    'age' : 80,
    'bmi' : 9,
    'children' : 3,
    'Sex' : 1,
    'Smoker' : 40,
    'Region' : 2
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)