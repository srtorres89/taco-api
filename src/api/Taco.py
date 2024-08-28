from fastapi import FastAPI
from service.FoodCompositionService import FoodCompositionService


app = FastAPI()


@app.get("/foods/nutrition-facts/{id}")
async def retrieve_by_id(id: int):
    try:
        service = FoodCompositionService()
        data = service.get_nutrition_facts(id)
        
        return data
        
    except Exception as e:
        raise e


@app.get("/foods/{category}")
async def retrieve_food_by_category(category: int):
    pass


@app.get("/foods/{id}/nutrition-facts")
async def retrieve_nutrition_facts_by_food(id: int):
    pass