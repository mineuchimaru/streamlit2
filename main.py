import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("プロフィールサイト")

st.write("プログレスバーの表示")
"Start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"


