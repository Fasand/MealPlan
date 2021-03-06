import { include } from "named-urls";

export default {
  root: "/",
  ingredients: include("/ingredients/", {
    list: "",
    detail: include(":id/", {
      edit: "edit/",
    }),
  }),
  recipes: include("/recipes/", {
    list: "",
    detail: include(":id/", {
      detail: "",
      edit: "edit/",
    }),
    planner: "planner/",
  }),
  auth: include("/", {
    logout: "logout/",
    login: "login/",
    register: "register/",
  }),
};
