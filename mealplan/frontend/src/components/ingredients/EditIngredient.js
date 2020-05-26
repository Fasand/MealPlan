import React, { useEffect } from "react";
import IngredientForm from "./IngredientForm";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
  getIngredient,
  getIngredientCategories,
} from "../../actions/ingredients";
import Loading from "../common/Loading";
import { Row, Col, Card } from "antd";

const EditIngredient = (_) => {
  const { id } = useParams();
  const ingredient = useSelector((state) => state.ingredients.ingredient);
  const categories = useSelector((state) => state.ingredients.categories);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getIngredientCategories());
  }, []);
  useEffect(() => {
    dispatch(getIngredient(id));
  }, [id]);

  return (
    <Loading until={ingredient}>
      <Row style={{ marginTop: "2rem" }}>
        <Col span={22} offset={1}>
          <Card>
            <IngredientForm {...{ ingredient, categories }} />
          </Card>
        </Col>
      </Row>
    </Loading>
  );
};

export default EditIngredient;
