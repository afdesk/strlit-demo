import streamlit as st
import numpy as np

values = range(10)

labels = ['all'] + list(map(str, values))

selected = st.sidebar.multiselect(
    'How to filter the values?',
    labels,
)

if 'all' in selected:
    st.write(np.array(values))
else:
    st.write(np.array([values[i] for i in map(int, selected)]))