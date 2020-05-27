import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  createRecipe,
  updateRecipe,
  getDurationTypes,
} from "../../actions/recipes";
import {
  Form,
  Input,
  Button,
  Select,
  Row,
  Col,
  TimePicker,
  Checkbox,
  Rate,
} from "antd";
import moment from "moment";
import NutritionTable from "../common/NutritionTable";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";
import { getIngredients, getIngredientUnits } from "../../actions/ingredients";

// TODO: Closest thing to a "create empty": https://codesandbox.io/s/headless-silence-ky32o?fontsize=14&hidenavigation=1&theme=dark&file=/src/ModifiedSelect.js

const DURATION_FORMAT = "HH:mm:ss";

const RecipeForm = ({ recipe }) => {
  const [form] = Form.useForm();
  const dispatch = useDispatch();
  const [totalNutrition, setTotalNutrition] = useState(null);
  const durationTypes = useSelector((state) => state.recipes.duration_types);
  const userIngredients = useSelector((state) => state.ingredients.ingredients);
  const units = useSelector((state) => state.ingredients.units);

  useEffect(() => {
    dispatch(getDurationTypes());
    dispatch(getIngredients());
    dispatch(getIngredientUnits());
  }, []);

  useEffect(() => {
    // Compute the initial nutrition from provided recipe
    if (userIngredients.length > 0 && units.length > 0 && recipe)
      setTotalNutrition(computeTotalNutrition(recipe));
  }, [userIngredients, units]);

  const formLayout = {
    labelCol: { span: 8 },
    wrapperCol: { span: 16 },
  };
  const formTailLayout = {
    wrapperCol: { offset: 8, span: 16 },
  };

  const STYLE_SECTION = {
    borderBottom: "1px solid #CCC",
    marginBottom: "1rem",
    paddingBottom: "1rem",
  };

  const onFinish = (values) => {
    values = {
      ...values,
      sections: values.sections.map((section) => ({
        ...section,
        directions: section.directions
          ? section.directions.map((direction) => ({
              ...direction,
              duration: direction.duration
                ? direction.duration.format(DURATION_FORMAT)
                : direction.duration,
            }))
          : section.directions,
      })),
    };

    // Strip tags of whitespace
    if (values.tags)
      values.tags = values.tags.map((tag) => tag.trim()).join(",");
    // Update or create
    if (recipe) {
      dispatch(updateRecipe(recipe.id, values));
    } else dispatch(createRecipe(values));
  };

  const computeTotalNutrition = (recipe) => {
    // TODO: move to a separate nutrition lib
    const nutritions = recipe.sections
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
                  typeof val == "number" ? [key, val * multiplier] : [key, val]
                )
              );
            })
          : []
      )
      // Flatten and remove empty dictionaries
      .flat()
      .filter((i) => Object.keys(i).length != 0);
    // Sum all nutritions or return null
    if (nutritions.length > 0)
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
    else return null;
  };

  const onValuesChange = (changed) => {
    setTotalNutrition(computeTotalNutrition(form.getFieldsValue()));
  };

  // TODO: tags should be loaded from previously created ingredients

  // Convert all present durations to moment()
  const initialValues = recipe
    ? {
        ...recipe,
        sections: recipe.sections.map((section) => ({
          ...section,
          ingredients: section.ingredients.map((ingredient) => ({
            ...ingredient,
            // Convert so that it works as a correct key
            ingredient: String(ingredient.ingredient),
            unit: String(ingredient.unit),
          })),
          directions: section.directions.map((direction) => ({
            ...direction,
            // Convert so that it works as a correct moment() duration
            duration: direction.duration
              ? moment(direction.duration, DURATION_FORMAT)
              : direction.duration,
          })),
        })),
      }
    : {};

  return (
    <Form
      form={form}
      onFinish={onFinish}
      {...formLayout}
      onValuesChange={onValuesChange}
      initialValues={initialValues}>
      <Row>
        <Col span={12}>
          <Form.Item label="Title" name="title">
            <Input />
          </Form.Item>
          <Form.Item label="Description" name="description">
            <Input.TextArea />
          </Form.Item>
          <Form.Item label="Tags" name="tags">
            <Select mode="tags" tokenSeparators={[","]}></Select>
          </Form.Item>
          <Form.Item label="Sources" name="sources">
            <Input.TextArea />
          </Form.Item>
          <Form.Item label="Servings" name="servings">
            <Input type="number" />
          </Form.Item>
          <Form.Item label="Notes" name="notes">
            <Input.TextArea />
          </Form.Item>
          <Form.Item label="Difficulty" name="difficulty">
            <Rate />
          </Form.Item>
          <Form.Item label="Scaled to (100%)" name="scaled_to">
            <Input type="number" />
          </Form.Item>
        </Col>
        <Col span={12} style={{ padding: "0 1rem" }}>
          <NutritionTable nutrition={totalNutrition} />
        </Col>
      </Row>
      <h3>Sections</h3>
      <Form.List name="sections" wrapperCol={{ span: 24 }}>
        {(
          sections,
          { add: addSection, remove: removeSection, move: moveSection }
        ) => (
          <div>
            {sections.map((section) => (
              <div key={section.key} style={STYLE_SECTION}>
                <Row>
                  <Col span={4}>
                    <Form.Item>
                      <Button
                        type="dashed"
                        onClick={() =>
                          moveSection(section.name, section.name + 1)
                        }>
                        Down
                      </Button>
                      <Button
                        type="dashed"
                        onClick={() =>
                          moveSection(section.name, section.name - 1)
                        }>
                        Up
                      </Button>
                    </Form.Item>
                  </Col>
                  <Col span={17}>
                    <Form.Item
                      labelCol={{ span: 2 }}
                      wrapperCol={{ span: 21 }}
                      label="Title"
                      name={[section.name, "title"]}
                      key={[section.key, "title"]}
                      fieldKey={[section.fieldKey, "title"]}>
                      <Input />
                    </Form.Item>
                  </Col>
                  <Col span={3}>
                    <Button
                      type="danger"
                      onClick={() => removeSection(section.name)}>
                      Delete section
                    </Button>
                  </Col>
                </Row>
                <Row>
                  <Col span={12}>
                    <Form.List
                      label="Ingredients"
                      key={[section.key, "ingredients"]}
                      name={[section.name, "ingredients"]}
                      fieldKey={[section.fieldKey, "ingredients"]}>
                      {(
                        ingredients,
                        { add: addIngredient, remove: removeIngredient }
                      ) => (
                        <div>
                          {ingredients.map((ingredient) => (
                            <Row key={[section.key, ingredient.key]}>
                              <Col span={8}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[
                                    section.key,
                                    ingredient.key,
                                    "ingredient",
                                  ]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "ingredient",
                                  ]}
                                  name={[ingredient.name, "ingredient"]}>
                                  <Select
                                    showSearch
                                    optionFilterProp="children">
                                    {userIngredients.map((i) => (
                                      <Select.Option key={i.id}>
                                        {i.title}
                                      </Select.Option>
                                    ))}
                                  </Select>
                                </Form.Item>
                              </Col>
                              <Col span={6}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[
                                    section.key,
                                    ingredient.key,
                                    "preparation_method",
                                  ]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "preparation_method",
                                  ]}
                                  name={[
                                    ingredient.name,
                                    "preparation_method",
                                  ]}>
                                  <Input placeholder="Preparation method" />
                                </Form.Item>
                              </Col>
                              <Col span={4}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[section.key, ingredient.key, "amount"]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "amount",
                                  ]}
                                  name={[ingredient.name, "amount"]}>
                                  <Input placeholder="Amount" type="number" />
                                </Form.Item>
                              </Col>
                              <Col span={4}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[section.key, ingredient.key, "unit"]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "unit",
                                  ]}
                                  name={[ingredient.name, "unit"]}>
                                  <Select
                                    showSearch
                                    optionFilterProp="children">
                                    {units.map((unit) => (
                                      <Select.Option key={unit.id}>
                                        {unit.shorthand || unit.title}
                                      </Select.Option>
                                    ))}
                                  </Select>
                                </Form.Item>
                              </Col>
                              <Col span={1}>
                                <Form.Item
                                  valuePropName="checked"
                                  key={[
                                    section.key,
                                    ingredient.key,
                                    "optional",
                                  ]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "optional",
                                  ]}
                                  name={[ingredient.name, "optional"]}>
                                  <Checkbox />
                                </Form.Item>
                              </Col>
                              <Col span={1}>
                                <MinusCircleOutlined
                                  style={{ margin: "0 8px" }}
                                  onClick={() =>
                                    removeIngredient(ingredient.name)
                                  }
                                />
                              </Col>
                            </Row>
                          ))}
                          <Form.Item wrapperCol={{ span: 24 }}>
                            <Button
                              type="dashed"
                              onClick={() => addIngredient()}
                              style={{ width: "100%" }}>
                              <PlusOutlined /> Add ingredient
                            </Button>
                          </Form.Item>
                        </div>
                      )}
                    </Form.List>
                  </Col>
                  <Col span={12}>
                    <Form.List
                      label="Directions"
                      key={[section.key, "directions"]}
                      name={[section.name, "directions"]}
                      fieldKey={[section.fieldKey, "directions"]}>
                      {(
                        directions,
                        { add: addDirection, remove: removeDirection }
                      ) => (
                        <div>
                          {directions.map((direction) => (
                            <Row key={[section.key, direction.key]}>
                              <Col span={13}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[
                                    section.key,
                                    direction.key,
                                    "description",
                                  ]}
                                  fieldKey={[
                                    section.fieldKey,
                                    direction.fieldKey,
                                    "description",
                                  ]}
                                  name={[direction.name, "description"]}>
                                  <Input placeholder="Description" />
                                </Form.Item>
                              </Col>
                              <Col span={5}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[section.key, direction.key, "duration"]}
                                  fieldKey={[
                                    section.fieldKey,
                                    direction.fieldKey,
                                    "duration",
                                  ]}
                                  name={[direction.name, "duration"]}>
                                  <TimePicker format={"HH:mm:ss"} />
                                </Form.Item>
                              </Col>
                              <Col span={4}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[
                                    section.key,
                                    direction.key,
                                    "duration_type",
                                  ]}
                                  fieldKey={[
                                    section.fieldKey,
                                    direction.fieldKey,
                                    "duration_type",
                                  ]}
                                  name={[direction.name, "duration_type"]}>
                                  <Select>
                                    {durationTypes.map((dType) => (
                                      <Select.Option key={dType[0]}>
                                        {dType[1]}
                                      </Select.Option>
                                    ))}
                                  </Select>
                                </Form.Item>
                              </Col>
                              <Col span={1}>
                                <Form.Item
                                  valuePropName="checked"
                                  key={[section.key, direction.key, "optional"]}
                                  fieldKey={[
                                    section.fieldKey,
                                    direction.fieldKey,
                                    "optional",
                                  ]}
                                  name={[direction.name, "optional"]}>
                                  <Checkbox />
                                </Form.Item>
                              </Col>
                              <Col span={1}>
                                <MinusCircleOutlined
                                  style={{ margin: "0 8px" }}
                                  onClick={() =>
                                    removeDirection(direction.name)
                                  }
                                />
                              </Col>
                            </Row>
                          ))}
                          <Form.Item wrapperCol={{ span: 24 }}>
                            <Button
                              type="dashed"
                              onClick={() => addDirection()}
                              style={{ width: "100%" }}>
                              <PlusOutlined /> Add direction
                            </Button>
                          </Form.Item>
                        </div>
                      )}
                    </Form.List>
                  </Col>
                </Row>
              </div>
            ))}
            <Form.Item wrapperCol={{ span: 24 }}>
              <Button
                type="dashed"
                onClick={() => addSection()}
                style={{ width: "100%" }}>
                <PlusOutlined /> Add section
              </Button>
            </Form.Item>
          </div>
        )}
      </Form.List>

      <Form.Item {...formTailLayout}>
        <Button type="primary" htmlType="submit">
          {recipe ? "Update" : "Create"}
        </Button>
      </Form.Item>
    </Form>
  );
};

export default RecipeForm;
