import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

RNG = np.random.default_rng(seed=42)
REJECTION_X = RNG.uniform(0, 1, 1000)
REJECTION_Y = RNG.uniform(0, 1, 1000)
REJECTION_C = np.linspace(0, 1, 1000)
REJECTION_COLORS = np.array(['red', 'green'])
REJECTION_INSIDE = ((REJECTION_Y**2 + REJECTION_X**2)<1).astype(int)

@st.cache_resource()
def rejection_sampling(n):
  """ Make a plot of rejection sampling using n samples of a quarter circle

  Args:
      n (int): Number of samples to plot

  Returns:
      Figure: returns a matplotlib figure
  """
  
  fig, ax = plt.subplots()

  x = REJECTION_X[:n]
  y = REJECTION_Y[:n]
  c = REJECTION_C
  colors = REJECTION_COLORS
  inside = REJECTION_INSIDE[:n]
  # Show the integral
  ax.text(.1, 1.2, 
          (r"Estimate of $\int^1_0\sqrt{1-x^2}dx=\frac{N_{in}}{N}$" 
           + f"={(np.mean(inside) if len(inside)>0 else 0):0.3f}\n"
           + r"Analytical Solution: $\frac{\pi}{4}\approx 0.785$"), 
          fontsize=8, color='black')
  # Plot the samples
  ax.scatter(x[inside==1], y[inside==1], color=colors[1], s=10, label='Inside: $N_{in}$'+f"={np.sum(inside)}")
  ax.scatter(x[inside==0], y[inside==0], color=colors[0], s=10, label='Outside: $N-N_{in}$'+f"={n-np.sum(inside)}")
  # Plot the quarter circle
  ax.plot(c, np.sqrt(1-c**2), color='black')
  # Plot the sample space
  ax.vlines(1, 0, 1, color='black', ls='--')
  ax.hlines(1, 0, 1, color='black', ls='--')

  
  ax.text(0.9, 0.8, f"", fontsize=8, color='black')
  ax.set_xlim(0, 1.8)
  ax.set_ylim(0, 1.5)
  ax.set_title("Sampling to Solve the Area of a Quarter Circle")
  ax.legend()
  return fig


@st.cache_resource()
def geometric_bayes(p, sp, sn):
  """Make a plot of a geometric interpretation of Bayes Theorem"""
  fig, ax = plt.subplots()
  ### Add the lines for the geometric interpretation
  ax.vlines(p, 0, 1, color='black', lw=.5) # P(C)
  ax.hlines(sn, 0, p, color='black') # P(T|C)
  ax.hlines(sp, p, 1, color='black') # P(T|not C)
  ax.set_xlabel("$P(C)$")
  ax.set_ylabel("$P(T|C)$")
  
  ## Add legend
  ax.text(1.2,.9, f"True Pos: \n$P(T=t|C=t)={p*sn:0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  tp_label = mpatches.Rectangle((1.08, .915), .02, .02, color='green', alpha=0.5)
  ax.add_patch(tp_label)
  ax.text(1.2,.8, f"False Pos:\n$P(T=t|C=f)={(1-p)*sp:0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  fp_label = mpatches.Rectangle((1.08, .915-(.1)), .02, .02, color='red', alpha=0.5)
  ax.add_patch(fp_label)
  ax.text(1.2,.7, f"True Neg:\n$P(T=f|C=f)={(1-p)*(1-sp):0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  tn_label = mpatches.Rectangle((1.08, .915-2*(.1)), .02, .02, color='lightgreen', alpha=0.5)
  ax.add_patch(tn_label)
  ax.text(1.2,.6, f"False Neg:\n$P(T=f|C=t)={(p)*(1-sn):0.2f}$", 
          fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')
  
  ## Add the posterior probability
  ax.text(1.2, .3, 
          ("$P(C|T)=\\frac{tp}{tp+fp}$"
           +("$=\\frac{tp}{tp+fp}$\n"
           .replace("tp", f"{p*sn:0.2f}")
           .replace("fp", f"{(1-p)*sp:0.2f}")
           )+ f"$={p*sn/(p*sn+(1-p)*sp):0.2f}$"), fontsize=8, color='black',
          horizontalalignment='center', verticalalignment='center')

  ## Add the rectangles for the geometric interpretation
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
  
  # set the axis limits and title
  ax.set_xlim(0, 1.45)
  ax.set_title("Geometric Interpretation of Bayes Theorem")

  return fig

@st.cache_resource()
def plot_posterior(c: float):
  """Plot the posterior probability of having covid given a positive test result"""
  pc = np.linspace(0, 1, 100) # P(C)
  pt = pc*.938/(.938*pc + .04*(1.0-pc)) # P(C|T)
  fig, ax = plt.subplots()
  ax.plot(pc, pt, color='black')
  ax.scatter(c, c*.938/(.938*c + .04*(1.0-c)), color='red', s=50) # Selected Point
  
  ax.set_xlabel("$P(C)$")
  ax.set_ylabel("$P(C|T)$")
  ax.set_title("Probability of Having Covid After Positive Test:\nGiven Prior $P(C)$")
  return fig