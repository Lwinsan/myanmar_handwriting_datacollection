import pandas as pd
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from io import BytesIO
#from Pillow import Image
import os



import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('bg_image.jpg')   





st.header("မြန်မာလက်ရေး အက္ခရာ ဒေတာစုခြင်း")

col1, col2 = st.columns([1,1])


#text = st.text_input('Enter Alphabet!')

st.subheader("၁။ ရေးမည့်စာလုံးအားရွေးချယ်ပါ...")
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

text = st.selectbox(
        "Select Alphabet!",
        ("00_က", "01_ခ", "02_ဂ", "03_ဃ", "04_င", "05_စ", "06_ဆ", "07_ဇ", "08_ဈ", "09_ည", "10_ဋ", "11_ဌ", "12_ဍ", "13_ဎ", "14_ဏ", "15_တ", "16_ထ", "17_ဒ", "18_ဓ", "19_န", "20_ပ", "21_ဖ", "22_ဗ", "23_ဘ", "24_မ", "25_ယ", "26_ရ", "27_လ", "28_ဝ", "29_သ", "30_ဟ", "31_ဠ", "32_အ"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

col1, col2 = st.columns([1,1])

with col1:
    st.subheader("၂။ ဤနေရာတွင်ရေးပါ ...⬇️")
    
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=20,
        stroke_color="black",
        background_color="white",
        height=350,
        width=350,
        drawing_mode="freedraw",
        key="canvas",
    )


if canvas_result.image_data is not None:
        
    im = Image.fromarray(canvas_result.image_data)
    

    
# Add a download button
if st.button("ဓါတ်ပုံအဖြင့်သိမ်းမည်"):
    image_counter = text
    file_dir = os.path.abspath("downloads")
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    file_path = os.path.join(file_dir, f"mAlp_{image_counter}.png")
    im.save(file_path)
    st.markdown(f"{file_path}")
    st.markdown(f'"{image_counter}" အား အထက်ပါ ဖိုင်လမ်းကြောင်းအတိုင် အောင်မြင်စွာသိမ်စည်းပြီးပါပြီ။')
