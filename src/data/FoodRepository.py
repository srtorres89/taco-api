from sqlmodel import Session, create_engine, join, select
from data.FoodCompositionDbModel import Food, FoodCategory


engine = create_engine("postgresql://postgres:postgres@localhost:5432/foodcompositiondb")


class FoodRepository():
    def select_one(self, id):
        with Session(engine) as session:
            statement = select(Food.id, \
                               Food.name, \
                               Food.food_category, \
                               Food.food_brand) \
            .where(Food.id == id)
            
            food = session.exec(statement).first()
            
            return food
    
    def select_list(self, category):
        with Session(engine) as session:
            statement = select(Food.id, \
                               Food.name, \
                               Food.food_category, \
                               Food.food_brand) \
            .where(Food.food_category == category)
            
            food = session.exec(statement).all()

            return food
    