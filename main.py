import streamlit as st

st.title("🎉 テスト成功！")
st.write("ゆうへいの Streamlit テストアプリです。")

name = st.text_input("名前を入力して")
if name:
    st.success(f"{name} さん、こんにちは！😄")