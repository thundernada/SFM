import streamlit as st

# ===============================
# إعدادات الصفحة
# ===============================
st.set_page_config(
    page_title="EGISF Smart Governance App",
    layout="centered"
)

# ===============================
# حماية الدخول (بدون auth.py)
# ===============================
PROJECT_PASSWORD = "EGISF2026"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 Secure Project Access")

    password = st.text_input("Enter Project Password", type="password")

    if st.button("Login"):
        if password == PROJECT_PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Incorrect password")

    st.stop()

# ===============================
# العنوان
# ===============================
st.title("EGISF – Smart Feasibility Model (SFM)")
st.subheader("Luxury · Unique · Value")

st.markdown("""
هذا النموذج هو النسخة التشغيلية الأولى من  
**نموذج الجدوى الذكية (SFM)**  
ويعتمد على إدخال يدوي كامل للأرقام والأوزان.
""")

st.markdown("---")

# ===============================
# إدخال القيم
# ===============================
st.header("🔢 إدخال الدرجات")

economic = st.number_input("الدرجة الاقتصادية (0 – 100)", 0.0, 100.0, 50.0)
social = st.number_input("الدرجة الاجتماعية (0 – 100)", 0.0, 100.0, 50.0)
environmental = st.number_input("الدرجة البيئية (0 – 100)", 0.0, 100.0, 50.0)

st.markdown("---")

# ===============================
# إدخال الأوزان
# ===============================
st.header("⚖️ إدخال الأوزان (المجموع = 1.00)")

w_e = st.number_input("وزن البُعد الاقتصادي", 0.0, 1.0, 0.4, 0.05)
w_s = st.number_input("وزن البُعد الاجتماعي", 0.0, 1.0, 0.3, 0.05)
w_env = st.number_input("وزن البُعد البيئي", 0.0, 1.0, 0.3, 0.05)

total = round(w_e + w_s + w_env, 2)
st.write(f"**مجموع الأوزان:** {total}")

if total != 1.0:
    st.error("❌ مجموع الأوزان يجب أن يساوي 1.00")
    st.stop()

st.success("✔️ الأوزان سليمة")

st.markdown("---")

# ===============================
# الحساب
# ===============================
sfm = round(
    economic * w_e +
    social * w_s +
    environmental * w_env,
    2
)

st.header("📊 النتيجة")
st.metric("SFM Score", f"{sfm} / 100")

# ===============================
# القرار
# ===============================
if sfm >= 70:
    decision = "GO ✅"
    explanation = "المشروع يحقق جدوى ذكية مرتفعة."
    color = "green"
elif sfm >= 50:
    decision = "REVIEW ⚠️"
    explanation = "المشروع يحتاج مراجعة."
    color = "orange"
else:
    decision = "STOP ❌"
    explanation = "المشروع غير مجدي حاليًا."
    color = "red"

st.markdown(
    f"<h3 style='color:{color}'>{decision}</h3><p>{explanation}</p>",
    unsafe_allow_html=True
)
