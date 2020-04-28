import React, { Fragment, useLayoutEffect } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch, Link } from "react-router-dom";

import Dashboard from "./Dashboard";

import Header from "./layout/Header";
import Ingredients from "./ingredients/Ingredients";
import EditIngredient from "./ingredients/EditIngredient";
import Login from "./auth/Login";
import Logout from "./auth/Logout";
import Register from "./auth/Register";
import PrivateRoute from "./common/PrivateRoute";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

import { Layout } from "antd";

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
              <PrivateRoute exact path="/" component={Dashboard} />
              <PrivateRoute exact path="/ingredients" component={Ingredients} />
              <PrivateRoute
                exact
                path="/ingredients/:id/edit"
                component={EditIngredient}
              />
              <Route exact path="/logout" component={Logout} />
              <Route exact path="/register" component={Register} />
              <Route exact path="/login" component={Login} />
            </Switch>
          </Layout.Content>
          <Layout.Footer>MealPlan</Layout.Footer>
        </Layout>
      </Router>
    </Provider>
  );
};

ReactDOM.render(<App />, document.getElementById("app"));
