import streamlit as st
import joblib
import pandas as pd
import os
print("Current working directory:", os.getcwd())

# ============================================================
# Load Model & Vectorizer (pakai path relatif)
# ============================================================
base_dir = os.path.dirname(__file__)
model = joblib.load(os.path.join(base_dir, "yelp_sentiment_model.joblib"))
vectorizer = joblib.load(os.path.join(base_dir, "yelp_tfidf_vectorizer.joblib"))

# ============================================================
# Judul Aplikasi
# ============================================================
st.title("🍔🍕 Ulasan Produk")
st.write("Masukkan ulasan anda")

# ============================================================
# Input Teks
# ============================================================
user_input = st.text_area("Masukkan Review", "")

# ============================================================
# Prediksi
# ============================================================
if st.button("Prediksi"):
    if user_input.strip() != "":
        # Transform input
        user_vec = vectorizer.transform([user_input])
        prediction = model.predict(user_vec)[0]
        probabilities = model.predict_proba(user_vec)[0]

        # Hasil Prediksi
        st.subheader("Hasil Prediksi:")
        st.write(f"**Sentimen:** {prediction}")

        # Probabilitas
        st.subheader("Probabilitas:")
        labels = model.classes_
        prob_dict = {labels[i]: round(probabilities[i], 3) for i in range(len(labels))}
        st.write(prob_dict)

        # Visualisasi Bar Chart
        proba_df = pd.DataFrame([prob_dict])
        st.bar_chart(proba_df.T)

        # Tambahkan respon chatbot
        st.subheader("Respon Chatbot:")
        if prediction == "positive":
            st.success("😊 Terima kasih atas ulasannya! Senang mendengar pengalaman positif Anda.")
        elif prediction == "negative":
            st.error("😔 Mohon maaf atas pengalaman yang mengecewakan. Kami akan segera menindaklanjuti.")
        else:
            st.info("🙂 Terima kasih atas masukannya. Kami akan pertimbangkan untuk meningkatkan layanan kami.")
    else:
        st.warning("Harap masukkan review terlebih dahulu.")
# cd "C:\Users\HYPE AMD\latihan" 
# python -m streamlit run coba/project3.py
