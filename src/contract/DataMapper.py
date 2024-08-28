from contract.TacoDataContract import FoodCompositionResponse


class FoodCompositionMapper():
    def map(self, model):
        result = FoodCompositionResponse(food= model.name, \
                                        category = model.name, \
                                        calories = model.calories, \
                                        protein = model.protein, \
                                        carbohydrate = model.carbohydrate, \
                                        fat = model.fat)
        
        return result