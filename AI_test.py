import os
os.system('cls')
import time
import streamlit as st
# import streamlit_nested_layout  # nested columns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
import cv2 as cv


### * -- Set page config
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/  유용한 사이트
st.set_page_config(page_title = "AI Practice", page_icon = ":star2:", layout = "wide",    # centered, wide
                    # runOnSave = True,
                    menu_items = {                                   #   initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                        'Get Help': 'https://www.extremelycoolapp.com/help',
                        'Report a bug': "https://www.extremelycoolapp.com/bug",
                    })
### * -- Set page config


bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# bream_length = np.array(bream_length)
st.write(type(bream_length))
# st.write(bream_length)
# st.write(bream_weight)

fig, ax = plt.subplots(layout = 'constrained')  # tight_layout = True
plt.scatter(bream_length, bream_weight, color = 'red')
plt.scatter(smelt_length, smelt_weight)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.pyplot(fig)

# img = cv.imread('girl_laughing.jpg')
# if img is None:
#     sys.exit('파일을 찾을 수 없습니다.')

# print(type(img))
# st.write(type(img))
# img.shape

# st.write(img[:, :, 0])

# # img[:, :, 2] = 0
# st.image(img, 'tddt221')
# # cv.imshow('girl', img)

# cv.waitKey()
# cv.destroyAllWindows()

# # df = pd.read_csv('rollercoasters.csv')
# # # df.info()
# # df.shape
# # print(df.head(10))
# # # print(df.describe())

# # df
# # # st.dataframe(df.info())

