from contract.DataMapper import FoodCompositionMapper
from data.FoodCompositionRepository import FoodCompositionRepository


class FoodCompositionService():
    def get_nutrition_facts(self, id: int):
        try:
            mapper = FoodCompositionMapper();
            repository = FoodCompositionRepository()
            
            data_model = repository.select_by_id(id)
            result = mapper.map(data_model)
            
            print(result)
            return result
            
        except Exception as e:
            raise e