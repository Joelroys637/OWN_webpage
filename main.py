import streamlit as st
from streamlit_option_menu import option_menu
import adout as ab

adsense_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="google-adsense-account" content="ca-pub-7596984091672717">
    <title>Example Streamlit Page</title>
</head>
</html>
"""
st.components.v1.html(adsense_html, height=300)

st.write("https://drive.google.com/drive/folders/1m-VrRZz67QLG4XG7nlh7mKqLRT3UGKIb?usp=sharing")
st.title("project")
st.write("software file")
a="https://drive.google.com/drive/folders/1gITi_Mg6PH6958xmlqDskYkM-yJzp3gI?usp=drive_link"
st.write(a)
st.write("source file")
b="https://drive.google.com/drive/folders/1S_e8pv8PXpMy2OI28XWv5TQ_xL2XAO6k?usp=drive_link"
st.write(b)
st.write("photo url")
c="sjctni.edu/images/SPhotos/22/22ucs101.jpg"
st.write(c)
st.markdown("""
        <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f6d365, #fda085);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            opacity: 0;
            animation: fadeIn 2s forwards;
            margin-bottom: 2rem;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #333;
        }

        p {
            font-size: 1.2rem;
            color: #555;
        }

        .image-container {
            text-align: center;
        }

        .clickable-image {
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .clickable-image:hover {
            transform: scale(1.1);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title="",  
        options=["HOME", "Portfolio","About"],
        icons=["house", "briefcase","info-circle"],
        default_index=0
    )


if selected == "HOME":
    
    # Add custom CSS for the animated container and image
    st.markdown("""
        <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #f6d365, #fda085);
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 2rem;
            background: orange;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            opacity: 0;
            animation: fadeIn 2s forwards;
            margin-bottom: 2rem;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #333;
        }

        p {
            font-size: 1.2rem;
            color: #555;
        }

        .image-container {
            text-align: center;
        }

        .clickable-image {
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .clickable-image:hover {
            transform: scale(1.1);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        </style>
        """, unsafe_allow_html=True)

    # Display the animated container with text
    st.markdown("""
        <div class="container">
            <h1>Welcome to My Website</h1>
            <p>HELLO EVERYONE</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <br><br><br>
    """, unsafe_allow_html=True)

    # Add description text with styling
    st.markdown("""
    <center>
    <p style="color: red;">Python web Project in School Admission form</p></center>
    """, unsafe_allow_html=True)

    # Display the image as a clickable link
    st.markdown("""
        <div class="image-container">
            <a href="https://leo-databaseschool.streamlit.app/" target="_blank">
                <img src="https://c4.wallpaperflare.com/wallpaper/645/96/47/python-programming-programming-programming-language-code-hd-wallpaper-preview.jpg" class="clickable-image" alt="Click to open webpage">
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <br><br><br><br>
    """, unsafe_allow_html=True)

    # VB.NET project section with images
    st.markdown("""
    <center>
    <p style="color: red;">VB.NET PROJECT</p></center>
    """, unsafe_allow_html=True)
    
    st.image("1.png")
    st.image("2.png")

    # Download section for VB.NET project
    st.markdown("""
    <center>
    <p style="color: blue;">Download the exe file</p></center>
    """, unsafe_allow_html=True)
    
    st.image("3.png")

    # Clickable image for downloading from Google Drive
    st.markdown("""
    <center>
    <p style="color: blue;">Click the image</p></center>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="image-container">
            <a href="https://drive.google.com/drive/folders/1GhLJYoRPaeksuXIECK188q34BTzzv0i8?usp=sharing" target="_blank">
                <img src="https://th.bing.com/th/id/OIP.qMY7Bs0vQxjAhMG6Z9-3ggAAAA?w=400&h=239&rs=1&pid=ImgDetMain" class="clickable-image" alt="Click to download">
            </a>
        </div>
        """, unsafe_allow_html=True)

# Placeholder for 'Portfolio' section (you can develop this later)
elif selected == "Portfolio":
    st.markdown("""
        <div class="image-container">
            <a href="https://joelroys637.github.io/final_html_portfolio/index.html" target="_blank">
                <img src="https://static.vecteezy.com/system/resources/previews/002/574/291/large_2x/portfolio-case-for-transporting-vector.jpg" class="clickable-image" alt="Click to download">
            </a>
        </div>
        """, unsafe_allow_html=True)

elif selected=="About":
    ab.main()
