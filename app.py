from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle 
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):
    age : int
    bmi : int
    children : int
    Sex : int
    Smoker : int
    Region : int

model = pickle.load(open('model/expense_model.pkl', 'rb'))

# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to Render Fast Api'}

@app.post('/prediction')
def getPrediction(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    age = int(input_dictionary['age'])
    bmi = int(input_dictionary['bmi'])
    children = int(input_dictionary['children'])
    sex = int(input_dictionary['Sex'])
    smoker = int(input_dictionary['Smoker'])
    region = int(input_dictionary['Region'])

    #get prediction
    input_cols = [[age, bmi, children, sex, smoker, region]]
    prediction = model.predict(input_cols)
    output = round(prediction[0], 2)
    return "Your predicted annual healthcare expense is ${}".format(output)
