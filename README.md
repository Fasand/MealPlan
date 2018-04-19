# MealPlan
Meal planner which keeps the ingredients and recipes you use (and no more) and your inventory

# Why does (will) this exist?
I'm lazy. That's really it. I've wanted something like this for a long time, be it just for keeping my inventory and not having to worry about what I need to buy, having an easy way to plan what I'm going to eat over the week, or even having some fancy statistics of what I've eaten in the past. This is the app I've always wanted – or at least hopefully will be one day.

# Philosophy of my approach
There are several very well-known applications for managing food, meals, nutrition, and whatnot. If tracking nutrition is the primary goal, you can use apps like [MyFitnessPal](http://myfitnesspal.com/) or [cronometer](https://cronometer.com/), which offer much more functionality in the nutrition domain than MealPlan ever should. If you just want something to track the recipes you know and plan what you're going to eat, you can use apps like [my diet meal plan](https://mydietmealplan.com/) (which also has some nutritional planning) or even just [Trello](https://trello.com/) or Excel. For your inventory, same thing.

However, these apps either offer very limited functionality (unless you want to create super-impressive function-packed spreadsheets), narrow functionality, or even too much functionality in one domain. I personally love MyFitnessPal but to be completely honest I don't need the access to every single ingredient on the planet. It is a fantastic idea but it often backfires when some ingredients/products have misleading/conflicting information.

My philosophy is simple: only include things that you actually use. You shouldn't have the option to include "Toasted sesame oil" in your recipe if you don't own it, have never used it, or have never even heard of it. On the other hand, if you actually use an ingredient frequently, you should absolutely have it handy, along with sufficient information (like nutrition, if you're into that), and you shouldn't have to wait for 5 seconds just to add it to your meal plan (I'm looking at you, MyFitnessPal).

## Why does every ingredient have nutrition and price? I though this was just a planner!
I'll explain later but I have my reasons... Also, you don't really have to use either of these – just type 0 instead of a value.

# Description of the application
*TBA*

# Roadmap
I have big plans. But I have other plans (like exams) as well, unfortunately. So I've split up some of the things I'd like to do into abstract time segments and I'll update this as time goes by.

## Completed
- [X] not much really

## Very soon
- [ ] have database models for ingredients, ... set up
- [ ] show content of DB models in their respective views
- [ ] set up Django admin for DB models
- [ ] add things to DB directly from their views
- [ ] advanced unit manipulation (custom units etc.)
- [ ] create recipes comfortably (search rather than ingredient IDs)

## Soon-ish
- [ ] the actual planner
- [ ] nutrition calculation
- [ ] shopping list from planned recipes
- [ ] "back from the grocery store" - easy add to inventory

## When the time comes...
- [ ] fancy statistics about what you eat

# Installation
*TBA*