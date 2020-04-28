import React, { useEffect } from "react";
import IngredientForm from "./IngredientForm";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getIngredient } from "../../actions/ingredients";
import Loading from "../common/Loading";
import { Row, Col, Card } from "antd";

const EditIngredient = (_) => {
  const { id } = useParams();
  const ingredient = useSelector((state) => state.ingredients.ingredient);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getIngredient(id));
  }, []);

  return (
    <Loading until={ingredient}>
      <Row style={{ marginTop: "2rem" }}>
        <Col span={16} offset={4}>
          <Card>
            <IngredientForm ingredient={ingredient} />
          </Card>
        </Col>
      </Row>
    </Loading>
  );
};

export default EditIngredient;
