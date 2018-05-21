from django.test import TestCase

from datetime import timedelta

from .models import Nutrition, Ingredient, Recipe, Unit


class NutritionModelTests(TestCase):

    # Addition

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

    def test_add_nutrition_and_number(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        # n + Nutrition should return Nutrition
        self.assertEquals(n1, n1 + 1.5)
        self.assertEquals(n1, 1.5 + n1)

    def test_add_nutrition_and_nonnumber(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        with self.assertRaises(TypeError):
            n1 + []
        with self.assertRaises(TypeError):
            n1 + "yoyoyo"

    def test_add_nutritions_with_none(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=1, fat_saturated=2.5)
        n2 = Nutrition(calories=200, fat=11.2, carbs=5.7, protein=2.1,
                       ingredient=None, id=2, fiber=3.3)
        n3 = Nutrition(calories=300, fat=21.2, carbs=11, protein=4.2,
                       ingredient=None, id=0, fat_saturated=2.5, fiber=3.3)
        self.assertEquals(n1 + n2, n3)
        self.assertEquals(n2 + n1, n3)

    # Multiplication

    def test_multiply_nutrition_by_nonnumber(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        with self.assertRaises(TypeError):
            n1 * n1
        with self.assertRaises(TypeError):
            n1 * "yoyoyo"

    def test_multiply_nutrition_by_one(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        self.assertEquals(n1, n1 * 1)
        self.assertEquals(n1, 1 * n1)

    def test_multiply_nutrition_by_two(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        self.assertEquals(n1 * 2, n1 + n1)
        self.assertEquals(2 * n1, n1 + n1)

    def test_multiply_nutrition_by_number(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        for i in range(0, 100):
            x = i / 10.0
            multiplied = n1 * x
            # Just test for calories, other fields should behave the same
            self.assertEquals(n1.calories * x, multiplied.calories)

    def test_multiply_ingredient_nutrition(self):
        i1 = Ingredient(name="Orange", unit_type="g", id=1)
        n1 = Nutrition(calories=300, fat=21.2, carbs=7.3, protein=5.1,
                       ingredient=i1, id=0)
        self.assertEquals(n1 * 2.0, 2.0 * n1)

    # Division

    def test_divide_nutrition_by_number(self):
        n1 = Nutrition(calories=250, fat=10, carbs=5.5, protein=10.5,
                       ingredient=None, id=0)
        n2 = Nutrition(calories=100.0, fat=4.0, carbs=2.2, protein=4.2,
                       ingredient=None, id=0)
        self.assertEquals(n1 / 2.5, n2)
        self.assertEquals(n1 / 2.5, n1 * (1/2.5))

    def test_divide_nutrition_by_nonnumber(self):
        n1 = Nutrition(calories=100, fat=10, carbs=5.3, protein=2.1,
                       ingredient=None, id=0)
        with self.assertRaises(TypeError):
            n1 / n1
        with self.assertRaises(TypeError):
            n1 / "yoyoyo"


class RecipeModelTests(TestCase):

    def test_get_recipe_nutrition(self):
        apple = Ingredient(name="Apple", unit_type="g")
        apple.save()
        apple_nutrition = Nutrition(
            calories=99, fat=0, carbs=10.2, protein=0.2,
            ingredient=Ingredient.objects.get(name__contains="Apple")
        )
        apple_nutrition.save()
        orange = Ingredient(name="Orange", unit_type="g")
        orange.save()
        orange_nutrition = Nutrition(
            calories=120, fat=0.1, carbs=14.2, protein=0.3,
            ingredient=Ingredient.objects.get(name__contains="Orange")
        )
        orange_nutrition.save()

        apples_and_oranges = Recipe(
            name="Apples and Oranges", servings=1, directions="do it",
            prep_time=timedelta(minutes=2), cook_time=timedelta(minutes=1)
        )
        apples_and_oranges.save()

        grams = Unit(unit_type="g", value=1, name="grams", shorthand="g")
        grams.save()

        apples_and_oranges.recipeingredient_set.create(
            ingredient=apple, quantity=80.0,
            unit=Unit.objects.get(name__contains="grams")
        )
        apples_and_oranges.recipeingredient_set.create(
            ingredient=orange, quantity=160.0,
            unit=Unit.objects.get(name__contains="grams")
        )

        self.assertEquals(
            apples_and_oranges.get_recipe_nutrition(),
            Nutrition(calories=271.2, fat=0.16, carbs=30.88, protein=0.64,
                      ingredient=None, id=0)
        )
