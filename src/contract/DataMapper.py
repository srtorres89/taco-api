from contract.TacoDataContract import FoodCompositionResponse, FoodWithCompositionResponse, FoodResponse


class FoodCompositionMapper():
    def map(self, model):
        result = FoodCompositionResponse(calories = model.calories, \
                                        protein = model.protein, \
                                        carbohydrate = model.carbohydrate, \
                                        totalfat = model.totalfat, \
                                        saturated_fat = model.saturated_fat, \
                                        trans_fat = model.trans_fat, \
                                        monounsaturated_fat = model.monounsaturated_fat, \
                                        polyunsaturated_fat = model.polyunsaturated_fat, \
                                        fiber = model.fiber, \
                                        sodium = model.sodium, \
                                        iron = model.iron, \
                                        calcium = model.calcium, \
                                        sugar = model.sugar, \
                                        cholesterol = model.cholesterol, \
                                        beta_glucan = model.beta_glucan, \
                                        omega3 = model.omega3, \
                                        portion_size = model. portion_size)
        
        return result
    
    def map2(self, model):
        result = FoodWithCompositionResponse(name = model.name, \
                                             calories = model.calories, \
                                             protein = model.protein, \
                                             carbohydrate = model.carbohydrate, \
                                             totalfat = model.totalfat, \
                                             saturated_fat = model.saturated_fat, \
                                             trans_fat = model.trans_fat, \
                                             monounsaturated_fat = model.monounsaturated_fat, \
                                             polyunsaturated_fat = model.polyunsaturated_fat, \
                                             fiber = model.fiber, \
                                             sodium = model.sodium, \
                                             iron = model.iron, \
                                             calcium = model.calcium, \
                                             sugar = model.sugar, \
                                             cholesterol = model.cholesterol, \
                                             beta_glucan = model.beta_glucan, \
                                             omega3 = model.omega3, \
                                             portion_size = model. portion_size)
        
        return result

    
class FoodMapper():
    def map(self, model):
        result = FoodResponse(id = model.id, \
                             name = model.name, \
                             category = model.food_category, \
                             brand = model.food_brand)
        
        return result
    
    def map_list(self, model):
        result = []
        for item in model:
            result.append(FoodResponse(id = item.id, \
                                       name = item.name, \
                                       category = item.food_category, \
                                       brand = item.food_brand))
            
        return result