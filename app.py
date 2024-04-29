import streamlit as st
import random
import time

# ゲームの状態をセッションステートで管理
if 'start_time' not in st.session_state:
    # ゲーム開始時に開始時間を記録
    st.session_state.start_time = time.time()
    st.session_state.score = 0
    st.session_state.target_position = random.randint(1, 10)
    st.session_state.game_over = False

# タイムリミット
TIME_LIMIT = 30  # 30秒

# 現在の時間と経過時間を計算
current_time = time.time()
elapsed_time = current_time - st.session_state.start_time

# ゲームが終了したかどうかを確認
if elapsed_time >= TIME_LIMIT:
    st.session_state.game_over = True

# ゲームのタイトル
st.title("30秒のターゲットクリックゲーム")

# 残り時間を表示
if not st.session_state.game_over:
    st.write(f"残り時間: {TIME_LIMIT - int(elapsed_time)}秒")
else:
    st.write("時間切れ！ ゲームオーバー")
    st.write(f"最終スコア: {st.session_state.score}")

# ターゲットをクリックしてスコアを増やす
if not st.session_state.game_over:
    target_position = st.session_state.target_position
    for i in range(1, 11):
        if i == target_position:
            if st.button(f"クリックして得点 {i}"):
                st.session_state.score += 1
                # ターゲットを新しい位置に移動
                st.session_state.target_position = random.randint(1, 10)
                st.experimental_rerun()  # リフレッシュしてターゲットを移動
        else:
            st.button(f"ボタン {i}")  # クリックできないボタン

# ゲームをリセットして再スタートするオプション
if st.session_state.game_over and st.button("リスタート"):
    st.session_state.start_time = time.time()  # 新しいゲーム開始時間
    st.session_state.score = 0  # スコアリセット
    st.session_state.target_position = random.randint(1, 10)  # ランダムなターゲット位置
    st.session_state.game_over = False  # ゲームオーバー解除
