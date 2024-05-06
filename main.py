import streamlit as st
from experiment import ScanImage
from PIL import Image
import os

@st.cache
def load_image(image_file):
   img = Image.open(image_file)
   return img


electricity_bill=st.file_uploader("Upload a clear image of Electricity Bill")
if electricity_bill:
    img = load_image(electricity_bill)
    st.image(img)

    with open(os.path.join("Electricity",electricity_bill.name),'wb') as f:
        f.write(electricity_bill.getbuffer())
    ScanImage()
    st.success("File Saved")