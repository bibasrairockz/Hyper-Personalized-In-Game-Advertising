import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader


#---user authenticator
names = ['Babu Sabu', 'Shona Vona']
usernames = ["bsanu","Svona"]
# dict1 = {}

# for key in usernames:
#     for value in names:
#         dict1[key] = value
#         names.remove(value)
#         break 
# print(dict1)
# load passwords
# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

file_path = Path(__file__).parent / "config.yaml"
with open(file_path) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'])

name, authentication_status, username = authenticator.login()

if authentication_status==False:
    st.error("username/password is incorrect")

if authentication_status==None:
    st.warning("Please enter username and password")

if authentication_status:
    authenticator.logout("Logout","sidebar")
    st.sidebar.title(f"Welcome {name}")
    # st.video(["newf.mp4","new.mp4"])
    # st.video("newf.mp4", width=200)
    # st.video("new.mp4")
    cols = st.columns(2)

    with cols[0]: st.video("newf.mp4", start_time=1)
    with cols[1]: st.video("new.mp4", start_time=1)  

    if st.button("Play all videos", use_container_width=True):
        st.components.v1.html(
            """<script>
            let videos = parent.document.querySelectorAll("video");
            videos.forEach(v => {
                v.play();
            })
            </script>""", 
            width=0, height=0
        )
