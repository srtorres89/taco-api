from pydantic import BaseModel
from typing import Optional


class FoodCompositionResponse(BaseModel):
    calories: Optional[float]
    protein: Optional[float]
    carbohydrate: Optional[float]
    totalfat: Optional[float]
    saturated_fat: Optional[float]
    trans_fat: Optional[float]
    monounsaturated_fat: Optional[float]
    polyunsaturated_fat: Optional[float]
    fiber: Optional[float]
    sodium: Optional[float]
    iron: Optional[float]
    calcium: Optional[float]
    sugar: Optional[float]
    cholesterol: Optional[float]
    beta_glucan: Optional[float]
    omega3: Optional[float]
    portion_size: Optional[float]
    
class FoodWithCompositionResponse(FoodCompositionResponse):
    name: Optional[str]
    
class FoodResponse(BaseModel):
    id: Optional[int]
    name: Optional[str]
    category: Optional[int]
    brand: Optional[int]
    