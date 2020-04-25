import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getIngredients } from "../../actions/ingredients";
import CreateForm from "./CreateForm";
import { Row, Col, Collapse } from "antd";
import IngredientsTable from "./IngredientsTable";

const Ingredients = (_) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getIngredients());
  }, []);

  const ingredients = useSelector((state) => state.ingredients.ingredients);

  return (
    <div>
      <h1>Ingredients</h1>
      <Row justify="center">
        <Col span={12}>
          <Collapse>
            <Collapse.Panel header="Create ingredient" key="1">
              <CreateForm />
            </Collapse.Panel>
          </Collapse>
        </Col>
      </Row>
      <IngredientsTable />
    </div>
  );
};

export default Ingredients;
