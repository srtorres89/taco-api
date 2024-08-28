CREATE VIEW food_composition AS 
SELECT
	c.name as category,
	i.name as food,
	nf.calories,
	nf.protein,
	nf.carbohydrate,
	nf.fat,
	CONCAT(ps.size, ' ' , ps.unit) as portion
FROM category c 
INNER JOIN ingredient i ON
	c.id = i.category
INNER JOIN nutrition_facts nf ON
	i.id = nf.ingredient
INNER JOIN portion_size ps ON 
	ps.id = nf.portion