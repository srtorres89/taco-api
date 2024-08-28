from typing import Optional
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    
    
class PortionSize(SQLModel, table=True):
    __tablename__ = "portion_size"
    id: Optional[int] = Field(default=None, primary_key=True)
    size: int
    unit: str


class Ingredient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: int | None = Field(default=None, foreign_key="category.id")


class NutritionFacts(SQLModel, table=True):
    __tablename__ = "nutrition_facts"
    id: Optional[int] = Field(default=None, primary_key=True)
    calories: float
    protein: float
    carbohydrate: float
    fat: float
    ingredient: int | None = Field(default=None, foreign_key="ingredient.id")
    portion: int | None = Field(default=None, foreign_key="portion_size.id")
    
    
class FoodComposition(SQLModel, table=False):
    __tablename__ = "food_composition"
    
    category_id: int
    food_id: int
    nutrition_facts_id: int
    category: str
    food: str
    calories: float
    protein: float
    carbohydrate: float
    fat: float
    portion: str
