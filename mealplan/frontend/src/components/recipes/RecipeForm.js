import React from "react";
import { useDispatch } from "react-redux";
import { createRecipe, updateRecipe } from "../../actions/recipes";
import { Form, Input, Button, Select, Row, Col, Space, Checkbox } from "antd";
import { MinusCircleOutlined, PlusOutlined } from "@ant-design/icons";

const RecipeForm = ({ recipe }) => {
  const dispatch = useDispatch();

  const formLayout = {
    labelCol: { span: 8 },
    wrapperCol: { span: 16 },
  };
  const formTailLayout = {
    wrapperCol: { offset: 8, span: 16 },
  };

  const onFinish = (values) => {
    console.log(values);
    return;

    // Strip tags of whitespace
    if (values.tags)
      values.tags = values.tags.map((tag) => tag.trim()).join(",");
    // Update or create
    if (recipe) {
      dispatch(updateRecipe(recipe.id, values));
    } else dispatch(createRecipe(values));
  };

  // TODO: tags should be loaded from previously created ingredients

  const initialValues = recipe
    ? {
        ...recipe,
      }
    : {};

  return (
    <Form onFinish={onFinish} {...formLayout} initialValues={initialValues}>
      <Form.Item label="Title" name="title">
        <Input />
      </Form.Item>
      <Form.Item label="Description" name="description">
        <Input.TextArea />
      </Form.Item>
      <Form.Item label="Tags" name="tags">
        <Select mode="tags" tokenSeparators={[","]}></Select>
      </Form.Item>
      <h3>Sections</h3>
      <Form.List name="sections" wrapperCol={{ span: 24 }}>
        {(sections, { add: addSection, remove: removeSection }) => (
          <div>
            {sections.map((section) => (
              <div key={section.key}>
                <Form.Item
                  label="Title"
                  name={[section.name, "title"]}
                  key={[section.key, "title"]}
                  fieldKey={[section.fieldKey, "title"]}>
                  <Input />
                </Form.Item>
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
                              <Col span={12}>
                                <Form.Item
                                  wrapperCol={{ span: 24 }}
                                  key={[section.key, ingredient.key, "title"]}
                                  fieldKey={[
                                    section.fieldKey,
                                    ingredient.fieldKey,
                                    "title",
                                  ]}
                                  name={[ingredient.name, "title"]}>
                                  <Input
                                    placeholder="Ingredient search"
                                    style={{ width: "100%" }}
                                  />
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
                              <Form.Item
                                key={[section.key, ingredient.key, "amount"]}
                                fieldKey={[
                                  section.fieldKey,
                                  ingredient.fieldKey,
                                  "amount",
                                ]}
                                name={[ingredient.name, "amount"]}>
                                <Input placeholder="Amount" />
                              </Form.Item>
                              <Form.Item
                                key={[section.key, ingredient.key, "unit"]}
                                fieldKey={[
                                  section.fieldKey,
                                  ingredient.fieldKey,
                                  "unit",
                                ]}
                                name={[ingredient.name, "unit"]}>
                                <Input placeholder="Unit" />
                              </Form.Item>
                              <Form.Item
                                valuePropName="checked"
                                key={[section.key, ingredient.key, "optional"]}
                                fieldKey={[
                                  section.fieldKey,
                                  ingredient.fieldKey,
                                  "optional",
                                ]}
                                name={[ingredient.name, "optional"]}>
                                <Checkbox />
                              </Form.Item>
                              {ingredients.length > 1 && (
                                <MinusCircleOutlined
                                  style={{ margin: "0 8px" }}
                                  onClick={() =>
                                    removeIngredient(ingredient.name)
                                  }
                                />
                              )}
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
                              <Form.Item
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
                              <Form.Item
                                key={[section.key, direction.key, "duration"]}
                                fieldKey={[
                                  section.fieldKey,
                                  direction.fieldKey,
                                  "duration",
                                ]}
                                name={[direction.name, "duration"]}>
                                <Input placeholder="Duration" />
                              </Form.Item>
                              <Form.Item
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
                                <Input placeholder="D Type" />
                              </Form.Item>
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
                              {directions.length > 1 && (
                                <MinusCircleOutlined
                                  style={{ margin: "0 8px" }}
                                  onClick={() =>
                                    removeDirection(direction.name)
                                  }
                                />
                              )}
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
                {sections.length > 1 && (
                  <MinusCircleOutlined
                    style={{ margin: "0 8px" }}
                    onClick={() => removeSection(section.name)}
                  />
                )}
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
