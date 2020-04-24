import React, { useState } from "react";
import { Link, Redirect } from "react-router-dom";
import { register } from "../../actions/auth";
import { createMessage } from "../../actions/messages";
import { useSelector, useDispatch } from "react-redux";
import { Card, Form, Input, Button, Row, Col } from "antd";
import { UserOutlined, LockOutlined } from "@ant-design/icons";

const Register = (props) => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const dispatch = useDispatch();

  const onFinish = ({ username, email, password, password2 }) => {
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
      <Row justify="center">
        <Col span={10}>
          <Card style={{ marginTop: "3rem" }}>
            <h2 className="text-center">Register</h2>
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
                name="email"
                rules={[
                  { required: true, message: "Please input your email" },
                  { type: "email" },
                ]}>
                <Input
                  prefix={<UserOutlined className="site-form-item-icon" />}
                  placeholder="Email"
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
              <Form.Item
                name="password2"
                dependencies={["password"]}
                rules={[
                  {
                    required: true,
                    message: "Please input your password again",
                  },
                  ({ getFieldValue }) => ({
                    validator(_, value) {
                      if (!value || getFieldValue("password") === value) {
                        return Promise.resolve();
                      }
                      return Promise.reject(
                        "The two passwords that you entered do not match!"
                      );
                    },
                  }),
                ]}>
                <Input.Password
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  placeholder="Password again"
                />
              </Form.Item>
              <Form.Item>
                <Button
                  type="primary"
                  htmlType="submit"
                  className="login-form-button">
                  Register
                </Button>
              </Form.Item>
              <p>
                Already have an account? <Link to="/login">Login</Link>
              </p>
            </Form>
          </Card>
        </Col>
      </Row>
    );
};

export default Register;
