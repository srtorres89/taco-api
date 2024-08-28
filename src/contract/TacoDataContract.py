from pydantic import BaseModel
from typing import Optional


class FoodCompositionResponse(BaseModel):
    food: Optional[str]
    category: Optional[str]
    calories: Optional[float]
    protein: Optional[float]
    carbohydrate: Optional[float]
    fat: Optional[float]
    
