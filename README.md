 
#  Loan Approval Predictor

A machine learning-powered web application that predicts loan approval likelihood with **85% accuracy** based on user financial profiles. Built with Python (Flask), HTML/CSS, and deployed on Render.

🌐 [Visit site](https://loan-approval-prediction-huo2.onrender.com)

---

##  Features

-  **Instant predictions** using a trained ML model  
-  **User-friendly interface** with responsive design  
-  **Key decision factors** visualization  
-  **EMI calculator** for approved loans  
-  **85% prediction accuracy** on test data  
-  **Google Colab Notebook** for model training and exploration  

---

##  Colab Notebook

The training and evaluation of the machine learning model was done in a **Google Colab notebook** for easy experimentation, reproducibility, and sharing.

**Key contents:**
- Data cleaning & preprocessing  
- Feature engineering  
- Model training (Logistic Regression)  
- Accuracy evaluation  
- Model export to `model.pkl`

---

##  Tech Stack

| Component        | Technology               |
|------------------|---------------------------|
| **Frontend**      | HTML5, CSS3, Tailwind CSS |
| **Backend**       | Python (Flask)            |
| **ML Framework**  | Scikit-learn              |
| **Deployment**    | Render                    |
| **Notebook**      | Google Colab              |
| **Version Control** | GitHub                 |

---

##  How It Works

1. User submits financial details via a web form  
2. Flask backend processes the input and passes it to the trained ML model  
3. Model predicts loan approval (`Approved` or `Not Approved`)  
4. If approved, EMI breakdown is shown  

---

##  Deployment on Render

###  Prerequisites
- GitHub account with this repository
- Render account (free tier works)

###  Steps

```bash
# Clone this repo
git clone https://github.com/yourusername/loan-approval-predictor.git
````

* Connect your GitHub repo to Render
* Choose Python environment
* Set build command: `pip install -r requirements.txt`
* Set start command: `gunicorn app:app`
* Deploy!

###  Auto-Deploy

Enabled by default in Render. Any push to the `main` branch triggers auto redeploy.

---

##  File Structure

```
loan-approval-predictor/
├── app.py                  # Flask app
├── model/
│   └── loan_model.pkl      # Trained ML model
├── templates/
│   ├── index.html          # Input form
│   └── result.html         # Results page
├── static/
│   └── style.css           # Styling
├── Loan_Approval_Model.ipynb  # Colab notebook
├── requirements.txt        # Python dependencies
└── .gitignore              # Git ignore rules
```

---

##  Running Locally

```bash
# 1. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate    # For macOS/Linux
venv\Scripts\activate       # For Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

Visit `http://localhost:5000` in your browser.

---

##  Contributors

* [Soumya Jain](https://github.com/soumya-xy)
* [Mehul Shah](https://github.com/shahmehul2005)
* [Bhavishya Jain](https://github.com/Bhavishya011)

---

 
