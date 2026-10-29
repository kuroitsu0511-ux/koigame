import streamlit as st

# ページの設定
st.set_page_config(page_title="君と紡ぐ三叉路", page_icon="🌸", layout="centered")

# セッション状態の初期化
if "stage" not in st.session_state:
    st.session_state.stage = "input_name"
    st.session_state.player_name = "翔太"
    st.session_state.aoi_hearts = 2
    st.session_state.rin_hearts = 2
    st.session_state.charm = 1
    st.session_state.intelligence = 1

st.title("✨ 恋愛シミュレーション『君と紡ぐ三叉路』")
st.markdown("---")

# サイドバー（ステータス表示）
with st.sidebar:
    st.markdown("### 【 ステータス 】")
    st.write(f"**名前:** {st.session_state.player_name}")
    st.write(f"**あおいの好感度:** {'♥' * max(0, st.session_state.aoi_hearts)} ({st.session_state.aoi_hearts})")
    st.write(f"**凛の好感度:** {'♥' * max(0, st.session_state.rin_hearts)} ({st.session_state.rin_hearts})")
    st.write(f"**魅力:** {st.session_state.charm}")
    st.write(f"**知性:** {st.session_state.intelligence}")

# 【ステージ0：名前入力】
if st.session_state.stage == "input_name":
    st.subheader("主人公の設定")
    name_input = st.text_input("あなたの名前を入力してください", value="翔太")
    
    if st.button("ゲームスタート"):
        st.session_state.player_name = name_input if name_input else "翔太"
        st.session_state.stage = "chapter1"
        st.rerun()

# 【ステージ1：チャプター1】
elif st.session_state.stage == "chapter1":
    p_name = st.session_state.player_name
    st.subheader("Chapter 1：委員会決めと放課後")
    st.write(f"🌸 ――春、高校2年生の新学期。{p_name}の新しい青春が始まる。")
    st.write("教室に入ると、幼馴染の『あおい』が笑顔で手を振ってきた。その隣には転校生の『凛』が座っている。")
    st.write("図書委員の仕事中、あおいは荷物でフラつき、凛は本棚に手が届かず困っている。")

    choice1 = st.radio(
        "行動を選んでください：",
        [
            "1: あおいの荷物を手伝う（あおい重視）",
            "2: 凛の高いところの本を取る（凛重視）",
            "3: 2人ともテキパキ手伝う（魅力・知性アップ）",
            "4: 自分の作業に没頭する（知性大幅アップ）"
        ],
        key="c1"
    )

    if st.button("決定する"):
        if "1:" in choice1:
            st.session_state.aoi_hearts += 2
            st.session_state.charm += 1
            st.success(">> あおい「ありがと！やっぱり頼りになるね♪」")
        elif "2:" in choice1:
            st.session_state.rin_hearts += 2
            st.session_state.charm += 1
            st.success(">> 凛「あ…ありがとう。親切なのね…」")
        elif "3:" in choice1:
            st.session_state.aoi_hearts += 1
            st.session_state.rin_hearts += 1
            st.session_state.charm += 2
            st.success(">> 2人ともあなたの手際に感心した様子だ！")
        else:
            st.session_state.intelligence += 3
            st.success(">> 一人で黙々と作業をこなし、知識が深まった！")
        
        st.session_state.stage = "chapter2"
        st.rerun()

# 【ステージ2：チャプター2】
elif st.session_state.stage == "chapter2":
    st.subheader("Chapter 2：夏休みの花火大会")
    st.write("🎆 浴衣姿のあおいと凛から、まさかの同じ時間帯に一緒に行こうと誘われた！")

    choice2 = st.radio(
        "誰と行く？",
        [
            "1: あおいとの約束を優先する",
            "2: 凛との約束を優先する",
            "3: 「3人で一緒に行こう！」と提案する",
            "4: どちらも断って家で過ごす"
        ],
        key="c2"
    )

    if st.button("決定する"):
        if "1:" in choice2:
            st.session_state.aoi_hearts += 3
            st.session_state.rin_hearts -= 2
        elif "2:" in choice2:
            st.session_state.rin_hearts += 3
            st.session_state.aoi_hearts -= 2
        elif "3:" in choice2:
            if st.session_state.charm >= 2:
                st.session_state.aoi_hearts += 1
                st.session_state.rin_hearts += 1
            else:
                st.session_state.aoi_hearts -= 2
                st.session_state.rin_hearts -= 2
        else:
            st.session_state.aoi_hearts = 0
            st.session_state.rin_hearts = 0

        st.session_state.stage = "ending"
        st.rerun()

# 【ステージ3：エンディング】
elif st.session_state.stage == "ending":
    st.subheader("――そして、卒業式へ――")
    
    aoi = st.session_state.aoi_hearts
    rin = st.session_state.rin_hearts
    charm = st.session_state.charm

    if aoi >= 4 and rin >= 4 and charm >= 2:
        st.success("💎 【超合格：伝説のハーレム・ハーモニー END】\n\nあおい＆凛「これからも3人でずっと一緒にいましょう？」\n圧倒的な魅力で最高の結末を迎えた！")
    elif aoi >= 4 and aoi > rin:
        st.success("🌸 【合格：あおい True END『桜色の誓い』】\n\nあおい「ずっと言えなかったけど…好き！」\n幼馴染から大切なパートナーへ！")
    elif rin >= 4 and rin > aoi:
        st.info("❄️ 【合格：凛 True END『雪解けの微笑み』】\n\n凛「私を、あなたの特別な人にさせて？」\nクールな凛の心を開いた！")
    else:
        st.error("💔 【不合格：孤独な結末】\n\n誰とも深い関係を築けないまま卒業を迎えてしまった……。")

    if st.button("もう一度遊ぶ"):
        st.session_state.stage = "input_name"
        st.session_state.aoi_hearts = 2
        st.session_state.rin_hearts = 2
        st.session_state.charm = 1
        st.session_state.intelligence = 1
        st.rerun()
