import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(100, 2) / [0.5, 0.5] + [55.5, 37.33],
    columns=['lat', 'lon'])
st.map(df)