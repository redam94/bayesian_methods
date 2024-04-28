import streamlit as st
from components.constants import SAMPLING_PATH
from components.plotting.bayesian_methods import rejection_sampling
from components.text.markdown_reader import load_md_file


st.write(load_md_file(SAMPLING_PATH/"sampling.md"), unsafe_allow_html=True)
with st.expander("## Sampling to solve an integral"):
  N = st.slider("Select the number of samples", 0, 1000, step=100)
  fig = rejection_sampling(N)
  fig