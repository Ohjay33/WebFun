// starting a new project "npx create-react-app-"folder name"
// run react "npm start"

// basic functional component setup
import React from "react";

const form = ()=>{}

export default form;

// in the folder you want to open in visualstudio 
cmd code .

// use the command prompt to start projects
cd "my-app-name"
npm start

npm init

npm i <package name>

//insert in app.js
npm install react-bootstrap bootstrap
import "bootstrap/dist/css/bootstrap.min.css"; //insert in app.js

import Button from 'react-bootstrap/Button';
// or less ideally
import { Button } from 'react-bootstrap';


// ------> In App.js <--------//

import React from "react";
import {
  Routes,
  Route,
  Link
} from "react-router-dom";

const Home = (props) => {
  return (
    <div>
      <h1 style={{ color: "red" }}>Home Component</h1>
      <Link to={"/about"}>Go to About </Link>
    </div>
  );
}

const About = (props) => {
  return (
    <div>
      <h1 style={{ color: "blue" }}>About Component</h1>
      <Link to={"/"}>Go Home</Link>
    </div>
  );
}

function App() {
  return (
    <div>
      <h1>Routing Example</h1>
      <Routes>
        <Route path="/about" element={<About />} />
        <Route exact path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App


// // ----------> URL Params <-----------// //

import React from "react";
import { useParams } from "react-router";
import {
  Link,
  Routes,
  Route
} from "react-router-dom";

const Location = (props) => {
  const {city} = useParams();
  return (
    <h1>Welcome to {city}! </h1>
  );
}

function App() {
  return (
    <div>
      <p>
        <Link to="/location/seattle">Seattle</Link>
        |
        <Link to="/location/chicago">Chicago</Link>
        |
        <Link to="/location/burbank">Burbank</Link>
      </p>
      <Routes>
        <Route path="/location/:city" element={<Location />} />
      </Routes>
    </div>
  );
}

export default App;


// -------> using "useNavigate" <--------//

import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function App() {

  const Survey = (props) => {
    const [name, setName] = useState("");
    const [comment, setComment] = useState("");
    const navigate = useNavigate();

    const sendSurvey = (e) => {
      e.preventDefault();
      // When the user clicks the submit input in the form, 
      //we will navigate to the "/results" path
      navigate("/results");
    }

    return (
      <form onSubmit={sendSurvey}>
        <label>Your Name:</label>
        <input type="text" onChange={(e) => setName(e.target.value)} value={name} />
        <label>Your Comment:</label>
        <textarea onChange={(e) => setComment(e.target.value)} value={comment}></textarea>
        <input type="submit" value="Submit Survey" />
      </form>
    );
  }
}




