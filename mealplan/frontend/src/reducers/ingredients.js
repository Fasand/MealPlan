import {
  GET_INGREDIENTS,
  GET_INGREDIENT,
  CREATE_INGREDIENT,
  UPDATE_INGREDIENT,
  DELETE_INGREDIENT,
  GET_INGREDIENT_UNITS,
  GET_INGREDIENT_CATEGORIES,
  SEARCH_USDA,
} from "../actions/types";

const initialState = {
  ingredients: [],
  ingredient: null,
  ingredientSearch: [],
  categories: [],
  units: [],
  searchUsda: [],
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
    case UPDATE_INGREDIENT:
      return {
        ...state,
        // TODO: find the updated ingredient and change in ingredients
        ingredient: action.payload,
      };
    case GET_INGREDIENT_UNITS:
      return {
        ...state,
        units: action.payload,
      };
    case GET_INGREDIENT_CATEGORIES:
      return {
        ...state,
        categories: action.payload,
      };
    case SEARCH_USDA:
      return {
        ...state,
        searchUsda: action.payload,
      };
    default:
      return state;
  }
}
