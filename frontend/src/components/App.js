import React from "react";
import ReactDOM from "react-dom";
/*
import '../../static/frontend/homepage.css';
*/
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";

const App = () => (
  <React.Fragment>
    <div>
      <h1>Hello, world!</h1>
      <DataProvider endpoint="api/lead/"
                    render={data => <Table data={data} />} />
      <Form endpoint="api/lead/" />
    </div>
  </React.Fragment>
);

/*
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
*/
ReactDOM.render(<App />, document.getElementById('app'));
