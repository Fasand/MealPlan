import React, { useEffect } from "react";
import { LoadingOutlined } from "@ant-design/icons";
import { Spin } from "antd";

const Loading = ({ until, delay = 0, size = "default", children } = {}) => {
  const indicator = <LoadingOutlined />;

  if (children) {
    return (
      <Spin spinning={!until} delay={delay} size={size} indicator={indicator}>
        {until ? children : <div style={{ padding: "2rem" }}></div>}
      </Spin>
    );
  } else
    return (
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100vw",
          height: "100vh",
          backgroundColor: "rgba(255,255,255,0.3)",
        }}>
        <Spin
          indicator={indicator}
          size="large"
          style={{ display: "block", margin: "30% auto" }}
        />
      </div>
    );
};

export default Loading;
