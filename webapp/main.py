import json
from os.path import dirname, abspath, join
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


current_dir = dirname(abspath(__file__))
historical_data = join(current_dir, "weather.json")

app = FastAPI()


# Loads the historical data for Portugal cities
with open(historical_data, "r") as f:
    data = json.load(f)


@app.get('/')
def root():
    return RedirectResponse(url='/docs', status_code=301)


@app.get('/countries')
def countries():
    # Only allows Portugal for now
    return list(data.keys())


@app.get('/countries/{country}/{city}/{month}')
def monthly_average(country: str, city: str, month: str):
    return data[country][city][month]
