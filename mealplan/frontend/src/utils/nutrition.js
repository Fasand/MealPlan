/*
 * nutritions: array(object())
 */
export const sumNutritions = (nutritions) => {
  if (nutritions && nutritions.length > 0) {
    // Remove empty dictionaries and nulls
    nutritions = nutritions.filter((i) => i && Object.keys(i).length > 0);
    // Sum all nutritions if any are left filtered or return null
    if (nutritions.length > 0) {
      return nutritions.reduce((acc, cur) =>
        Object.fromEntries(
          Object.entries(acc).map(([key, val]) => {
            // Both numbers, return sum
            if (typeof val == "number" && typeof cur[key] == "number")
              return [key, val + cur[key]];
            // Accumulater has a value already (number or other), leave it
            else if (val) return [key, val];
            // Otherwise return whatever is in the current one
            else return [key, cur[key]];
          })
        )
      );
    }
  }
  // If no nutritions left after filtering or in the first place
  return null;
};

export const scaleNutrition = (nutrition, multiplier) => {
  return Object.fromEntries(
    Object.entries(nutrition).map(([key, val]) =>
      typeof val == "number" ? [key, val * multiplier] : [key, val]
    )
  );
};

export const computeRecipeNutrition = (recipe, userIngredients, units) => {
  const nutritions =
    recipe && recipe.sections
      ? recipe.sections
          .map((section) =>
            section && section.ingredients
              ? section.ingredients.map((i) => {
                  // Only compute anything if data is present
                  if (!(i && i.ingredient && i.unit && i.amount)) return {};
                  // Find the necessary data in state
                  const ingredient = userIngredients.find(
                    (x) => x.id == i.ingredient
                  );
                  const unit = units.find((u) => u.id == i.unit);
                  // TODO: will need to convert to weight units for this
                  const inGrams = unit.amount_in_base * i.amount;
                  const multiplier = inGrams / 100.0;
                  // Compute scaled nutrition
                  return Object.fromEntries(
                    Object.entries(ingredient.nutrition).map(([key, val]) =>
                      typeof val == "number"
                        ? [key, val * multiplier]
                        : [key, val]
                    )
                  );
                })
              : []
          )
          .flat()
      : [];
  // Sum all nutritions or return null
  return sumNutritions(nutritions);
};
