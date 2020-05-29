import React, { useEffect, Fragment, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { getRecipe, getDurationTypes } from "../../actions/recipes";
import { getIngredients, getIngredientUnits } from "../../actions/ingredients";
import Loading from "../common/Loading";
import { Row, Col, Card } from "antd";
import { computeRecipeNutrition } from "../../utils/nutrition";
import NutritionTable from "../common/NutritionTable";

const BORDER_BOTTOM = { borderBottom: "1px solid black" };
const TEXT_RIGHT = { textAlign: "right" };

const RecipeDetail = (props) => {
  const { id } = useParams();
  const dispatch = useDispatch();
  const recipe = useSelector((state) => state.recipes.recipe);
  const durationTypes = useSelector((state) => state.recipes.duration_types);
  const userIngredients = useSelector((state) => state.ingredients.ingredients);
  const units = useSelector((state) => state.ingredients.units);
  const [totalNutrition, setTotalNutrition] = useState();

  useEffect(() => {
    dispatch(getRecipe(id));
    dispatch(getDurationTypes());
    dispatch(getIngredients());
    dispatch(getIngredientUnits());
  }, []);

  useEffect(() => {
    if (recipe && userIngredients.length > 0 && units.length > 0)
      setTotalNutrition(computeRecipeNutrition(recipe, userIngredients, units));
  }, [userIngredients, units]);

  const SectionRow = ({ section, recipe }) => {
    const len = Math.max(section.ingredients.length, section.directions.length);
    // Precompute all directions to later find the index for each
    const all_directions = recipe.sections.map((sec) => sec.directions).flat();
    const els = [];
    // Add section header
    els.push(
      <tr key={`${section.id}_title`}>
        <th colSpan={4}>{section.title}</th>
      </tr>
    );
    for (let i = 0; i < len; i++) {
      const ing = section.ingredients[i];
      const direction = section.directions[i];
      // Compute the direction index out of the entire recipe
      const direction_idx =
        direction && all_directions.findIndex((d) => d.id == direction.id) + 1;
      const ingredient =
        ing && userIngredients.find((x) => x.id == ing.ingredient);
      const unit = ing && units.find((u) => u.id == ing.unit);
      const scale =
        recipe.scaled_to && ing && (ing.amount / recipe.scaled_to) * 100.0;

      els.push(
        <tr
          key={`${section.id}_${i}`}
          style={i == len - 1 ? BORDER_BOTTOM : {}}>
          <td>
            {ingredient && ingredient.title}
            {ingredient &&
              ing.preparation_method &&
              ", " + ing.preparation_method}
          </td>
          <td style={TEXT_RIGHT}>
            {ingredient && ing.amount} {unit && (unit.shorthand || unit.title)}
          </td>
          <td style={TEXT_RIGHT}>{scale && scale.toFixed(1) + "%"}</td>
          <td>{direction && `${direction_idx}. ${direction.description}`}</td>
        </tr>
      );
    }
    return <Fragment key={section.id}>{els}</Fragment>;
  };

  const TotalRow = ({ recipe }) => {
    // TODO: assumes all amounts are in the same unit (grams)

    const totalWeight = recipe.sections
      .map((s) => s.ingredients && s.ingredients.map((i) => i.amount))
      .flat()
      .reduce((acc, cur) => acc + cur, 0);
    const totalScale =
      recipe.scaled_to && (totalWeight / recipe.scaled_to) * 100.0;

    return (
      <tr>
        <th></th>
        <th style={TEXT_RIGHT}>{totalWeight.toFixed(1)} g</th>
        <th style={TEXT_RIGHT}>{totalScale.toFixed(1)}%</th>
        <th></th>
      </tr>
    );
  };

  if (!recipe) return <Loading />;
  return (
    <Card>
      <Row className="mb-3">
        <Col span={12}>
          <h1>{recipe.title}</h1>
          <p>{recipe.description}</p>
        </Col>
        <Col span={12}>
          <NutritionTable
            nutrition={totalNutrition}
            numServings={recipe.servings}
          />
        </Col>
      </Row>

      <table className="table">
        <thead>
          <tr style={BORDER_BOTTOM}>
            <th>Ingredient</th>
            <th style={{ width: "5rem", ...TEXT_RIGHT }}>Amount</th>
            <th style={{ width: "5rem", ...TEXT_RIGHT }}>Scale</th>
            <th>Direction</th>
          </tr>
        </thead>
        <tbody>
          {recipe.sections &&
            recipe.sections.map((section) => (
              <SectionRow key={section.id} section={section} recipe={recipe} />
            ))}
          <TotalRow recipe={recipe} />
        </tbody>
      </table>
    </Card>
  );
};

export default RecipeDetail;
