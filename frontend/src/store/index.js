import { createStore } from 'redux'
import TodoReducer from './Todoreducer'
export { default as TodoReducer } from './Todoreducer'
export const store = createStore(TodoReducer)
