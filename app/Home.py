import streamlit as st
from st_pages import show_pages_from_config, add_page_title
from pathlib import Path
from components.constants import INTRODUCTION_PATH
from components.plotting.bayesian_methods import geometric_bayes, plot_posterior
from components.text.markdown_reader import load_md_file, replace_vars
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

if st.session_state.get('c', None) is None:
  st.session_state['c'] = 0.02
  

if __name__ == '__main__':
  show_pages_from_config()
  
  st.write(load_md_file(INTRODUCTION_PATH/"introduction.md"), unsafe_allow_html=True)   
  st.write(replace_vars(load_md_file(INTRODUCTION_PATH/"bayes_theorem.md"), 
                        **{"varc": st.session_state.c, 
                           "varc|t": st.session_state.c*.938/(.938*st.session_state.c + .04*(1.0-st.session_state.c))}), 
           unsafe_allow_html=True)
  
  with st.expander("## Probability of Test Given Prior $P(C)$"):
    c = st.slider("Select a value for $P(C)$", 0.0, 1.0, step=0.01, key='c')
    fig1 = plot_posterior(c)
    
    fig = geometric_bayes(c, .04, .938)
    fig, fig1
    
  if st.button("Next Page"):
    st.switch_page('my_pages/Sampling.py')