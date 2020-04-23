import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  DELETE_INGREDIENT,
} from "../actions/types";

const initialState = {
  ingredients: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_INGREDIENTS:
      return {
        ...state,
        ingredients: action.payload,
      };
    default:
      return state;
  }
}
