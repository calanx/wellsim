import datetime
import pickle

import requests
import streamlit as st


headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.atyarisi.com/"}
url = "https://tjkbulten.atyarisi.com/api/v7/GetPremadeSharedCoupon"


st.title("Hello World!")


col1, col2 = st.columns(2)

date = datetime.date.today().strftime("%Y-%m-%d")

with col1:
    if st.button("GO Today"):
        
        params = {"playableStatus": 0, "raceNo": 0, "order": 1, "isOnlyMemberCoupon": "false", "pageNumber": 1, "pageSize": 1, "date": date}
    
        data = requests.get(url, params=params, headers=headers).json()
        for h in data["d"]["hippodromes"]:
            st.write(f'{h["programId"]} - {h["name"]}')


with col2:
    user_input = st.text_input("Input")
    if st.button("Create pickle"):
        # Replace this with your function and its result.
       
        

         params = {
             "playableStatus": 0, "raceNo": 0, "order": 1,
             "isOnlyMemberCoupon": "false", "programId": user_input,
             "pageNumber": 1, "pageSize": 999, "date": date
         }
         data = requests.get(url, params=params, headers=headers).json()
         
         st.session_state["pickle_data"] = pickle.dumps(data)



    if "pickle_data" in st.session_state:
        st.download_button(
            "Download pickle",
            data=st.session_state["pickle_data"],
            file_name=user_input,
            mime="application/octet-stream",
        )
