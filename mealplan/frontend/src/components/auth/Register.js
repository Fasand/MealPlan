import React, { useState } from "react";
import { Link, Redirect } from "react-router-dom";
import { register } from "../../actions/auth";
import { createMessage } from "../../actions/messages";
import { useSelector, useDispatch } from "react-redux";

const Register = (props) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [password2, setPassword2] = useState("");

  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();

  const onSubmit = (e) => {
    e.preventDefault();
    if (password !== password2) {
      dispatch(createMessage({ passwordNotMatch: "Passwords do not match" }));
    } else {
      const newUser = {
        username,
        password,
        email,
      };
      dispatch(register(newUser));
    }
  };

  if (isAuthenticated) return <Redirect to="/" />;
  else
    return (
      <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Register</h2>
          <form onSubmit={onSubmit}>
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input
                type="text"
                className="form-control"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                className="form-control"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password2">Password again</label>
              <input
                type="password"
                className="form-control"
                id="password2"
                value={password2}
                onChange={(e) => setPassword2(e.target.value)}
              />
            </div>
            <button type="submit" className="btn btn-primary">
              Register
            </button>
            <p className="pt-2">
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </form>
        </div>
      </div>
    );
};

export default Register;
