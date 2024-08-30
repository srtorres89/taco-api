from typing import Optional
from sqlmodel import SQLModel, Field


class FoodComposition(SQLModel, table=True):
    __tablename__ = "food_composition"
    id: Optional[int] = Field(default=None, primary_key=True)
    food_id: int | None = Field(default=None, foreign_key="food.id")
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
    
    
class Food(SQLModel, table=True):
    __tablename__ = "food"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]
    food_category: int | None = Field(default=None, foreign_key="food_category.id")
    food_brand: int | None = Field(default=None, foreign_key="food_brand.id")


class FoodCategory(SQLModel, table=True):
    __tablename__ = "food_category"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]


class FoodBrand(SQLModel, table=True):
    __tablename__ = "food_brand"
    id: Optional[int] = Field(default=None, primary_key=True)
    brand: Optional[str]
    inactive: Optional[bool]
