import streamlit as st
from st_pages import show_pages_from_config, add_page_title
from pathlib import Path


if __name__ == '__main__':
  show_pages_from_config()
  st.write(Path("static/introduction.md").read_text(), unsafe_allow_html=True)
  with st.expander("**Review of Probability Theory**", expanded=False):
    
    st.write(Path("static/review_of_probability_theory.md").read_text())
    
  st.write(Path("static/bayes_theorem.md").read_text(), unsafe_allow_html=True)
  
  st.stop()