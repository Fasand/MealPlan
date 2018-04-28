from django.test import TestCase

from .models import Nutrition, Ingredient

class NutritionModelTests(TestCase):
    
    def test_add_two_ingredient_nutritions(self):
        i1 = Ingredient(name="Apple", unit_type="g")
        i2 = Ingredient(name="Orange", unit_type="g")
        n1 = Nutrition(calories=300, fat=21.2, carbs=7.3, protein=5.1,
            ingredient=i1, id=0)
        n2 = Nutrition(calories=210, fat=11.2, carbs=8.3, protein=4.1,
            ingredient=i2, id=1)
        add = n1 + n2
        radd = n2 + n1
        self.assertEquals(add, radd)


    def test_add_two_noningredient_nutritions(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
            ingredient=None, id=0)
        n2 = Nutrition(calories=300, fat=21.2, carbs=7.3, protein=5.1,
            ingredient=None, id=1)
        add = n1 + n2
        radd = n2 + n1
        self.assertEquals(add, radd)

    def test_add_three_nutritions(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
            ingredient=None, id=0)
        n2 = Nutrition(calories=300, fat=21.2, carbs=7.3, protein=5.1,
            ingredient=None, id=1)
        n3 = Nutrition(calories=200, fat=11.2, carbs=5.7, protein=2.1,
            ingredient=None, id=2)
        add = n1 + n2 + n3
        radd = n3 + n2 + n1
        another = n2 + n1 + n3
        self.assertEquals(add, radd)
        self.assertEquals(add, another)
        self.assertEquals(radd, another)

    def test_sum_nutritions(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
            ingredient=None, id=0)
        n2 = Nutrition(calories=300, fat=21.2, carbs=7.3, protein=5.1,
            ingredient=None, id=1)
        n3 = Nutrition(calories=200, fat=11.2, carbs=5.7, protein=2.1,
            ingredient=None, id=2)
        ns = [n1, n2, n3]
        s = sum(ns)
        self.assertEquals(s, n1 + n2 + n3)
