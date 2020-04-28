import React from "react";
import { useDispatch } from "react-redux";
import { createRecipe, updateRecipe } from "../../actions/recipes";
import { Form, Input, Button, Select, Row, Col } from "antd";
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
                        <div key={[section.key, ingredient.key]}>
                          <Form.Item
                            label="Ingredient title"
                            key={[section.key, ingredient.key, "title"]}
                            fieldKey={[
                              section.fieldKey,
                              ingredient.fieldKey,
                              "title",
                            ]}
                            name={[ingredient.name, "title"]}>
                            <Input />
                          </Form.Item>
                          {ingredients.length > 1 && (
                            <MinusCircleOutlined
                              style={{ margin: "0 8px" }}
                              onClick={() => removeIngredient(ingredient.name)}
                            />
                          )}
                        </div>
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
