import React from "react";
import { Table, Tag } from "antd";
import { EditOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";
import { reverse } from "named-urls";
import routes from "../routes";

const IngredientsTable = ({ ingredients, categories }) => {
  const columns = [
    {
      title: "Title",
      dataIndex: "title",
      key: "title",
    },
    {
      title: "Description",
      dataIndex: "description",
      key: "description",
    },
    {
      title: "Category",
      dataIndex: "category",
      key: "category",
      render: (category) => (
        <p>
          {category
            ? categories.find((c) => c.id == category).title
            : "Uncategorized"}
        </p>
      ),
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
      title: "Action",
      key: "action",
      render: (text, record) => (
        <Link to={reverse(routes.ingredients.detail.edit, { id: record.id })}>
          <EditOutlined />
        </Link>
      ),
    },
  ];
  return (
    <Table
      dataSource={ingredients}
      columns={columns}
      rowKey={(record) => record.id}
    />
  );
};

export default IngredientsTable;
