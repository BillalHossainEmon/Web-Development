import AppName from "./components/Appname";
import AddTodo from "./components/AddTodo";
import TodoItems from "./components/TodoItems";
import "./App.css";
function App() {
  const todoItems = [
    {
      name: "Buy Milk",
      dueDate: "14/07/2024"
    },
    {
      name: "Go To Office",
      dueDate: "15/07/2024"
    },
    {
      name: "Go To Gym",
      dueDate: "15/07/2024"
    },
  ];
  
  return (
    <center className="todo-container">
      <AppName/>
      <AddTodo/>
      <TodoItems todoItems={todoItems}></TodoItems>
   </center>
    );
}

export default App
