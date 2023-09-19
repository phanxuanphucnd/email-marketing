# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan


import openai
import random
import streamlit as st
from apps.constants import *

openai.api_key = "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"

openai_params = {
    'temperature': 1,
    'top_p': 1,
    'model': "gpt-3.5-turbo-16k",
    'stream': False
}


def call_openai(messages, max_tokens: int = 512):
    response = openai.ChatCompletion.create(messages=messages, max_tokens=max_tokens, **openai_params)
    response = response["choices"][0]["message"]["content"]

    return response


def template_content_rewriter():
    is_rewrite = False

    content = st.text_area("**Nội dung cần viết lại\*:**", "", 500, 1024)
    tone_email = st.selectbox(
        "**Phong cách (Tone):**",
        (
            "Bình thường", "Chuyên nghiệp", "Hài hước & Sáng tạo", "Thân thiện", "Sang trọng", "Thư giãn", "Táo bạo", "Mạo hiểm",
            "Hóm hỉnh", "Thuyết phục", "Đồng cảm", "Tạo kỷ niệm", "Câu chuyện", "Tương tác và Tham gia", "Cá nhân hóa",
            "Khẩn cấp"
        ),
        index=1
    )

    style_email = st.selectbox(
        "**Chế độ (Mode):**",
        (
            "Viết lại",
            "Mở rộng thêm",
            "Tóm tắt lại"
        ),
        index=0
    )

    language = st.selectbox(
        "**Ngôn ngữ (Language):**",
        (
            "Tiếng Việt",
            "Tiếng Anh"
        ),
        index=0
    )

    st.write("")
    st.write("")
    m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #024a2d;
            color:#ffffff;
        }
        div.stButton > button:hover {
            background-color: #64d1a4;
            color:#ffffff;
            }
        </style>""", unsafe_allow_html=True)
    submit_btn = st.button("**Rewrite Content**", type="secondary")

    if submit_btn:
        is_rewrite = True

    return is_rewrite, content, tone_email, style_email, language


def rewrite_content(content, tone_email, style_email, language):
    if not content:
        st.error("Bạn cần phải cung cấp **Nội dung cần viết lại** để chúng tôi có thể hỗ trợ bạn tốt nhất!")
    else:
        print('\n\n----------------- Rewriting Content Email Marketing -----------------')
        messages = []

        # st.write("**Nội dung được viết lại:**")
        st.write("")
        st.write("")
        content_placeholder = st.empty()

        messages.extend([
            {
                "role": "system",
                "content": "Bạn là một trợ lý ảo tạo nội dụng AI Marketing."
            },
            {
                "role": "user",
                "content": REWRITE_CONTENT_PROMPT[style_email].format(
                    tone_email=tone_email, language=language, content=content)
            }
        ])
        content = call_openai(messages=messages, max_tokens=1024)

        print(">> Messages: ", messages)
        print(">> Re-written Content: ", content)

        content_placeholder.write(content)
