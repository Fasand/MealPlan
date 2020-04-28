import React from "react";
import { useDispatch } from "react-redux";
import { createRecipe, updateRecipe } from "../../actions/recipes";
import { Form, Input, Button, Select } from "antd";

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
      <Form.Item {...formTailLayout}>
        <Button type="primary" htmlType="submit">
          {ingredient ? "Update" : "Create"}
        </Button>
      </Form.Item>
    </Form>
  );
};

export default RecipeForm;
