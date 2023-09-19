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


def template_simple_email():
    is_create = False

    topic = st.text_area("**Chủ đề chiến dịch email (Topic)\*:**", "", 50, 200)

    st.write("**:black[Những điểm chính mà bạn muốn đề cập (Key points):]**")
    key_point_1 = st.text_input("Key point 1: ", "", 50)
    key_point_2 = st.text_input("Key point 2: ", "", 50)
    key_point_3 = st.text_input("Key point 3: ", "", 50)
    key_point_4 = st.text_input("Key point 4: ", "", 50)
    key_point_5 = st.text_input("Key point 5: ", "", 50)

    key_points = []
    if key_point_1:
        key_points.append(key_point_1)

    if key_point_2:
        key_points.append(key_point_2)

    if key_point_3:
        key_points.append(key_point_3)

    if key_point_4:
        key_points.append(key_point_4)

    if key_point_5:
        key_points.append(key_point_5)

    # tone = [
    # 'Friendly', 'Luxury', 'Relaxed', 'Professional',
    # 'Bold', 'Adventurous', 'Witty', 'Persuasive', 'Empathetic'
    # ]

    tone_email = st.selectbox(
        "**Phong cách (Tone):**",
        (
            "Bình thường", "Chuyên nghiệp", "Hài hước & Sáng tạo", "Thân thiện", "Sang trọng", "Thư giãn", "Táo bạo", "Mạo hiểm",
            "Hóm hỉnh", "Thuyết phục", "Đồng cảm", "Tạo kỷ niệm", "Câu chuyện", "Tương tác và Tham gia", "Cá nhân hóa",
            "Khẩn cấp"
        ),
        index=1
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
    submit_btn = st.button("**Create Content**", type="secondary")

    if submit_btn:
        is_create = True

    return is_create, topic, key_points, tone_email, language


def create_simple_email(topic, key_points, tone_email, language):
    if not topic:
        st.error("Bạn cần phải cung cấp **Chủ đề chiến dịch email (Topic)** để chúng tôi có thể hỗ trợ bạn tốt nhất!")
    else:
        print('\n\n----------------- Creating Simple Email Marketing -----------------')
        messages = []
        title_placeholder = st.empty()

        content_placeholder = st.empty()

        system_prompt = random.choice(SYSTEM_PROMPT)

        messages.extend([
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": TITLE_PROMPT.format(topic=topic, tone_email=tone_email, language=language)
            }
        ])
        title = call_openai(messages=messages, max_tokens=512)

        print(">> Messages: ", messages)
        print(">> Title: ", title)

        messages.append({
            "role": "user",
            "content": CONTENT_PROMPT.format(
                n=len(key_points), key_points='\n- '.join(key_points), tone_email=tone_email, language=language)
        })
        content = call_openai(messages=messages, max_tokens=1024)

        print("\n>> Messages: ", messages)
        print(">> Content: ", content)

        title_placeholder.write(f"**{title}**")
        content_placeholder.write(content)
