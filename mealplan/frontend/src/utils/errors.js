import { message } from "antd";

export const returnError = (error, status) => {
  console.log(error, status);
  if (error.non_field_errors) message.error(error.non_field_errors.join());
  else {
    for (const key of Object.keys(error)) {
      const capitalized = key.charAt(0).toUpperCase() + key.slice(1);
      message.error(`${capitalized}: ${error[key]}`);
    }
  }
};
