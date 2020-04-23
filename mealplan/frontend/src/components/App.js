import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import { HashRouter as Router, Route, Switch, Redirect } from 'react-router-dom';

// import { Provider as AlertProvider } from 'react-alert';
// import AlertTemplate from 'react-alert-template-basic';

// import Header from './layout/Header';
// import Dashboard from './leads/Dashboard';
// import Alerts from './layout/Alerts';
// import Login from './accounts/Login';
// import Register from './accounts/Register';
// import PrivateRoute from './common/PrivateRoute';

import { Provider } from "react-redux";
import store from "../store";
// import { loadUser } from '../actions/auth';

// Alert Options
// const alertOptions = {
//   timeout: 3000,
//   position: 'top center',
// };

const App = (props) => {
  return (
    <Provider store={store}>
      <Router>
        <Fragment>
          <div className="container">
            <h1>Hello from React</h1>
            <Switch>
              {/* <Route exact path="/register" component={Register} /> */}
              {/* <Route exact path="/login" component={Login} /> */}
            </Switch>
          </div>
        </Fragment>
      </Router>
    </Provider>
  );
};

// TODO: need  to load user with hooks somehow
// class App extends Component {
//   componentDidMount() {
//     store.dispatch(loadUser());
//   }
// }

ReactDOM.render(<App />, document.getElementById("app"));
