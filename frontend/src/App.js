import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import { AuthProvider } from './AuthContext';

import './App.css';
import RegistrationPage from './pages/RegistrationPage';
import DescriptionPage from './pages/DescriptionPage';

function App() {

  const [authDetails, setAuthDetails] = React.useState(
    localStorage.getItem('token')
  );

  function setAuth(token, u_id){
    localStorage.setItem('token', token);
    localStorage.setItem('u_id', u_id);
    setAuthDetails(token);
  }

  return (
    <AuthProvider value={authDetails}>
      <Router>
        <Switch>
          <Route
            exact
            path="/login"
            render={(props)=>{
              return <LoginPage {...props} setAuth={setAuth}/>
            }}
          />
          <Route
            exact
            path="/register"
            render={(props)=>{
              return <RegistrationPage {...props} setAuth={setAuth}/>
            }}
          ></Route>
          <Route
            exact
            path="/moreInfo"
            render={(props)=>{
              return <DescriptionPage {...props}/>
            }}
          ></Route>
        </Switch>
      </Router>
    </AuthProvider>

  );
}

export default App;
