import streamlit as st

PROJECT_PASSWORD = "EGISF2026"

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.title("🔒 Secure Project Access")

        password = st.text_input(
            "Enter Project Password",
            type="password"
        )

        if st.button("Login"):
            if password == PROJECT_PASSWORD:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Incorrect password")

        return False

    return True
