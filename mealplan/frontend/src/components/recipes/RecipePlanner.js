import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getRecipes } from "../../actions/recipes";
import { Form, Input, Button, Select, Row, Col, Card } from "antd";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import { getIngredients, getIngredientUnits } from "../../actions/ingredients";
import NutritionTable from "../common/NutritionTable";
import {
  computeRecipeNutrition,
  sumNutritions,
  scaleNutrition,
} from "../../utils/nutrition";
import { useForm } from "antd/lib/form/util";

const RecipePlanner = (props) => {
  const [form] = useForm();
  const dispatch = useDispatch();
  const userRecipes = useSelector((state) => state.recipes.recipes);
  const userIngredients = useSelector((state) => state.ingredients.ingredients);
  const units = useSelector((state) => state.ingredients.units);
  const [totalNutrition, setTotalNutrition] = useState();

  useEffect(() => {
    dispatch(getRecipes());
    dispatch(getIngredients());
    dispatch(getIngredientUnits());
  }, []);

  const onFinish = (values) => {
    console.log(values);
    console.log(userRecipes);
  };

  const onValuesChange = () => {
    const values = form.getFieldsValue();
    const nutritions = values.recipes.map((r) => {
      if (!r) return {};
      // Find the full recipe
      const recipe = userRecipes.find((ur) => ur.id == r.recipe);
      const scale =
        r.servings && recipe.servings ? r.servings / recipe.servings : 1;
      const nutrition = computeRecipeNutrition(recipe, userIngredients, units);
      return nutrition ? scaleNutrition(nutrition, scale) : null;
    });
    setTotalNutrition(sumNutritions(nutritions));
  };

  const RecipeItem = ({ recipe, removeRecipe }) => (
    <Row key={recipe.key}>
      <Col span={8}>
        <Form.Item
          wrapperCol={{ span: 24 }}
          key={[recipe.key, "recipe"]}
          fieldKey={[recipe.fieldKey, "recipe"]}
          name={[recipe.name, "recipe"]}>
          <Select showSearch optionFilterProp="children">
            {userRecipes.map((r) => (
              <Select.Option key={r.id}>
                {r.title}
                {r.servings && ` (${r.servings} servings)`}
              </Select.Option>
            ))}
          </Select>
        </Form.Item>
      </Col>
      <Col span={4}>
        <Form.Item
          wrapperCol={{ span: 24 }}
          key={[recipe.key, "servings"]}
          fieldKey={[recipe.fieldKey, "servings"]}
          name={[recipe.name, "servings"]}>
          <Input placeholder="Servings" type="number" />
        </Form.Item>
      </Col>
      <Col span={1}>
        <MinusCircleOutlined
          style={{ margin: "0 8px" }}
          onClick={() => removeRecipe(recipe.name)}
        />
      </Col>
    </Row>
  );

  const initialValues = { recipes: [{}] };

  return (
    <Card>
      <NutritionTable nutrition={totalNutrition} />
      <Form
        form={form}
        onFinish={onFinish}
        initialValues={initialValues}
        onValuesChange={onValuesChange}>
        <Form.List
          label="Recipes"
          key={"recipes"}
          name={"recipes"}
          fieldKey={"recipes"}>
          {(recipes, { add: addRecipe, remove: removeRecipe }) => (
            <div>
              {recipes.map((recipe) => (
                <RecipeItem
                  recipe={recipe}
                  removeRecipe={removeRecipe}
                  key={`recipe_item_${recipe.name}`}
                />
              ))}
              <Form.Item wrapperCol={{ span: 24 }}>
                <Button
                  type="dashed"
                  onClick={() => addRecipe()}
                  style={{ width: "100%" }}>
                  <PlusOutlined /> Add recipe
                </Button>
              </Form.Item>
            </div>
          )}
        </Form.List>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Compute or something
          </Button>
        </Form.Item>
      </Form>
    </Card>
  );
};

export default RecipePlanner;
