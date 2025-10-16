# 🧠 Yelp Sentiment Analysis App

A simple Streamlit web app that performs **sentiment analysis** on Yelp-style text reviews using a pre-trained machine learning model. The app classifies input text as **positive** or **negative** sentiment.

## 🚀 Demo
👉 [Live App on Streamlit Cloud]: https://deploy-vfapp589zx4emh6rdt8w9sw.streamlit.app/  


## 📦 Features
- Real-time sentiment prediction
- Clean and responsive Streamlit UI
- Pre-trained model loaded from `.joblib`
- Easy to extend with your own dataset or model

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- Joblib
- Pandas / NumPy

## 📁 Project Structure
📦 yelp-sentiment-app/ ├── app.py ├── yelp_sentiment_model.joblib ├── vectorizer.joblib ├── requirements.txt └── README.md



## ▶️ How to Run Locally
1. Activate your virtual environment:
     .venv\Scripts\activate

2. Install dependensi:
     pip install -r requirements.txt

3. Launch the app:
     streamlit run app.py


## 📚 Model Info
Model dilatih menggunakan data review Yelp dengan TF-IDF vectorizer dan Logistic Regression. File 
## 📚 Model Info
The model was trained on Yelp review data using a TF-IDF vectorizer and Logistic Regression classifier. Both the model and vectorizer are saved as `.joblib` files and loaded directly in `app.py`.

## ⚠️ Notes
- Ensure all `.joblib` files are in the same folder as `app.py`
- Use dynamic paths to avoid errors when moving folders or deploying

## ✍️ Author
**Bayan** — [LinkedIn](https://www.linkedin.com/in/your-profile)  
Feel free to fork, star, or contribute!
