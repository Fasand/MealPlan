import axios from "axios";
import { returnErrors } from "./messages";
import { tokenConfig } from "./auth";
import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  DELETE_INGREDIENT,
} from "./types";

export const getIngredients = () => (dispatch, getState) => {
  // TODO: dispatch loading
  axios
    .get("/api/ingredients/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_INGREDIENTS,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

export const createIngredient = (ingredient) => (dispatch, getState) => {
  axios
    .post("/api/ingredients/", ingredient, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ text: "Ingredient created" }));
      dispatch({
        type: CREATE_INGREDIENT,
        payload: res.data,
      });
    })
    .catch((err) =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};
