import streamlit as st



@st.cache_data()
def replace_vars(text: str, **kwargs)-> str:
  """Helper function for replacing variables in markdown files
  Args:
    text (str): the text to replace variables in
    kwargs (dict): the variables to replace"""
  for key, value in kwargs.items():
    if isinstance(value, float):
      value = f"{value:0.2f}"
    text = text.replace(f"<<{key}>>", f"{value}")
  return text


@st.cache_data()
def load_md_file(path)-> str:
  """Helper function for loading in markdown files"""
  return path.read_text()