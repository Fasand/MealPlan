import axios from "axios";
import { returnError } from "../utils/errors";
import { tokenConfig } from "./auth";
import { message } from "antd";
import {
  GET_RECIPES,
  GET_RECIPE,
  CREATE_RECIPE,
  UPDATE_RECIPE,
  DELETE_RECIPE,
} from "./types";

export const getRecipes = () => (dispatch, getState) => {
  axios
    .get("/api/recipes/", tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_RECIPES,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const getRecipe = (id) => (dispatch, getState) => {
  axios
    .get(`/api/recipes/${id}/`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_RECIPE,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const createRecipe = (recipe) => (dispatch, getState) => {
  axios
    .post("/api/recipes/", recipe, tokenConfig(getState))
    .then((res) => {
      message.success("Recipe created");
      dispatch({
        type: CREATE_RECIPE,
        payload: res.data,
      });
    })
    .catch((err) => returnError(err.response.data, err.response.status));
};

export const updateRecipe = (id, recipe) => (dispatch, getState) => {
  if (!id) message.error("ID was not supplied for recipe update");
  else
    axios
      .patch(`/api/recipes/${id}/`, recipe, tokenConfig(getState))
      .then((res) => {
        message.success("Recipe updated");
        dispatch({
          type: UPDATE_RECIPE,
          payload: res.data,
        });
      })
      .catch((err) => returnError(err.response.data, err.response.status));
};
