import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()
# import znanych nam bibliotek

filename = "model.sv"
model = pickle.load(open(filename,'rb'))
# otwieramy wcześniej wytrenowany model

zdrowie = {0:"chory",1:"wyleczony"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem
def main():

	st.set_page_config(page_title="Czy będziesz zdrowy po tygodniu?")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	with overview:
		st.title("Czy będziesz zdrowy po tygodniu?")

	with right:
		objawy_slider = st.slider("Objawy", value=1, min_value=1, max_value=5)
		wiek_slider = st.slider( "Wiek", min_value=11, max_value=77)
		choroby_slider = st.slider( "Choroby", min_value=0, max_value=5)
		wzrost_slider = st.slider( "Wzrost", min_value=159, max_value=200, step=1)

	data = [[objawy_slider, wiek_slider,  choroby_slider, wzrost_slider]]
	survival = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Czy dana osoba wyzdrowieje? {0}".format("Tak" if survival[0] == 1 else "Nie"))
		st.subheader("Pewność predykcji {0:.2f} %".format(s_confidence[0][survival][0] * 100))

	st.subheader('s19978')

if __name__ == "__main__":
    main()

## Źródło danych [https://www.kaggle.com/c/titanic/](https://www.kaggle.com/c/titanic), zastosowanie przez Adama Ramblinga
