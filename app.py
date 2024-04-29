# streamlitをインポート
import streamlit as st
import random

# セッションステートを使用して、ターゲット番号と推測回数を記録
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.correct = False

# ゲームのタイトル
st.title("数当てゲーム")

# ユーザーに推測を入力してもらう
guess = st.number_input("1から100までの数を推測してください", min_value=1, max_value=100, step=1)

# 推測ボタン
if st.button("推測"):
    # 推測回数を増やす
    st.session_state.guesses += 1
    
    # ユーザーの推測がターゲットに近いかどうかをチェック
    if guess < st.session_state.target:
        st.write("小さすぎます！")
    elif guess > st.session_state.target:
        st.write("大きすぎます！")
    else:
        st.write("正解！")
        st.write(f"推測回数: {st.session_state.guesses}")
        st.session_state.correct = True

# ゲームをリセットするボタン
if st.session_state.correct and st.button("ゲームをリセット"):
    st.session_state.target = random.randint(1, 100)
    st.session_state.guesses = 0
    st.session_state.correct = False
