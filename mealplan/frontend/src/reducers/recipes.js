import {
  GET_RECIPES,
  GET_RECIPE,
  CREATE_RECIPE,
  UPDATE_RECIPE,
  DELETE_RECIPE,
} from "../actions/types";

const initialState = {
  recipes: [],
  recipe: null,
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_RECIPES:
      return {
        ...state,
        recipes: action.payload,
      };
    case GET_RECIPE:
      return {
        ...state,
        recipe: action.payload,
      };
    case CREATE_RECIPE:
      return {
        ...state,
        recipes: [...state.recipes, action.payload],
      };
    case UPDATE_RECIPE:
      return {
        ...state,
        // TODO: find the updated recipe and change in recipes
        recipe: action.payload,
      };
    case GET_RECIPE_CATEGORIES:
      return {
        ...state,
        categories: action.payload,
      };
    default:
      return state;
  }
}
