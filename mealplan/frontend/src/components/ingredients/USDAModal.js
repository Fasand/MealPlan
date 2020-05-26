import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Select, Button, Modal } from "antd";
import { Fragment } from "react";
import { searchUsda, loadFromUsda } from "../../actions/ingredients";

const USDAModal = ({ ingredient }) => {
  const dispatch = useDispatch();
  const [visible, setVisible] = useState(false);
  const [selected, setSelected] = useState(null);
  const results = useSelector((state) => state.ingredients.searchUsda);

  const handleSearch = (value) => {
    dispatch(searchUsda(value));
  };

  const onOk = () => {
    if (selected && ingredient) {
      setVisible(false);
      dispatch(loadFromUsda(ingredient.id, selected));
    }
  };

  return (
    <Fragment>
      <Button type="default" onClick={() => setVisible(true)}>
        Load data from USDA
      </Button>
      <Modal
        title="Load data from USDA"
        visible={visible}
        onOk={onOk}
        onCancel={() => setVisible(false)}>
        <Select
          showSearch
          style={{ width: "100%" }}
          value={selected}
          onChange={setSelected}
          defaultActiveFirstOption={false}
          showArrow={false}
          filterOption={false}
          onSearch={handleSearch}
          notFoundContent={null}>
          {results.map((r) => (
            <Select.Option key={r.id}>{r.title}</Select.Option>
          ))}
        </Select>
      </Modal>
    </Fragment>
  );
};

export default USDAModal;
