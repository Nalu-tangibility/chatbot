import streamlit as st

st.title("🧠 Psychological Distance Simulator")

st.markdown("""
このツールでは、心理的距離（x）を以下の数式でシミュレーションします：

\[
x = \frac{1}{\sum_{i=1}^{n} w_i z_i}
\]

※ 全ての \( w_i \) の合計は1である必要があります。
""")

# 初期構成
num_factors = st.slider("要素の数（n）", min_value=1, max_value=10, value=3)

weights = []
scores = []

total_weight = 0.0
st.subheader("🔧 各要素の設定")

for i in range(num_factors):
    st.markdown(f"### 要素 {i+1}")
    w = st.number_input(f"重み w{i+1}", min_value=0.0, max_value=1.0, step=0.01, key=f"w{i}")
    z = st.number_input(f"スコア z{i+1}", min_value=0.0, step=0.1, key=f"z{i}")
    weights.append(w)
    scores.append(z)
    total_weight += w

if total_weight == 0:
    st.warning("重みの合計が0です。少なくとも1つの重みを設定してください。")
elif abs(total_weight - 1.0) > 0.01:
    st.error("重みの合計は1にしてください。現在の合計: {:.3f}".format(total_weight))
else:
    weighted_sum = sum(w * z for w, z in zip(weights, scores))
    if weighted_sum == 0:
        st.error("加重和が0のため、心理的距離は定義できません。")
    else:
        x = 1 / weighted_sum
        st.success(f"心理的距離 x の値: **{x:.3f}**")

        # optional: グラフ表示
        st.bar_chart({"weighted factors": [w * z for w, z in zip(weights, scores)]})
