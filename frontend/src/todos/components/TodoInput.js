import React, { useState } from 'react'
import { useDispatch } from "react-redux"
import { v4 as uuidv4 } from 'uuid'
import { addTodoAction } from 'store/Todoreducer'

const TodoInput = () => {
    const [ todo, setTodo ] = useState('')
    const dispatch = useDispatch();

    const submitForm = e => {
        e.preventDefault()
        console.log(`uuidv4 : ${uuidv4()}`)
        const newTodo = {
            id: uuidv4(),
            name: todo, 
            complete: false
        }
        addTodo(newTodo)
        setTodo('')    
    }
    
    const addTodo = todo => dispatch(addTodoAction(todo))

    const handleChange = e => {
        e.preventDefault()
        setTodo(e.target.value)
    }

    return (<>
    <h1>To do list</h1><br/>
    <form onSubmit = { submitForm } method="POST">
        <div className="row mt-3">
            <div className="form-group col-sm-8">
                <input
                    type="text"
                    placeholder='Input Todo'
                    name="todo"
                    className="form-contrl"
                    value={ todo }
                    onChange={ handleChange }
                />
            </div>
        </div>
    </form>
    </>)
}

export default TodoInput