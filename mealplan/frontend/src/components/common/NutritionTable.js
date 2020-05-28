import React, { Fragment } from "react";
import { Table } from "antd";

const NutritionTable = ({
  nutrition,
  numServings = null,
  toFixed = 1,
  ...props
}) => {
  const fields = [
    ["Protein", "protein", "g"],
    ["Fat", "total_lipid_fat", "g"],
    ["Carbohydrates", "carbohydrate_by_difference", "g"],
    ["Sugar", "sugars_total_including_nlea", "g"],
    ["Energy", "energy", "kcal"],
  ];

  const dataSource = nutrition
    ? fields.map(([label, field, unit]) => ({
        total: nutrition[field] ? nutrition[field].toFixed(toFixed) : null,
        serving:
          numServings && nutrition[field]
            ? (nutrition[field] / numServings).toFixed(toFixed)
            : null,
        field,
        label,
        unit,
      }))
    : [];

  const { Column } = Table;

  return (
    <Table
      dataSource={dataSource}
      rowKey="field"
      title={() => <h4>Nutrition</h4>}
      pagination={false}
      size="middle"
      bordered
      loading={!nutrition}
      {...props}>
      <Column dataIndex="label" key="label" />
      {numServings && (
        <Fragment>
          <Column
            title="Serving"
            dataIndex="serving"
            key="serving"
            align="right"
          />
          <Column dataIndex="unit" key="unit_serving" width="3rem" />
        </Fragment>
      )}
      <Column title="Total" dataIndex="total" key="total" align="right" />
      <Column dataIndex="unit" key="unit_total" width="3rem" />
    </Table>
  );
};

export default NutritionTable;
