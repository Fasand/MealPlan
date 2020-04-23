import React, { Fragment, useLayoutEffect } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import Dashboard from "./Dashboard";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import Header from "./layout/Header";
import Ingredients from "./ingredients/Ingredients";
import Alerts from "./layout/Alerts";
import Login from "./auth/Login";
import Logout from "./auth/Logout";
import Register from "./auth/Register";
import PrivateRoute from "./common/PrivateRoute";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

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
      <AlertProvider template={AlertTemplate} {...alertOptions}>
        <Router>
          <Fragment>
            <Header />
            <Alerts />
            <div className="container">
              <Switch>
                <PrivateRoute exact path="/" component={Dashboard} />
                <PrivateRoute
                  exact
                  path="/ingredients"
                  component={Ingredients}
                />
                <Route exact path="/logout" component={Logout} />
                <Route exact path="/register" component={Register} />
                <Route exact path="/login" component={Login} />
              </Switch>
            </div>
          </Fragment>
        </Router>
      </AlertProvider>
    </Provider>
  );
};

ReactDOM.render(<App />, document.getElementById("app"));
