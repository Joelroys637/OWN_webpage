import streamlit as st

def main():

    st.markdown("""
        <div class="container">
            <h2>About Me</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center;">
        <img src="https://sjctni.edu/images/SPhotos/22/22ucs101.jpg" alt="Your Image" style="border-radius: 50%; max-width: 150px;">
        </div>

        <br>
        <p><strong>Name:</strong> LEO JOEL ROYS J</p>
        <p><strong>Contact Number:</strong> +91 8838343971</p>
        <p><strong>Email:</strong> joelroys637@.com</p>
        <p><strong>Bio:</strong> I am a software developer with experience in web development and windows application.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        h2 {
            color: #333;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }

        p {
            font-family: 'Arial', sans-serif;
            font-size: 1.2rem;
            color: #555;
        }

        img {
            width: 150px;
            height: 150px;

            
        }
        .{
            style="max-width: 100%;border-radius: 50px;
        }
        div {
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)