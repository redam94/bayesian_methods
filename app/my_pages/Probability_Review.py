import streamlit as st
from components.constants import INTRODUCTION_PATH
from components.text.markdown_reader import load_md_file

st.write(load_md_file(INTRODUCTION_PATH/"review_of_probability_theory.md"))