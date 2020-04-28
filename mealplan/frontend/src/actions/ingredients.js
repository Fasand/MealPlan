import axios from "axios";
import { returnError } from "../utils/errors";
import { tokenConfig } from "./auth";
import { message } from "antd";
import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  DELETE_INGREDIENT,
  GET_INGREDIENT_CATEGORIES,
} from "./types";

export const getIngredients = () => (dispatch, getState) => {
  axios
    .get("/api/ingredients/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_INGREDIENTS,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const getIngredient = (id) => (dispatch, getState) => {
  axios
    .get(`/api/ingredients/${id}`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_INGREDIENT,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const createIngredient = (ingredient) => (dispatch, getState) => {
  axios
    .post("/api/ingredients/", ingredient, tokenConfig(getState))
    .then((res) => {
      message.success("Ingredient created");
      dispatch({
        type: CREATE_INGREDIENT,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const getIngredientCategories = () => (dispatch, getState) => {
  axios
    .get("/api/ingredient-categories/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_INGREDIENT_CATEGORIES,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};
