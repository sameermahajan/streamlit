import streamlit as st
from langchain.schema import ChatMessage

prompts = ["1. What is the value for the first option ?", "2. What is the value for the second option ?", 
           "3. What is the value for the third option ?", "4. What the value for the fourth option ?"]

if "messages" not in st.session_state:
    st.session_state["messages"] = [ChatMessage(role="assistant", content=prompts[0])]
    st.session_state["id"] = 1
    st.session_state["option1"] = st.session_state["option2"] = st.session_state["option3"] = st.session_state["option4"] = None

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if user_input := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=user_input))
    st.chat_message("user").write(user_input)

    match st.session_state["id"]:
        case 1:
            st.session_state["option1"] = user_input
        case 2:
            st.session_state["option2"] = user_input
        case 3:
            st.session_state["option3"] = user_input
        case 4:
            st.session_state["option4"] = user_input

    if st.session_state["id"] < 4:
        prompt = prompts[st.session_state["id"]]
        with st.chat_message("assistant"):
            st.session_state.messages.append(ChatMessage(role="assistant", content=prompt))
            st.write(prompt)
        st.session_state["id"] += 1

st.write(st.session_state["option1"], st.session_state["option2"], st.session_state["option3"], st.session_state["option4"])