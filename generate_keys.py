import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ['Babu Sabu', 'Shona Vona']
usernames = ["bsanu","Svona"]
passwords = ["00100", "11011"]
#passwords = ["xxxxx","xxxxx"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent/"hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)