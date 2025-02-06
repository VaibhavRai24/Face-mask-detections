# Face Mask Detection System

## 📋 **Project Overview**
This project is a deep learning-based face mask detection system designed to identify whether a person is wearing a face mask or not. The system can be used for applications such as access control, public safety monitoring, and smart surveillance.

---
## 🎯 **Key Features**
- **Real-Time Detection:** Identifies face masks from live video streams or static images.
- **Deep Learning Model:** Utilizes advanced deep learning techniques for accurate predictions.
- **Binary Classification:** Outputs "Mask" or "No Mask" labels.

---
## 🛠 **Technologies Used**
- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow/Keras
- **Data Processing:** OpenCV, NumPy
- **Model Architecture:** CNN (Convolutional Neural Network)

---
## 📂 **Project Structure**
```
|-- face_mask_detection_project
    |-- data/                    # Dataset files
    |-- models/                  # Trained CNN models
    |-- app.py                   # Main application file
    |-- requirements.txt         # Python package requirements
    |-- README.md                # Project documentation
```
---
## ⚙️ **Setup and Installation**

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd face_mask_detection_project
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows, use env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

---
## 🚀 **How to Use**
1. **Run the application:** Start the detection system using the terminal.
2. **Input data:** Provide live video feed or static images for mask detection.
3. **View results:** Get real-time detection output with "Mask" or "No Mask" labels.

---
## 🤖 **Model Details**
- **Dataset:** Custom dataset with images of masked and unmasked faces.
- **Model Architecture:** Convolutional Neural Network (CNN) with multiple layers for feature extraction.
- **Training:** Model trained with TensorFlow/Keras on a balanced dataset for high accuracy.
- **Evaluation:** Achieved high accuracy on the test set.

---
## 📊 **Sample Outputs**
### Example:
- **Input:** Image of a person wearing a face mask
- **Predicted Label:** Mask

### Example:
- **Input:** Image of a person without a face mask
- **Predicted Label:** No Mask

---
## 🏆 **Future Enhancements**
- Deployment on edge devices for real-time detection.
- Model optimization for faster inference.
- Improved detection under various lighting conditions.

---
## 🤝 **Contributions**
Contributions are welcome! Feel free to submit a pull request or open an issue.

---
## 📄 **License**
This project is licensed under the MIT License.
