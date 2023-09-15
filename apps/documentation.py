# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan


import streamlit as st


DOCUMENT_STRING = """
### Table of contents

1. [Giới thiệu](#introduction)
2. [Hướng dẫn sử dụng](#how_to_use)
    - 2.1  [Tạo một email-marketing cơ bản](#simple)
    - 2.2  [Viết lại nội dung trong email-marketing](#content_rewriting)
    - 2.3  [Trợ lý ChatMSpot](#assistant)
---


### <a name='introduction'></a> 1. Giới thiệu

**Công cụ AI tạo sinh Email-marketing (β)** là bản thử nghiệm ứng dụng công nghệ AI tạo sinh (Generative-AI) trong Email 
Marketing. 

**Công cụ Công cụ AI tạo sinh Email-marketing (β)** tiên tiến, một bước đột phá trong lĩnh vực quảng cáo qua email. 
Được phát triển dựa trên công nghệ AI tạo sinh hàng đầu, công cụ này mang đến ba tính năng ấn tượng:

1. **Tạo Email Marketing Tự Động**: Bạn không cần là một chuyên gia viết nội dung để tạo email marketing cuốn hút. 
Với sự trợ giúp của AI, việc tạo mới email marketing trở nên nhanh chóng và dễ dàng hơn bao giờ hết. Chỉ cần một số 
thông tin cơ bản, công cụ sẽ tạo nên những email chất lượng cao để tương tác với khách hàng của bạn.

2. **Viết Lại Nội Dung Hiệu Quả**: Công cụ của chúng tôi không chỉ giúp bạn tạo mới email, mà còn có khả năng viết lại nội 
dung trong email marketing hiện có. Bạn có thể nâng cấp và tối ưu hóa nội dung để đảm bảo thông điệp của bạn luôn hiện 
diện một cách tối ưu trước mắt khách hàng.

3. **Chatbot ChatMSpot - Trợ Lý AI Chuyên Nghiệp**: ChatMSpot là người bạn đồng hành đắc lực của bạn trong lĩnh vực 
AI-Marketing. Với khả năng tư vấn thông minh và cung cấp hướng dẫn chi tiết, ChatMSpot giúp bạn tối ưu hóa chiến dịch 
marketing của mình và nắm bắt những cơ hội tốt nhất trong thế giới tiếp thị dựa trên trí tuệ nhân tạo.

Chúng tôi tin rằng công cụ này sẽ là một phần quan trọng trong chiến lược tiếp thị của bạn, giúp bạn 
tiết kiệm thời gian và tài nguyên, đồng thời tăng cường hiệu suất chiến dịch của bạn. Hãy khám phá và trải nghiệm sự 
khác biệt ngay hôm nay.

### <a name='how_to_use'></a> 2. Hướng dẫn sử dụng

#### <a name='simple'></a> 2.1 Tạo một Email-marketing cơ bản

#### <a name='content_rewriting'></a> 2.2 Viết lại nội dung trong Email-marketing

#### <a name='assistant'></a> 2.3 Trợ lý ChatMSpot

--- 

<p style="text-align: center;"><b>Công cụ tạo sinh Email-marketing</b> được phát triển bởi AI Team thuộc Viện Nghiên 
cứu và Phát triển Công nghệ - MISA © Copyright 2023.</p>

<p style="text-align: center;">Nếu có câu hỏi hoặc phản hồi nào, vui lòng liên hệ với chúng tôi qua email: 
phanxuanphucnd@gmail.com.</p>

<p style="text-align: center;">Cảm ơn bạn đã quan tâm tới sản phẩm của chúng tôi! 🤗</p>
"""


def template_documentation():
    st.markdown(DOCUMENT_STRING, unsafe_allow_html=True)
