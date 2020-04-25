import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { Table, Tag } from "antd";
import { EditOutlined } from "@ant-design/icons";

const IngredientsTable = (_) => {
  const dispatch = useDispatch();
  const ingredients = useSelector((state) => state.ingredients.ingredients);
  const categories = useSelector((state) => state.ingredients.categories);

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
      render: (category) => <p>{category || "Uncategorized"}</p>,
    },
    {
      title: "Tags",
      key: "tags",
      dataIndex: "tags",
      render: (tags) => (
        <span>
          {tags.length > 0 &&
            tags.split(",").map((tag) => {
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
        <span>
          <EditOutlined />
        </span>
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