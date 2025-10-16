
## ▶️ How to Run Locally
1. Aktifkan virtual environment:
     .venv\Scripts\activate

2. Install dependensi:
     pip install -r requirements.txt

3. Jalankan Streamlit:
     streamlit run app.py


## 📚 Model Info
Model dilatih menggunakan data review Yelp dengan TF-IDF vectorizer dan Logistic Regression. File model dan vectorizer disimpan sebagai `.joblib` dan diload langsung di `app.py`.

## ⚠️ Notes
- Pastikan semua file `.joblib` ada di folder yang sama dengan `app.py`
- Gunakan path dinamis agar tidak error saat pindah folder atau deploy

## ✍️ Author
Bayan — [LinkedIn](https://www.linkedin.com/in/your-profile)  
Feel free to fork, star, or contribute!
## Link deploy
https://deploy-vfapp589zx4emh6rdt8w9sw.streamlit.app/