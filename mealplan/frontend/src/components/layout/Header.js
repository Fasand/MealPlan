import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
import { Menu } from "antd";

const Header = (_) => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const user = useSelector((state) => state.auth.user);

  const authMenu = (
    <Menu theme="dark" mode="horizontal">
      <Menu.Item key="ingredients">
        <Link to="/ingredients">Ingredients</Link>
      </Menu.Item>
      <Menu.Item disabled>
        <strong>{user ? `Welcome ${user.username}` : ""}</strong>
      </Menu.Item>
      <Menu.Item key="logout">
        <Link to="/logout">Logout</Link>
      </Menu.Item>
    </Menu>
  );

  const guestMenu = (
    <Menu theme="dark" mode="horizontal">
      <Menu.Item key="register">
        <Link to="/register">Register</Link>
      </Menu.Item>
      <Menu.Item key="login">
        <Link to="/login">Login</Link>
      </Menu.Item>
    </Menu>
  );

  return (
    <Fragment>
      <div className="logo" />
      {isAuthenticated ? authMenu : guestMenu}
    </Fragment>
  );
};

export default Header;
