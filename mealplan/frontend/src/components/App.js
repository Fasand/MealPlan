import React, { Fragment, useEffect } from "react";
import ReactDOM from "react-dom";
import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";

import Dashboard from "./Dashboard";

// import { Provider as AlertProvider } from 'react-alert';
// import AlertTemplate from 'react-alert-template-basic';

import Header from "./layout/Header";
// import Dashboard from './leads/Dashboard';
// import Alerts from './layout/Alerts';
import Login from "./auth/Login";
// import Register from './accounts/Register';
import PrivateRoute from "./common/PrivateRoute";

import { Provider } from "react-redux";
import store from "../store";
import { loadUser } from "../actions/auth";

// Alert Options
// const alertOptions = {
//   timeout: 3000,
//   position: 'top center',
// };

export const App = (props) => {
  // Load the user on component mount
  useEffect(() => {
    store.dispatch(loadUser());
  }, []);

  return (
    <Provider store={store}>
      <Router>
        <Fragment>
          <Header />
          <div className="container">
            <h1>Hello from React</h1>
            <Switch>
              <PrivateRoute exact path="/" component={Dashboard} />
              <Route exact path="/login" component={Login} />
            </Switch>
          </div>
        </Fragment>
      </Router>
    </Provider>
  );
};

ReactDOM.render(<App />, document.getElementById("app"));
