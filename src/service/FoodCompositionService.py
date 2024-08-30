from contract.DataMapper import FoodCompositionMapper
from data.FoodCompositionRepository import FoodCompositionRepository


class FoodCompositionService():
    def get_food_composition(self, id: int):
        try:
            mapper = FoodCompositionMapper();
            repository = FoodCompositionRepository()
            
            data_model = repository.select_by_id(id)
            result = mapper.map(data_model)
            
            return result
        except Exception as e:
            raise e
    
    def get_food_composition_by_food(self, id):
        try:
            mapper = FoodCompositionMapper();
            repository = FoodCompositionRepository()
            
            data_model = repository.select_one(id)
            result = mapper.map2(data_model)
            
            return result
        except Exception as e:
            raise e
    
