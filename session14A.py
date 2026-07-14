# import streamlit as st

# st.set_page_config(page_title='Agentic chat UI')
# st.subheader('Write a task to delegate')

# task_clues = {
#     'how to create a task': 'create task: title, descriptin, action(call etc), contact_name, contact_phone',
#     'how to view task': 'list all tasks',
#     'how to update task': 'update task: title, descriptin, action(call etc), contact_name, contact_phone',
#     'how to delete task': 'delete tasks: title',
# }

# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# user_input=st.chat_input('Type your task here')

# if user_input:

#     message = {
#         'role': 'user',
#         'content': user_input
#     }

#     st.session_state.messages.append(message)

#     with st.chat_message(message['role']):
#             st.markdown(['content'])

#     if user_input in task_clues:
#         clue = task_clues(user_input)

#         message = {
#         'role': 'assistant',
#         'content': clue
#         }
#         st.session_state.messages.append(message)

#         with st.chat_message(message['role']):
#             st.markdown(['content'])
#     else:
#         message = {
#         'role': 'assistant',
#         'content': 'Sorry, I cannot Help You'
#         }
#         st.session_state.messages.append(message)
#         with st.chat_message(message['role']):
#             st.markdown(['content'])
