import streamlit as st
import pandas as pd

st.set_page_config(page_title="معرض أنطاليا", layout="centered")
st.title("🏗️ معرض أنطاليا للسيراميك")

menu = st.sidebar.selectbox("القائمة", ["المخزن", "المبيعات"])

if 'products' not in st.session_state:
    st.session_state.products = pd.DataFrame(columns=['الاسم', 'السعر', 'الكمية'])

if menu == "المخزن":
    st.header("📦 إضافة منتج")
    name = st.text_input("اسم المنتج")
    price = st.number_input("السعر")
    qty = st.number_input("الكمية", step=1)
    if st.button("حفظ"):
        new_row = pd.DataFrame([[name, price, qty]], columns=['الاسم', 'السعر', 'الكمية'])
        st.session_state.products = pd.concat([st.session_state.products, new_row], ignore_index=True)
        st.success("تم الحفظ!")
    st.dataframe(st.session_state.products)
else:
    st.header("💰 تسجيل بيع")
    st.write("نظام المبيعات قيد التطوير...")
