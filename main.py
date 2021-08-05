import app1
import app2
import app
import streamlit as st
PAGES = {
    "APP1":app1,
    "APP2":app2,
    "APP3":app,
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page= PAGES[selection]
page.app()