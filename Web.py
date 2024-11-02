import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This app aims to boost productivity")
st.write("Created by Dr3wza")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(placeholder="Enter a todo...", label="",
              on_change=add_todo, key="new_todo")

# pip freeze > requirements.txt
# (instructs the server what python packages to install
# streamlit run Web.py (runs script)
