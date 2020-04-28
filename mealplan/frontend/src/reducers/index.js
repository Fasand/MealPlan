import { combineReducers } from "redux";
import auth from "./auth";
import errors from "./errors";
import ingredients from "./ingredients";
import recipes from "./recipes";

export default combineReducers({
  auth,
  errors,
  ingredients,
  recipes,
});
