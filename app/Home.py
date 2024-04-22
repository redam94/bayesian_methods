import streamlit as st
from st_pages import show_pages_from_config, add_page_title
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

if st.session_state.get('c', None) is None:
  st.session_state['c'] = 0.02

INTRODUCTION_PATH = Path("static/introduction")
SAMPLING_PATH = Path("static/sampling")

def replace_vars(text, **kwargs):
  for key, value in kwargs.items():
    if isinstance(value, float):
      value = f"{value:0.2f}"
    text = text.replace(f"<<{key}>>", f"{value}")
  return text

def plot_geo(p, sp, sn):
  prob_T = p*sn + (1-p)*(1-sp)
  fig, ax = plt.subplots()
  ax.vlines(p, 0, 1, color='black')
  ax.hlines(sn, 0, p, color='black')
  ax.hlines(sp, p, 1, color='black')
  ax.set_xlabel("$P(C)$")
  ax.set_ylabel("$P(T|C)$")
  ax.text(1.2,.9, f"True Pos: \n$P(T=t|C=t)={c*sn:0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  tp_label = mpatches.Rectangle((1.08, .915), .02, .02, color='green', alpha=0.5)
  ax.add_patch(tp_label)
  ax.text(1.2,.8, f"False Pos:\n$P(T=t|C=f)={(1-c)*sp:0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  fp_label = mpatches.Rectangle((1.08, .915-(.1)), .02, .02, color='red', alpha=0.5)
  ax.add_patch(fp_label)
  ax.text(1.2,.7, f"True Neg:\n$P(T=f|C=f)={(1-c)*(1-sp):0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  tn_label = mpatches.Rectangle((1.08, .915-2*(.1)), .02, .02, color='lightgreen', alpha=0.5)
  ax.add_patch(tn_label)
  ax.text(1.2,.6, f"False Neg:\n$P(T=f|C=t)={(c)*(1-sn):0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  
  ax.text(1.2, .3, 
          ("$P(C|T)=\\frac{tp}{tp+fp}$"
           +("$=\\frac{tp}{tp+fp}$\n"
           .replace("tp", f"{c*sn:0.2f}")
           .replace("fp", f"{(1-c)*sp:0.2f}")
           )+ f"={c*sn/(c*sn+(1-c)*sp):0.2f}"), fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')

  fn_label = mpatches.Rectangle((1.08, .915-3*(.1)), .02, .02, color='pink', alpha=0.5)
  
  ax.add_patch(fn_label)
  true_pos = mpatches.Rectangle((0,0), p, sn, color='green', alpha=0.5)
  ax.add_patch(true_pos)
  false_neg = mpatches.Rectangle((0,sn), p, 1-sn, color='pink', alpha=0.5)
  ax.add_patch(false_neg)
  false_pos = mpatches.Rectangle((p,0), 1-p, sp, color='red', alpha=0.5)
  ax.add_patch(false_pos)
  true_neg = mpatches.Rectangle((p,sp), 1-p, 1-sp, color='lightgreen', alpha=0.5)
  ax.add_patch(true_neg)
  ax.set_xlim(0, 1.4)
  #ax.axis('equal')
  return fig
  

def plot_prob(c: float):
  pc = np.linspace(0, 1, 100)
  pt = pc*.938/(.938*pc + .04*(1.0-pc))
  fig, ax = plt.subplots()
  ax.plot(pc, pt, color='black')
  ax.scatter(c, c*.938/(.938*c + .04*(1.0-c)), color='red', s=50)
  
  ax.set_xlabel("$P(C)$")
  ax.set_ylabel("$P(T|C)$")
  ax.set_title("Probability of Test Given Prior $P(C)$")
  return fig

if __name__ == '__main__':
  show_pages_from_config()

  st.write((INTRODUCTION_PATH/"introduction.md").read_text(), unsafe_allow_html=True)
  with st.expander("**Review of Probability Theory**", expanded=False):
    
    st.write((INTRODUCTION_PATH/"review_of_probability_theory.md").read_text())
   
  st.write(replace_vars((INTRODUCTION_PATH/"bayes_theorem.md").read_text(), 
                        **{"varc": st.session_state.c, 
                           "varc|t": st.session_state.c*.938/(.938*st.session_state.c + .04*(1.0-st.session_state.c))}), 
           unsafe_allow_html=True)
  
  pc = np.linspace(0, 1, 100)
  pt = pc*.938/(.938*pc + .04*(1.0-pc))
  with st.expander("## Probability of Test Given Prior $P(C)$"):
    c = st.slider("Select a value for $P(C)$", 0.0, 1.0, step=0.01, key='c')
    fig1 = plot_prob(c)
    
    fig = plot_geo(c, .04, .938)
    fig, fig1
    
  st.write((SAMPLING_PATH/"sampling.md").read_text(), unsafe_allow_html=True)
  
  st.stop()