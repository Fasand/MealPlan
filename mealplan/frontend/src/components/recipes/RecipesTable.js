import React from "react";
import { Table, Tag, Rate } from "antd";
import { EditOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import { reverse } from "named-urls";
import routes from "../routes";

const RecipeTable = ({ recipes }) => {
  const columns = [
    {
      title: "Title",
      dataIndex: "title",
      key: "title",
      render: (_, record) => (
        <Link to={reverse(routes.recipes.detail.detail, { id: record.id })}>
          {record.title}
        </Link>
      ),
    },
    {
      title: "Description",
      dataIndex: "description",
      key: "description",
    },
    {
      title: "Tags",
      key: "tags",
      dataIndex: "tags",
      render: (tags) => (
        <span>
          {tags.length > 0 &&
            tags.map((tag) => {
              let color = tag.length > 5 ? "geekblue" : "green";
              if (tag === "loser") {
                color = "volcano";
              }
              return (
                <Tag color={color} key={tag}>
                  {tag}
                </Tag>
              );
            })}
        </span>
      ),
    },
    {
      title: "Servings",
      dataIndex: "servings",
      key: "servings",
    },
    {
      title: "Difficulty",
      dataIndex: "difficulty",
      key: "difficulty",
      render: (difficulty) => <Rate disabled defaultValue={difficulty} />,
    },
    {
      title: "Action",
      key: "action",
      render: (_, record) => (
        <Link to={reverse(routes.recipes.detail.edit, { id: record.id })}>
          <EditOutlined />
        </Link>
      ),
    },
  ];
  return (
    <Table
      dataSource={recipes}
      columns={columns}
      rowKey={(record) => record.id}
    />
  );
};

export default RecipeTable;
