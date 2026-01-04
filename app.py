import streamlit as st
from auth import check_password

# ===============================
# إعدادات الصفحة
# ===============================
st.set_page_config(
    page_title="EGISF Smart Governance App",
    layout="centered"
)

# ===============================
# حماية الدخول
# ===============================
if not check_password():
    st.stop()

# ===============================
# العنوان
# ===============================
st.title("EGISF – Smart Feasibility Model (SFM)")
st.subheader("Luxury · Unique · Value")

st.markdown("""
هذا النموذج هو النسخة التشغيلية الأولى من  
**نموذج الجدوى الذكية (SFM)**  
ويعتمد على إدخال يدوي كامل للأرقام والأوزان  
لضمان المرونة السيادية في اتخاذ القرار.
""")

st.markdown("---")

# ===============================
# إدخال القيم
# ===============================
st.header("🔢 إدخال الدرجات")

economic = st.number_input(
    "الدرجة الاقتصادية (0 – 100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

social = st.number_input(
    "الدرجة الاجتماعية (0 – 100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

environmental = st.number_input(
    "الدرجة البيئية (0 – 100)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

st.markdown("---")

# ===============================
# إدخال الأوزان
# ===============================
st.header("⚖️ إدخال الأوزان (يجب أن يكون المجموع = 1.00)")

weight_economic = st.number_input(
    "وزن البُعد الاقتصادي",
    min_value=0.0,
    max_value=1.0,
    value=0.40,
    step=0.05
)

weight_social = st.number_input(
    "وزن البُعد الاجتماعي",
    min_value=0.0,
    max_value=1.0,
    value=0.30,
    step=0.05
)

weight_environmental = st.number_input(
    "وزن البُعد البيئي",
    min_value=0.0,
    max_value=1.0,
    value=0.30,
    step=0.05
)

total_weight = round(
    weight_economic + weight_social + weight_environmental, 2
)

st.markdown(f"""
**مجموع الأوزان الحالي:** `{total_weight}`
""")

# ===============================
# التحقق من المنطق
# ===============================
if total_weight != 1.00:
    st.error("❌ مجموع الأوزان يجب أن يساوي 1.00 بالضبط")
    st.stop()

st.success("✔️ الأوزان سليمة – يمكن الحساب")

st.markdown("---")

# ===============================
# الحساب
# ===============================
sfm_score = (
    economic * weight_economic +
    social * weight_social +
    environmental * weight_environmental
)

sfm_score = round(sfm_score, 2)

# ===============================
# النتيجة
# ===============================
st.header("📊 النتيجة")

st.metric("Smart Feasibility Score (SFM)", f"{sfm_score} / 100")

# ===============================
# منطق القرار
# ===============================
if sfm_score >= 70:
    decision = "GO ✅"
    explanation = "المشروع يحقق جدوى ذكية مرتفعة ويُنصح بالاستمرار."
    color = "green"
elif sfm_score >= 50:
    decision = "REVIEW ⚠️"
    explanation = "المشروع يحتاج مراجعة وتحسين قبل اتخاذ القرار."
    color = "orange"
else:
    decision = "STOP ❌"
    explanation = "المشروع لا يحقق الحد الأدنى من الجدوى الذكية."
    color = "red"

st.markdown(f"""
### 🧭 القرار النهائي
<span style="color:{color}; font-size:22px;"><strong>{decision}</strong></span>

{explanation}
""", unsafe_allow_html=True)

st.markdown("---")

# ===============================
# شفافية المنطق
# ===============================
st.markdown(f"""
### 🧠 منطق الحساب المستخدم

**SFM =**  
({economic} × {weight_economic})  
+ ({social} × {weight_social})  
+ ({environmental} × {weight_environmental})

> مجموع الأوزان = **1.00**
""")
