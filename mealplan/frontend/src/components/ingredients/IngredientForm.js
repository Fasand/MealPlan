import React from "react";
import { useDispatch } from "react-redux";
import { createIngredient, updateIngredient } from "../../actions/ingredients";
import { Form, Input, Button, Select } from "antd";

const IngredientForm = ({ ingredient, categories }) => {
  const dispatch = useDispatch();

  const formLayout = {
    labelCol: { span: 8 },
    wrapperCol: { span: 16 },
  };
  const formTailLayout = {
    wrapperCol: { offset: 8, span: 16 },
  };
  const densityAddon = (
    <span>
      kg/m<sup>3</sup>
    </span>
  );

  const onFinish = (values) => {
    // Strip tags of whitespace
    if (values.tags)
      values.tags = values.tags.map((tag) => tag.trim()).join(",");
    // Category is nullable but undefined doesn't do anything
    if (values.category === undefined) values.category = null;
    // Update or create
    if (ingredient) {
      dispatch(updateIngredient(ingredient.id, values));
    } else dispatch(createIngredient(values));
  };

  // TODO: tags should be loaded from previously created ingredients

  const initialValues = ingredient
    ? {
        ...ingredient,
        // Category must be a string to be auto-selected
        category: ingredient.category && String(ingredient.category),
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
      <Form.Item label="Category" name="category">
        <Select
          showSearch
          allowClear
          filterOption={(input, option) =>
            option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
          }>
          {categories.map((category) => (
            <Select.Option key={category.id}>{category.title}</Select.Option>
          ))}
        </Select>
      </Form.Item>
      <Form.Item label="Tags" name="tags">
        <Select mode="tags" tokenSeparators={[","]}></Select>
      </Form.Item>
      <Form.Item label="Density" name="density">
        <Input addonAfter={densityAddon} />
      </Form.Item>
      <Form.Item {...formTailLayout}>
        <Button type="primary" htmlType="submit">
          {ingredient ? "Update" : "Create"}
        </Button>
      </Form.Item>
    </Form>
  );
};

export default IngredientForm;
