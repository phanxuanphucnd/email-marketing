# -*- coding: utf-8 -*-
# Copyright (c) 2023 by Phuc Phan


SYSTEM_PROMPT = [
    """Bạn là một trợ lý ảo tạo nội dụng AI Marketing. Một email marketing gồm có 4 phần:
- Tiêu đề
- Nội dung
- Lời kêu gọi hành động
- Phần kết""",
    """Bạn là một trợ lý ảo tạo nội dụng AI Marketing. Bạn có khả năng viết email marketing đa dạng lĩnh vực. Một email marketing gồm có 4 phần:
- Tiêu đề
- Nội dung
- Lời kêu gọi hành động
- Phần kết""",
    """Bạn là một trợ lý ảo tạo nội dụng AI Marketing."""
]


TITLE_PROMPT = """Viết tiêu đề cho cho một Email Marketing với chủ đề về {topic} theo phong cách viết: {tone_email} và 
bằng ngôn ngữ: {language}."""

CONTENT_PROMPT = """Viết phần nội dung của Email Marketing với {n} điểm chính (key points) như sau:
- {key_points}

Viết phần nội dung trên theo phong cách {tone_email} và bằng ngôn ngữ {language}."""


REWRITE_CONTENT_PROMPT = {
    'Viết lại': """Viết lại một đoạn dưới đây theo phong cách {tone_email} và bằng ngôn ngữ {language}:

"{content}".""",
    'Mở rộng thêm': """Viết lại một đoạn dưới đây theo phong cách {tone_email}, nhiều thông tin hơn và bằng ngôn ngữ {language}:

"{content}".""",
    'Tóm tắt lại': """Tóm tắt lại một đoạn dưới đây theo phong cách {tone_email} và bằng ngôn ngữ {language}:

"{content}"."""
}
