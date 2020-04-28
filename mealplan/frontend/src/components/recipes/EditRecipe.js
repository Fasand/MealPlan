import React, { useEffect } from "react";
import RecipeForm from "./RecipeForm";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getRecipe } from "../../actions/recipes";
import Loading from "../common/Loading";
import { Row, Col, Card } from "antd";

const EditRecipe = (_) => {
  const { id } = useParams();
  const recipe = useSelector((state) => state.recipes.recipe);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRecipe(id));
  }, []);

  return (
    <Loading until={recipe}>
      <Row style={{ marginTop: "2rem" }}>
        <Col span={16} offset={4}>
          <Card>
            <RecipeForm {...{ recipe }} />
          </Card>
        </Col>
      </Row>
    </Loading>
  );
};

export default EditRecipe;
