# 📊 Number Classification API

This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from the Numbers API.

## 🚀 Features
- Checks if a number is **prime**, **perfect**, or an **Armstrong number**
- Identifies if a number is **odd** or **even**
- Computes the **sum of digits** of the number
- Fetches a **fun fact** about the number from the Numbers API
- Returns results in **JSON format**
- Handles **CORS (Cross-Origin Resource Sharing)**
- Provides proper **error handling**

---

## 🏗️ Technology Stack
- **Python 3.x**
- **Flask** (Web framework)
- **Flask-CORS** (For handling CORS)
- **Requests** (For fetching fun facts from the Numbers API)

---

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Fola-Git/number-classification-api.git
cd number-classification-api
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the API
```sh
python app.py
```
The server should now be running on **http://127.0.0.1:5000**

---

## 📡 API Usage

### 🎯 **Endpoint:**
```http
GET /api/classify-number?number=<integer>
```

### ✅ **Success Response (200 OK)**
**Example Request:**
```http
GET http://127.0.0.1:5000/api/classify-number?number=371
```

**Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

### ❌ **Error Response (400 Bad Request)**
**Example Request:**
```http
GET http://127.0.0.1:5000/api/classify-number?number=abc
```

**Response:**
```json
{
    "number": "abc",
    "error": true
}
```

---

## 🚀 Deployment
This API can be deployed on:
- **Heroku**
- **Render**
- **Railway**
- **Fly.io**
- **AWS/GCP/Azure**

---

## 👨‍💻 Author
Developed by **STARR**  
LinkedIn: [Folashade Oroge](https://linkedin.com/in/folashadeoluwaseun)  
GitHub: [Fola-Git](https://github.com/Fola-Giit)

