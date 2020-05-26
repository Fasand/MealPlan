import React from "react";
import { useDispatch } from "react-redux";
import { createIngredient, updateIngredient } from "../../actions/ingredients";
import { Row, Col, Form, Input, Button, Select } from "antd";

const IngredientForm = ({ ingredient, categories }) => {
  const dispatch = useDispatch();

  const formLayout = {
    labelCol: { span: 6 },
    wrapperCol: { span: 18 },
  };
  const formTailLayout = {
    wrapperCol: { offset: 6, span: 18 },
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
    } else {
      dispatch(createIngredient(values));
    }
  };

  // TODO: tags should be loaded from previously created ingredients

  const initialValues = ingredient
    ? {
        ...ingredient,
        // Category must be a string to be auto-selected
        category: ingredient.category && String(ingredient.category),
      }
    : {};

  const [form] = Form.useForm();

  return (
    <Form
      form={form}
      onFinish={onFinish}
      {...formLayout}
      initialValues={initialValues}>
      <Row>
        <Col span={12}>
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
                <Select.Option key={category.id}>
                  {category.title}
                </Select.Option>
              ))}
            </Select>
          </Form.Item>
          <Form.Item label="Tags" name="tags">
            <Select mode="tags" tokenSeparators={[","]}></Select>
          </Form.Item>
          <Form.Item label="Density" name="density">
            <Input addonAfter={densityAddon} />
          </Form.Item>
        </Col>
        <Col span={12}>
          <Form.Item {...formTailLayout}>
            <h4>Nutrition per 100g</h4>
          </Form.Item>
          <Form.Item label="Protein" name={["nutrition", "protein"]}>
            <Input type="number" />
          </Form.Item>
          <Form.Item label="Fat" name={["nutrition", "total_lipid_fat"]}>
            <Input type="number" />
          </Form.Item>
          <Form.Item
            label="Carbohydrates"
            name={["nutrition", "carbohydrate_by_difference"]}>
            <Input type="number" />
          </Form.Item>
          <Form.Item label="Sugar" name={["nutrition", "sugars_total_nlea"]}>
            <Input type="number" />
          </Form.Item>
          <Form.Item label="Energy" name={["nutrition", "energy"]}>
            <Input type="number" />
          </Form.Item>
          <Form.Item wrapperCol={{ span: 24 }} style={{ textAlign: "right" }}>
            <Button type="ghost" onClick={() => form.resetFields()}>
              Clear
            </Button>
            <Button
              type="primary"
              htmlType="submit"
              style={{ marginLeft: "1rem" }}>
              {ingredient ? "Update" : "Create"}
            </Button>
          </Form.Item>
        </Col>
      </Row>
    </Form>
  );
};

export default IngredientForm;
