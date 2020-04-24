import React, { useState } from "react";
import { Link, Redirect } from "react-router-dom";
import { login } from "../../actions/auth";
import { useSelector, useDispatch } from "react-redux";
import { Card, Form, Input, Button, Row, Col } from "antd";
import { UserOutlined, LockOutlined } from "@ant-design/icons";

const Login = (_) => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();

  const onFinish = ({ username, password }) => {
    dispatch(login(username, password));
  };

  if (isAuthenticated) return <Redirect to="/" />;
  else
    return (
      <Row justify="center">
        <Col span={10}>
          <Card style={{ marginTop: "3rem" }}>
            <h2 className="text-center">Login</h2>
            <Form onFinish={onFinish}>
              <Form.Item
                name="username"
                rules={[
                  { required: true, message: "Please input your username" },
                ]}>
                <Input
                  prefix={<UserOutlined className="site-form-item-icon" />}
                  placeholder="Username"
                />
              </Form.Item>
              <Form.Item
                name="password"
                rules={[
                  { required: true, message: "Please input your password" },
                ]}>
                <Input.Password
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  placeholder="Password"
                />
              </Form.Item>
              <Form.Item>
                <Button
                  type="primary"
                  htmlType="submit"
                  className="login-form-button">
                  Log in
                </Button>
              </Form.Item>
              <p>
                Don't have an account? <Link to="/register">Register</Link>
              </p>
            </Form>
          </Card>
        </Col>
      </Row>
    );
};

export default Login;
