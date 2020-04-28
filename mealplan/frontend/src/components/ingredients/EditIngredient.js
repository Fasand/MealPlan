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

  if (ingredient) return <IngredientForm ingredient={ingredient} />;
  else return <Loading />;
};

export default EditIngredient;
