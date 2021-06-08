import React, { useState } from 'react'

const Todo = () => {
    
    const [ item, setItem ] = useState('')

    return( <>
    <h1> Todo List </h1>
    <h4> { item } </h4><br/>
    <input onChange = { e => setItem(e.target.value)}/>
    <button onClick = { () => setItem( '' )}> 초기화 </button><br/>
    </>)
}

export default Todo