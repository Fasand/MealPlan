import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getIngredients } from "../../actions/ingredients";

const Ingredients = (_) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getIngredients());
  }, []);

  const ingredients = useSelector((state) => state.ingredients.ingredients);

  return (
    <div>
      <h1>Ingredients</h1>
    </div>
  );
};

export default Ingredients;
