from sqlmodel import Session, create_engine, join, select
from data.FoodCompositionDbModel import FoodCategory, FoodComposition, Food, FoodBrand


engine = create_engine("postgresql://postgres:postgres@localhost:5432/foodcompositiondb")


class FoodCompositionRepository():
    def select_by_id(self, id: int):
        with Session(engine) as session:
            statement = select(FoodComposition.id, \
                       FoodComposition.calories, \
                       FoodComposition.protein, \
                       FoodComposition.carbohydrate, \
                       FoodComposition.totalfat, \
                       FoodComposition.saturated_fat, \
                       FoodComposition.trans_fat, \
                       FoodComposition.monounsaturated_fat, \
                       FoodComposition.polyunsaturated_fat, \
                       FoodComposition.fiber, \
                       FoodComposition.sodium, \
                       FoodComposition.iron, \
                       FoodComposition.calcium, \
                       FoodComposition.sugar, \
                       FoodComposition.cholesterol, \
                       FoodComposition.beta_glucan, \
                       FoodComposition.omega3, \
                       FoodComposition.portion_size) \
            .where(FoodComposition.id == id)
            
            food_composition = session.exec(statement).first()
            
            return food_composition
        
    def select_one(self, id):
        with Session(engine) as session:
            statement = select(FoodComposition.id, \
                       Food.name, \
                       FoodComposition.calories, \
                       FoodComposition.protein, \
                       FoodComposition.carbohydrate, \
                       FoodComposition.totalfat, \
                       FoodComposition.saturated_fat, \
                       FoodComposition.trans_fat, \
                       FoodComposition.monounsaturated_fat, \
                       FoodComposition.polyunsaturated_fat, \
                       FoodComposition.fiber, \
                       FoodComposition.sodium, \
                       FoodComposition.iron, \
                       FoodComposition.calcium, \
                       FoodComposition.sugar, \
                       FoodComposition.cholesterol, \
                       FoodComposition.beta_glucan, \
                       FoodComposition.omega3, \
                       FoodComposition.portion_size) \
            .join(Food) \
            .where(Food.id == id)
            
            food_composition = session.exec(statement).first()
            
            return food_composition
        