import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  getIngredientCategories,
  createIngredient,
} from "../../actions/ingredients";
import { Form, Input, Button, Select } from "antd";

const IngredientForm = ({ ingredient } = { ingredient: null }) => {
  const dispatch = useDispatch();
  const categories = useSelector((state) => state.ingredients.categories);
  useEffect(() => {
    dispatch(getIngredientCategories());
    console.log(ingredient);
  }, []);

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
      values.tags = values.tags
        .split(",")
        .map((tag) => tag.trim())
        .join(",");
    // Update or create
    if (ingredient) {
      // TODO dispatch(updateIngredient(id, values))
    } else dispatch(createIngredient(values));
  };

  // TODO: tags should be loaded from previously created ingredients

  return (
    <Form onFinish={onFinish} {...formLayout} initialValues={ingredient}>
      <Form.Item label="Title" name="title">
        <Input />
      </Form.Item>
      <Form.Item label="Description" name="description">
        <Input.TextArea />
      </Form.Item>
      <Form.Item label="Category" name="category">
        <Select showSearch>
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
          Create
        </Button>
      </Form.Item>
    </Form>
  );
};

export default IngredientForm;
