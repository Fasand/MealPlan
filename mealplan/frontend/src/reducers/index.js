import { combineReducers } from "redux";
import auth from "./auth";
import errors from "./errors";
import ingredients from "./ingredients";

export default combineReducers({
  auth,
  errors,
  ingredients,
});
