# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan


import base64
import streamlit as st
from pathlib import Path


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' width=\"95%\" height=\"95%\" class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html


image_example_1 = img_to_html(img_path='/home/misa/phucpx/misa/email-marketing/imgs/turo1.png')
image_example_2 = img_to_html(img_path='/home/misa/phucpx/misa/email-marketing/imgs/turo2.png')
image_example_3 = img_to_html(img_path='/home/misa/phucpx/misa/email-marketing/imgs/turo3.png')
image_example_4 = img_to_html(img_path='/home/misa/phucpx/misa/email-marketing/imgs/turo4.png')


with open('./apps/ui/document.md', 'r', encoding='utf-8') as f:
    DOCUMENT_STRING = f.read()
    DOCUMENT_STRING = DOCUMENT_STRING.format(
        IMAGE_EXAMPLE_1=image_example_1,
        IMAGE_EXAMPLE_2=image_example_2,
        IMAGE_EXAMPLE_3=image_example_3,
        IMAGE_EXAMPLE_4=image_example_4
    )


def template_documentation():
    st.markdown(DOCUMENT_STRING, unsafe_allow_html=True)
