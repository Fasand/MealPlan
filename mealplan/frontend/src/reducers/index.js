import { combineReducers } from "redux";
import auth from "./auth";
import errors from "./errors";
import ingredients from "./ingredients";
import messages from "./messages";

export default combineReducers({
  auth,
  errors,
  ingredients,
  messages,
});
