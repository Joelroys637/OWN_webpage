import streamlit as st


def main():
    st.markdown(
    """
    <div class="image-container">
        <a href="https://leo-databaseschool.streamlit.app/" target="_blank"></a>
    </div>
    """, 
    unsafe_allow_html=True
    )
    st.image("2.png")