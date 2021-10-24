import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

st.title('Zajęcia 1. Streamlit')

st.header('Translator EN - DE')

st.text('Aplikacja pozwala na translację języka angielskiego na niemiecki.')
st.text('Używa do tego wytrenowanego modelu uczenia maszynowego T5.')
st.text('')
st.text('')

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
        try:
            de_text = translator(en_text, max_length=40)
            st.success('Świetnie! Udało się przetłumaczyć tekst')
            st.write(de_text)
        catch Exception:
            st.error('Ups. Cos poszło nie tak...')

st.subheader('s19978')
