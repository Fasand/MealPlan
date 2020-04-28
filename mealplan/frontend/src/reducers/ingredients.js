import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  DELETE_INGREDIENT,
  GET_INGREDIENT_CATEGORIES,
} from "../actions/types";

const initialState = {
  ingredients: [],
  ingredient: null,
  categories: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_INGREDIENTS:
      return {
        ...state,
        ingredients: action.payload,
      };
    case GET_INGREDIENT:
      return {
        ...state,
        ingredient: action.payload,
      };
    case CREATE_INGREDIENT:
      return {
        ...state,
        ingredients: [...state.ingredients, action.payload],
      };
    case GET_INGREDIENT_CATEGORIES:
      return {
        ...state,
        categories: action.payload,
      };
    default:
      return state;
  }
}
