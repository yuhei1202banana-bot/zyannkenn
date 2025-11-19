import streamlit as st
import random

st.title("じゃんけんゲーム")

hands = ["グー", "チョキ", "パー"]

player = st.radio("出す手を選んでください", hands)
ai = random.choice(hands)

if st.button("勝負！"):
    st.write(f"あなた：**{player}**")
    st.write(f"コンピュータ：**{ai}**")

    if player == ai:
        st.warning("あいこです！")
    elif (player == "グー" and ai == "チョキ") or \
         (player == "チョキ" and ai == "パー") or \
         (player == "パー" and ai == "グー"):
        st.success("あなたの勝ち！")
    else:
        st.error("あなたの負け…")