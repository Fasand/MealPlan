import React, { Fragment, useLayoutEffect } from "react";
import ReactDOM from "react-dom";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";

import Dashboard from "./Dashboard";

import { Provider as AlertProvider } from "react-alert";
import AlertTemplate from "react-alert-template-basic";

import Header from "./layout/Header";
// import Dashboard from './leads/Dashboard';
import Alerts from "./layout/Alerts";
import Login from "./auth/Login";
import Logout from "./auth/Logout";
// import Register from './accounts/Register';
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
                <Route exact path="/logout" component={Logout} />
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
