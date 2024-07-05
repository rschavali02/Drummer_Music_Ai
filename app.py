from audiocraft.models import MusicGen
import streamlit as st
import os 
import torch 
import torchaudio
import numpy as np
import base64
import sentencepiece
import xformers

##Do on Google Colab so I can run melody, otherwise run small
def load_model():
    try:
        model = MusicGen.get_pretrained("facebook/musicgen-small")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

st.set_page_config(
    page_icon = "🥁", 
    page_title = "Background Music Generator for Drummers"
)

def main():
    st.title("Melodic Music Generation")

    with st.expander("See Explanation"):
        st.write("This is a Music Generation app for drummers built using Meta's Audiocraft Music Gen model")

text_area = st.text_area("Enter your Description......")
##If can run on gpu, set to larger time
time_slider = st.slider("Set a time duration (In seconds)", 2, 20, 5)

if text_area and time_slider:
    st.json(
        {
            "Your Description" : text_area,
            "Selected Time Duration (In Seconds):" : time_slider
           ## "Selected Tempo:" : 
        }
    )

    st.subheader("Generated Music")

    model = load_model()
    if model:
        # Placeholder for actual music generation code
        st.write("Model loaded successfully. Add music generation code here.")
    else:
        st.error("Model could not be loaded. Please check the logs for more details.")



if __name__ == "__main__" :
    main()