from PIL import Image
from apps.assistant import *
from apps.documentation import *
from apps.content_rewriter import *
from apps.simple_email_creator import *
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Email Marketing Content Creator", layout="wide", page_icon="📩")


def create_header(header: str = "Công cụ tạo nội dung Email-marketing"):
    image = Image.open('imgs/misa-email-marketing.jpg')

    st.header(header, divider='rainbow')
    st.image(image, width=200, use_column_width=True)
    st.markdown(
        "<b style='color:blue;'> From: AI Team - Viện Nghiên cứu và Phát triển Công nghệ</b><br>"
        "<i style='color:blue'>Chúng tôi có thể tạo ra tất cả những gì bạn muốn!<i>",
        unsafe_allow_html=True
    )
    st.write('\n\n')


with st.sidebar:
    menu = option_menu(
        "Tất cả", ["Simple", "Content Rewriter", "AI Assistant", 'Document'],
        icons=['alexa', 'alexa', 'alexa', 'badge-hd'],
        menu_icon="cast",
        default_index=0
    )

topic, key_points, style_email, language = None, None, None, None

if menu == "Simple":
    create_header(header="Công cụ tạo nội dung Email-marketing")
    # create_header(header="Email-marketing Content Creation Tool")
    column1, column2 = st.columns(2)
    with column1:
        st.subheader("Thiết kế", divider='rainbow')
        is_create, topic, key_points, style_email, language = template_simple_email()

    with column2:
        st.subheader("Kết quả", divider='rainbow')

        if is_create:
            create_simple_email(topic, key_points, style_email, language)


if menu == 'Content Rewriter':
    create_header(header="Công cụ viết lại nội dung Email-marketing")
    # create_header(header="Email-marketing Content Rewriting Tool")
    column1, column2 = st.columns(2)
    with column1:
        st.subheader("Thiết kế", divider='rainbow')
        is_rewrite, content, tone_email, style_email, language = template_content_rewriter()

    with column2:
        st.subheader("Kết quả", divider='rainbow')

        if is_rewrite:
            rewrite_content(content, tone_email, style_email, language)

if menu == 'AI Assistant':
    template_assistant()


if menu == 'Document':
    create_header(header="Bí kíp sử dụng công cụ tạo sinh Email-marketing hiệu quả")
    template_documentation()
