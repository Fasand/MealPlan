import React from "react";
import { Table } from "antd";

const NutritionDisplay = ({ nutrition, toFixed = 1, ...props }) => {
  const fields = [
    ["Protein", "protein", "g"],
    ["Fat", "total_lipid_fat", "g"],
    ["Carbohydrates", "carbohydrate_by_difference", "g"],
    ["Sugar", "sugars_total_including_nlea", "g"],
    ["Energy", "energy", "kcal"],
  ];

  const dataSource = nutrition
    ? fields.map(([label, field, unit]) => ({
        value: nutrition[field].toFixed(toFixed),
        field,
        label,
        unit,
      }))
    : [];

  const columns = [
    { title: null, dataIndex: "label", key: "label" },
    { title: null, dataIndex: "value", key: "value", align: "right" },
    { title: null, dataIndex: "unit", key: "unit" },
  ];
  return (
    <Table
      dataSource={dataSource}
      columns={columns}
      rowKey="field"
      title={() => <h4>Nutrition</h4>}
      showHeader={false}
      pagination={false}
      size="middle"
      bordered
      loading={!nutrition}
      {...props}
    />
  );
};

export default NutritionDisplay;
