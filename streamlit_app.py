import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Zajęcia 1. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Translator EN - DE')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('Aplikacja pozwalająca na translację języka angielskiego na niemiecki używając wytrenowanego modelu T5.')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

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
        st.write(de_text)

st.subheader('s19978')
