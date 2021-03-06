import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getRecipes } from "../../actions/recipes";
import RecipeForm from "./RecipeForm";
import { Row, Col, Collapse } from "antd";
import RecipesTable from "./RecipesTable";
import { Link } from "react-router-dom";
import { reverse } from "named-urls";
import routes from "../routes";

const Recipes = (_) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getRecipes());
  }, []);

  const recipes = useSelector((state) => state.recipes.recipes);

  return (
    <div>
      <h1>Recipes</h1>
      <Link to={reverse(routes.recipes.planner)}>Recipe Planner</Link>
      <Row justify="center">
        <Col span={24}>
          <Collapse defaultActiveKey={1}>
            <Collapse.Panel header="Create recipe" key="1">
              <RecipeForm />
            </Collapse.Panel>
          </Collapse>
        </Col>
      </Row>
      <RecipesTable recipes={recipes} />
    </div>
  );
};

export default Recipes;
