import React, { useEffect } from "react";
import IngredientForm from "./IngredientForm";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getIngredient } from "../../actions/ingredients";
import Loading from "../common/Loading";

const EditIngredient = (_) => {
  const { id } = useParams();
  const ingredient = useSelector((state) => state.ingredients.ingredient);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getIngredient(id));
  }, []);

  return (
    <Loading until={ingredient}>
      <IngredientForm ingredient={ingredient} />
    </Loading>
  );
};

export default EditIngredient;
