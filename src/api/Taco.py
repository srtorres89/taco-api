from fastapi import FastAPI
from service.FoodCompositionService import FoodCompositionService
from service.FoodService import FoodService


app = FastAPI(title="Taco API", \
             summary="API that provides nutrition facts for foods in our DB.", \
             version="0.0.1", \
             terms_of_service="", \
             contact={"name": "Daniel Torres", "url": "https://github.com/srtorres89/taco-api/blob/main/README.md", "email": "contact@daniel.com" }, \
             licence_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0.html"}
             )


@app.get("/api/{category}/foods")
async def retrieve_food_by_category(category: int):
    try:
        service = FoodService()
        data = service.get_food_list(category)
        
        return data
    except Exception as e:
        raise e

        
@app.get("/api/foods/food-composition/{id}")
async def retrieve_food_composition_by_id(id: int):
    try:
        service = FoodCompositionService()
        data = service.get_food_composition(id)
        
        return data
        
    except Exception as e:
        raise e
        

@app.get("/api/foods/{id}/food-composition")
async def retrieve_food_composition_by_food(id: int):
    try:
        service = FoodCompositionService()
        data = service.get_food_composition_by_food(id)
        
        return data
    except Exception as e:
        raise e


@app.get("/api/foods/{id}")
async def retrieve_food_by_id(id: int):
    try:
        service = FoodService()
        data = service.get_food(id)
        
        return data
    except Exception as e:
        raise e