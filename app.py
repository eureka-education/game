import streamlit as st
import random

# セッションステートを使ってスコアとターゲット位置を記録
if 'score' not in st.session_state:
    st.session_state.score = 0

if 'target_position' not in st.session_state:
    st.session_state.target_position = random.randint(1, 10)

# ゲームのタイトル
st.title("クリックターゲットゲーム")

# スコアを表示
st.write(f"スコア: {st.session_state.score}")

# ランダムな位置にターゲットを配置
target_position = st.session_state.target_position

# ボタンを作成して、ターゲットの位置に合わせる
for i in range(1, 11):
    if i == target_position:
        if st.button(f"クリックして得点 {i}"):
            st.session_state.score += 1
            # ターゲットを新しい位置に移動
            st.session_state.target_position = random.randint(1, 10)
            st.experimental_rerun()  # リフレッシュしてターゲットを移動
    else:
        st.button(f"ボタン {i}")  # クリックできないボタン
