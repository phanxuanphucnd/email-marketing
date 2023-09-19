# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan

import time
import uuid
import openai
import streamlit as st
from apps.constants import *
from apps.ui.chat_ui import *


openai.api_key = "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"

openai_params = {
    'temperature': 1,
    'top_p': 1,
    'model': "gpt-3.5-turbo-16k"
}

INITIAL_MESSAGE = [
    {
        "role": "assistant",
        "content": "Xin chào, tôi có thể giúp gì cho bạn?",
    },
]

st.session_state["model"] = 'GPT-3.5'

# if 'id' not in st.session_state:
#     user_id = uuid.uuid4().hex
#     st.session_state["id"] = user_id
#
# st.info(st.session_state["id"])


def call_openai(messages, max_tokens: int = 512, stream: bool = False):
    response = openai.ChatCompletion.create(messages=messages, max_tokens=max_tokens, stream=stream, **openai_params)
    response = response["choices"][0]["message"]["content"]

    return response


def template_assistant():
    st.header(":rainbow[ChatMSpot]")
    st.markdown(
        "<i style='color:blue'>A Virtual assistant creates content<i>",
        unsafe_allow_html=True
    )
    with open("apps/ui/style.md", "r") as styles_file:
        styles_content = styles_file.read()

    messages = [
        {
            "role": "system",
            "content": "Bạn là một trợ lý ảo tạo nội dụng AI Marketing."
        }
    ]

    # Add a reset button
    if st.sidebar.button("♻️  Chủ đề mới", use_container_width=True):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.session_state["messages"] = INITIAL_MESSAGE.copy()
        st.session_state["history"] = []
        messages = [
            {
                "role": "system",
                "content": "Bạn là một trợ lý ảo tạo nội dụng AI Marketing."
            }
        ]

    # st.write(styles_content, unsafe_allow_html=True)

    # Initialize the chat messages history
    if "messages" not in st.session_state.keys():
        st.session_state["messages"] = INITIAL_MESSAGE.copy()

    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "model" not in st.session_state:
        st.session_state["model"] = 'GPT-3.5'

    # Prompt for user input and save
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state["messages"]:
        message_func(
            message["content"],
            True if message["role"] == "user" else False,
            True if message["role"] == "data" else False,
        )

    # callback_handler = StreamlitUICallbackHandler()

    def append_message(content, role="assistant", display=False):
        message = {"role": role, "content": content}
        message_func(content, False, display)
        st.session_state.messages.append(message)
        if role != "data":
            append_chat_history(st.session_state.messages[-2]["content"], content)

    if st.session_state.messages[-1]["role"] != "assistant":
        content = st.session_state.messages[-1]["content"]
        print("\n-------------- *** --------------")
        if isinstance(content, str):
            # messages.append({
            #     'role': 'user',
            #     'content': content
            # })
            messages = st.session_state['messages']
            bot_response = call_openai(messages, max_tokens=1024, stream=False)

            print(f"\n++ Call openai with messages: {messages}")
            print(f"[USER]:\t{content}")
            print(f"[BOT RESPONSE]:\t{bot_response[:256]}")
            append_message(bot_response)
