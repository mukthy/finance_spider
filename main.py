from fastapi import FastAPI
import grow_in

app = FastAPI()


@app.get('/')
async def root():
    return {'Description': 'Indian Stock Market Data'}


@app.get("/stock_price/{search_string}")
async def games_list(search_string: str):
    data = grow_in.grow_in_get_data(search_string)
    # print(games_lists, boolean, total_count)
    return data
