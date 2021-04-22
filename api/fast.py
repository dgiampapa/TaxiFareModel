
# write some code for the API here
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict_fare")
def predict_fare(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):

    df1 = pd.DataFrame(columns = ['key', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count'])

    df1 = df1.append(
    {
    'key': pickup_datetime,
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
    }, ignore_index=True
    )
    df1.set_index('key', inplace=True)

    return {'pickup_datetime': pickup_datetime, 'pickup_longitude': pickup_longitude,'pickup_latitude':pickup_latitude, 
            'dropoff_longitude': dropoff_longitude, 'dropoff_latitude': dropoff_latitude, 'passenger_count' : passenger_count}