import React, { Fragment, useEffect } from "react";
import { useAlert } from "react-alert";
import { useSelector } from "react-redux";

const Alerts = (_) => {
  const error = useSelector((state) => state.errors);
  const message = useSelector((state) => state.messages);
  const alert = useAlert();

  useEffect(() => {
    if (error.msg.name) alert.error(`Name: ${error.msg.name.join()}`);
    if (error.msg.email) alert.error(`Email: ${error.msg.email.join()}`);
    if (error.msg.message) alert.error(`Message: ${error.msg.message.join()}`);
    if (error.msg.non_field_errors)
      alert.error(error.msg.non_field_errors.join());
    if (error.msg.username) alert.error(error.msg.username.join());
  }, [error]);

  useEffect(() => {
    if (message.passwordNotMatch) alert.error(message.passwordNotMatch);
    if (message.text) alert.success(message.text);
  }, [message]);

  return <Fragment />;
};

export default Alerts;
