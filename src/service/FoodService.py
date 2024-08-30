from contract.DataMapper import FoodMapper
from data.FoodRepository import FoodRepository


class FoodService():
    def get_food_list(self, category):
        try:
            mapper = FoodMapper();
            repository = FoodRepository()
            
            data_model = repository.select_list(category)
            result = mapper.map_list(data_model)
            
            return result
        except Exception as e:
            raise e
            
    def get_food(self, id): 
        try:
            mapper = FoodMapper();
            repository = FoodRepository()
            
            data_model = repository.select_one(id)
            result = mapper.map(data_model)
            
            return result
        except Exception as e:
            raise e