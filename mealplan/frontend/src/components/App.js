import React, { Fragment, useLayoutEffect } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch, Link } from "react-router-dom";

import Dashboard from "./Dashboard";

import Header from "./layout/Header";
import Ingredients from "./ingredients/Ingredients";
import EditIngredient from "./ingredients/EditIngredient";
import Recipes from "./recipes/Recipes";
import EditRecipe from "./recipes/EditRecipe";
import Login from "./auth/Login";
import Logout from "./auth/Logout";
import Register from "./auth/Register";
import PrivateRoute from "./common/PrivateRoute";
import routes from "./routes";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

import { Layout } from "antd";
import RecipeDetail from "./recipes/RecipeDetail";

// Alert Options
const alertOptions = {
  timeout: 3000,
  position: "top center",
};

export const App = (props) => {
  // Load the user on component mount
  useLayoutEffect(() => {
    store.dispatch(loadUser());
  }, []);

  return (
    <Provider store={store}>
      <Router>
        <Layout style={{ minHeight: "100vh" }}>
          <Layout.Header>
            <Header />
          </Layout.Header>
          <Layout.Content>
            <Switch>
              <PrivateRoute exact path={routes.root} component={Dashboard} />
              <PrivateRoute
                exact
                path={routes.ingredients.list}
                component={Ingredients}
              />
              <PrivateRoute
                exact
                path={routes.ingredients.detail.edit}
                component={EditIngredient}
              />
              <PrivateRoute
                exact
                path={routes.recipes.list}
                component={Recipes}
              />
              <PrivateRoute
                exact
                path={routes.recipes.detail.edit}
                component={EditRecipe}
              />
              <PrivateRoute
                exact
                path={routes.recipes.detail.detail}
                component={RecipeDetail}
              />
              <Route exact path={routes.auth.logout} component={Logout} />
              <Route exact path={routes.auth.register} component={Register} />
              <Route exact path={routes.auth.login} component={Login} />
            </Switch>
          </Layout.Content>
          <Layout.Footer>MealPlan</Layout.Footer>
        </Layout>
      </Router>
    </Provider>
  );
};

ReactDOM.render(<App />, document.getElementById("app"));
