import streamlit as st

st.set_page_config(page_title="أكلنا الصحي", layout="wide")

st.title("🍽️ أكلنا الصحي - تطبيق السعرات")
st.write("هذا التطبيق يعرض أكلات عراقية صحية مع معلوماتها الغذائية والسعرات الحرارية.")

# بيانات الأكلات
meals = [
    {
        "name": "شوربة عدس",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Lentil_soup.jpg/800px-Lentil_soup.jpg",
        "calories": 180,
        "protein": "12g",
        "fat": "5g",
        "carbs": "22g"
    },
    {
        "name": "تبولة",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Tabbouleh-20050816.jpg/800px-Tabbouleh-20050816.jpg",
        "calories": 120,
        "protein": "3g",
        "fat": "4g",
        "carbs": "18g"
    },
    {
        "name": "دجاج مشوي",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Chicken_on_a_grill.jpg/800px-Chicken_on_a_grill.jpg",
        "calories": 250,
        "protein": "30g",
        "fat": "10g",
        "carbs": "0g"
    }
]

# عرض الأكلات
for meal in meals:
    st.header(f"🍴 {meal['name']}")
    st.image(meal["image"], width=300)
    st.markdown(f"""
    **السعرات:** {meal['calories']} kcal  
    **بروتين:** {meal['protein']}  
    **دهون:** {meal['fat']}  
    **كاربوهيدرات:** {meal['carbs']}  
    """)

    st.markdown("---")
