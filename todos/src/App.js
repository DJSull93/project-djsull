import { Schedule } from './containers'
import { Route } from "react-router-dom"

const App = () => {
  return (
    <>
      <Route exact path='/' component={ Schedule }/>
    </>
  )
}

export default App;