import axios from "axios";
import { returnError } from "../utils/errors";
import { tokenConfig } from "./auth";
import { message } from "antd";
import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  UPDATE_INGREDIENT,
  DELETE_INGREDIENT,
  GET_INGREDIENT_UNITS,
  GET_INGREDIENT_CATEGORIES,
  SEARCH_USDA,
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
  // Reset before loading
  dispatch({
    type: GET_INGREDIENT,
    payload: null,
  });
  axios
    .get(`/api/ingredients/${id}/`, tokenConfig(getState))
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

export const updateIngredient = (id, ingredient) => (dispatch, getState) => {
  if (!id) message.error("ID was not supplied for ingredient update");
  else
    axios
      .patch(`/api/ingredients/${id}/`, ingredient, tokenConfig(getState))
      .then((res) => {
        message.success("Ingredient updated");
        dispatch({
          type: UPDATE_INGREDIENT,
          payload: res.data,
        });
      })
      .catch((err) => returnError(err.response.data, err.response.status));
};

export const getIngredientUnits = () => (dispatch, getState) => {
  // TODO: add units for specific ingredients
  axios
    .get("/api/ingredient-units/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_INGREDIENT_UNITS,
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

export const searchUsda = (query) => (dispatch, getState) => {
  axios
    .get(`/api/ingredients/usda/?q=${query}`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: SEARCH_USDA,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const loadFromUsda = (ingredient, usdaIngredient) => (
  dispatch,
  getState
) => {
  const data = { ingredient, usdaIngredient };
  // Reset before loading
  dispatch({
    type: GET_INGREDIENT,
    payload: null,
  });
  axios
    .post(`/api/ingredients/usda/`, data, tokenConfig(getState))
    .then((res) => {
      message.success("Ingredient loaded from USDA");
      dispatch({
        type: GET_INGREDIENT,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};
