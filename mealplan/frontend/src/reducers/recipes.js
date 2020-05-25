import {
  GET_RECIPES,
  GET_RECIPE,
  GET_DURATION_TYPES,
  CREATE_RECIPE,
  UPDATE_RECIPE,
  DELETE_RECIPE,
} from "../actions/types";

const initialState = {
  recipes: [],
  recipe: null,
  duration_types: [],
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
    case GET_DURATION_TYPES:
      return {
        ...state,
        duration_types: action.payload,
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
    default:
      return state;
  }
}
