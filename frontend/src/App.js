import React from "react"
import { Redirect, Route } from "react-router-dom"
import { Home, User, Counter } from 'templates'
import { Login, SignUp, UserDetail, UserEdit, UserList } from 'user'
import { TodoReducer} from './store'
import { Schedule } from './todos/containers'
import { Navi } from 'common'
import { BrowserRouter as Router } from "react-router-dom"
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
const rootReducer = combineReducers({TodoReducer})

const App = () => {
return(<div>
    <Router>
      <Provider store = {createStore(rootReducer)}>
        <Navi/>
        <Route exact path='/home' component={Home}/>
        <Redirect exact from={'/'} to={'/home'}/>
        <Route exact path='/counter' component={Counter}/>
        
        <Route exact path='/schedule' component={Schedule}/>

        <Route exact path='/user' component={User}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/signup-form' component={SignUp}/>
        <Route exact path='/user-detail' component={UserDetail}/>
        <Route exact path='/user-modify' component={UserEdit}/>
        <Route exact path='/user-list' component={UserList}/>
      </Provider>
    </Router>
  </div>)
}

export default App