import { message } from "antd";

export const returnError = (error, status) => {
  if (error.name) message.error(`Name: ${error.name.join()}`);
  if (error.email) message.error(`Email: ${error.email.join()}`);
  if (error.message) message.error(`Message: ${error.message.join()}`);
  if (error.non_field_errors) message.error(error.non_field_errors.join());
  if (error.username) message.error(error.username.join());
  console.log(error, status);
};
