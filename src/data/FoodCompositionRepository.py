from sqlmodel import Session, create_engine, join, select
from data.FoodCompositionModel import Category, Ingredient, PortionSize, NutritionFacts


engine = create_engine("postgresql://postgres:postgres@localhost:5432/nutritiondb")


class FoodCompositionRepository():
    def select_by_id(self, id: int):
        with Session(engine) as session:
            statement = select(NutritionFacts.id, \
                       Ingredient.name, \
                       NutritionFacts.calories, \
                       NutritionFacts.protein, \
                       NutritionFacts.carbohydrate, \
                       NutritionFacts.fat, \
                       PortionSize.size, \
                       PortionSize.unit \
                      ).join(PortionSize) \
                        .join(Ingredient) \
                        .where(NutritionFacts.id == id)
            food_composition = session.exec(statement).first()
            
            return food_composition
        
#with Session(engine) as session:
#    # statement = select(FoodComposition).where(FoodComposition.nutrition_facts_id == 1)
#    statement = select(NutritionFacts.id, \
#                       Ingredient.name, \
#                       NutritionFacts.calories, \
#                       NutritionFacts.protein, \
#                       NutritionFacts.carbohydrate, \
#                       NutritionFacts.fat, \
#                       PortionSize.size, \
#                       PortionSize.unit \
#                      ).join(PortionSize) \
#                        .join(Ingredient) \
#                        .where(NutritionFacts.id == 1)
#    print(statement)
#    
#    food_composition = session.exec(statement).first()
#    
#    print(food_composition.name)