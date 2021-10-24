import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.title('Zajęcia 1. Streamlit')

st.header('Translator EN - DE')

st.text('Aplikacja pozwalająca na translację języka angielskiego na niemiecki używając wytrenowanego modelu T5.')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    "Opcje",
    [
        "Translacja EN - DE"
    ],
)

if option == "Translacja EN - DE":
    en_text = st.text_area(label="Wpisz tekst")
    if en_text:
        translator = pipeline("translation_en_to_de")
        de_text = translator(en_text, max_length=40)
        st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
        st.write(de_text)

st.subheader('s19978')
