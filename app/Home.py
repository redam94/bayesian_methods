import streamlit as st
from st_pages import show_pages_from_config, add_page_title
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

if st.session_state.get('c', None) is None:
  st.session_state['c'] = 0.02
def replace_vars(text, **kwargs):
  for key, value in kwargs.items():
    if isinstance(value, float):
      value = f"{value:0.2f}"
    text = text.replace(f"<<{key}>>", f"{value}")
  return text

if __name__ == '__main__':
  show_pages_from_config()

  st.write(Path("static/introduction.md").read_text(), unsafe_allow_html=True)
  with st.expander("**Review of Probability Theory**", expanded=False):
    
    st.write(Path("static/review_of_probability_theory.md").read_text())
   
  st.write(replace_vars(Path("static/bayes_theorem.md").read_text(), 
                        **{"varc": st.session_state.c, "varc|t": st.session_state.c*.938/(.938*st.session_state.c + .04*(1.0-st.session_state.c))}), 
           unsafe_allow_html=True)
  
  pc = np.linspace(0, 1, 100)
  pt = pc*.938/(.938*pc + .04*(1.0-pc))
  with st.expander("## Probability of Test Given Prior $P(C)$"):
    c = st.slider("Select a value for $P(C)$", 0.0, 1.0, step=0.1, key='c')
    fig, ax = plt.subplots()
    ax.plot(pc, pt, color='black')
    ax.scatter(c, c*.938/(.938*c + .04*(1.0-c)), color='red', s=50)
    ax.set_xlabel("$P(C)$")
    ax.set_ylabel("$P(T|C)$")
    ax.set_title("Probability of Test Given Prior $P(C)$")
    fig
  st.stop()