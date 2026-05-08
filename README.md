# 🧠 Brain-Tumor-MRI-Classificationised Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-DeepLearning-red)
![MobileNetV2](https://img.shields.io/badge/Model-MobileNetV2-green)
![Accuracy](https://img.shields.io/badge/Accuracy-90%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A professional deep learning-based medical imaging project focused on the classification of brain tumors from MRI scans using Convolutional Neural Networks (CNNs) and Transfer Learning with MobileNetV2.

This project classifies MRI images into four categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor (`notumor`)

The model was developed using TensorFlow/Keras and trained on MRI image datasets with advanced regularization and augmentation techniques to improve performance and reduce overfitting.

---

# 📚 Table of Contents

* [Project Overview](#-project-overview)
* [Project Highlights](#-project-highlights)
* [Dataset Information](#-dataset-information)
* [Model Architecture](#-model-architecture)
* [Training Methodology](#-training-methodology)
* [Performance Results](#-performance-results)
* [Project Structure](#-project-structure)
* [Installation & Setup](#-installation--setup)
* [How to Train the Model](#-how-to-train-the-model)
* [How to Run Predictions](#-how-to-run-predictions)
* [Sample Prediction Results](#-sample-prediction-results)
* [Future Improvements](#-future-improvements)
* [License](#-license)
* [Citation](#-citation)
* [Author](#-author)

---

# 🔍 Project Overview

Brain tumors are among the most critical neurological diseases requiring early and accurate diagnosis. Manual analysis of MRI scans is time-consuming and highly dependent on medical expertise.

This project leverages Deep Learning and Transfer Learning techniques to automate brain tumor classification from MRI images with high accuracy.

The final refined model uses:

* Transfer Learning with MobileNetV2
* Data Augmentation
* Batch Normalization
* Dropout Regularization
* L2 Regularization
* EarlyStopping
* ReduceLROnPlateau

to achieve robust performance on MRI image classification tasks.

---

# ✨ Project Highlights

✅ Multi-class Brain Tumor Classification
✅ Transfer Learning using MobileNetV2
✅ TensorFlow / Keras Implementation
✅ MRI Image Augmentation Pipeline
✅ Overfitting Reduction Techniques
✅ Advanced Model Regularization
✅ Google Colab Compatible
✅ Single Image Prediction Support
✅ Performance Visualization Graphs
✅ Medical Imaging Deep Learning Workflow

---

# 🗂 Dataset Information

## Primary Dataset

| Property        | Details                                |
| --------------- | -------------------------------------- |
| Dataset Type    | Brain MRI Images                       |
| Classes         | Glioma, Meningioma, Pituitary, Notumor |
| Training Images | ~5600                                  |
| Testing Images  | ~1600                                  |
| Source          | Google Drive MRI Dataset               |
| Image Type      | MRI Brain Scans                        |

### Dataset Structure

```bash
MRI SCAN DATASET/
│
├── Training/
│   ├── glioma/
│   ├── meningioma/
│   ├── pituitary/
│   └── notumor/
│
└── Testing/
    ├── glioma/
    ├── meningioma/
    ├── pituitary/
    └── notumor/
```

---

## Additional Dataset Attempt

### BraTS2020 Dataset

An attempt was made to integrate the BraTS2020 medical imaging dataset from Kaggle using NIfTI (.nii) medical image files.

Although the custom NIfTI data loading pipeline was partially implemented, the dataset was not successfully integrated into the final training workflow due to preprocessing and compatibility issues.

---

# 🏗 Model Architecture

## Initial Model

A custom CNN architecture was initially developed using:

* Convolution Layers
* MaxPooling
* Dense Layers
* Dropout Layers

---

## Final Refined Model

The final model uses:

# MobileNetV2 Transfer Learning Pipeline

### Architecture Features

* Pre-trained MobileNetV2 (ImageNet weights)
* Custom Classification Head
* Batch Normalization
* Dropout Regularization
* L2 Weight Regularization
* Fine-tuning Support

---

## 🧠 Architecture Diagram

> Add architecture diagram image here

```bash
Input MRI Image
       ↓
Data Augmentation
       ↓
MobileNetV2 Base Model
       ↓
Global Average Pooling
       ↓
Batch Normalization
       ↓
Dense Layer + ReLU
       ↓
Dropout
       ↓
Softmax Output Layer
       ↓
Predicted Tumor Class
```

---

# ⚙ Training Methodology

## Data Augmentation Techniques

The following augmentation techniques were used:

* Rotation
* Width Shift
* Height Shift
* Shearing
* Zooming
* Horizontal Flipping
* Rescaling

---

## Regularization Techniques

To improve generalization and reduce overfitting:

* Dropout Layers
* Batch Normalization
* L2 Regularization
* EarlyStopping Callback
* ReduceLROnPlateau Callback

---

## Training Configuration

| Parameter      | Value                    |
| -------------- | ------------------------ |
| Framework      | TensorFlow / Keras       |
| Base Model     | MobileNetV2              |
| Epochs         | 30                       |
| Image Size     | 224 × 224                |
| Optimizer      | Adam                     |
| Loss Function  | Categorical Crossentropy |
| Output Classes | 4                        |

---

# 📈 Performance Results

## Final Refined Model Performance

| Metric         | Value  |
| -------------- | ------ |
| Test Accuracy  | ~90%   |
| Test Loss      | 0.5269 |
| Epochs Trained | 30     |

---

## 📊 Training Visualization

### Accuracy Plot

> Add `accuracy_plot.png` here

### Loss Plot

> Add `loss_plot.png` here

---

# 📁 Project Structure

```bash
Brain-Tumor-MRI-Classificationised-Prediction/
│
├── notebooks/
│   └── brain_tumor_classification.ipynb
│
├── models/
│   └── cnn_cancer_prediction_model_refined.keras
│
├── outputs/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── predictions/
│
├── dataset/
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# 💻 Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/BasimHassan2008/Brain-Tumor-MRI-Classificationised-Prediction.git
```

```bash
cd Brain-Tumor-MRI-Classificationised-Prediction
```

---

## 2. Install Dependencies

```bash
pip install tensorflow keras numpy matplotlib seaborn scikit-learn kaggle nibabel tensorflow-io
```

---

## 3. Google Colab Setup

Mount Google Drive:

```python
from google.colab import drive
drive.mount('/content/drive')
```

---

# 🚀 How to Train the Model

## Step 1 — Prepare Dataset

Ensure the MRI dataset is organized by tumor category.

---

## Step 2 — Run Preprocessing

Execute preprocessing and augmentation cells inside the notebook.

---

## Step 3 — Train MobileNetV2 Model

Run:

```python
model.fit()
```

with callbacks:

* EarlyStopping
* ReduceLROnPlateau

---

## Step 4 — Save Model

```python
model.save("cnn_cancer_prediction_model_refined.keras")
```

---

# 🔬 How to Run Predictions

## Single MRI Prediction Workflow

1. Upload MRI image
2. Resize to 224×224
3. Normalize image
4. Run prediction
5. Display predicted tumor type

---

## Example Prediction Classes

| Class ID | Prediction |
| -------- | ---------- |
| 0        | Glioma     |
| 1        | Meningioma |
| 2        | Pituitary  |
| 3        | No Tumor   |

---

# 🖼 Sample Prediction Results

> Add MRI prediction screenshots here

Example:

| MRI Image   | Predicted Class |
| ----------- | --------------- |
| Example MRI | Glioma          |
| Example MRI | Pituitary       |
| Example MRI | No Tumor        |

---

# 🔮 Future Improvements

## Planned Enhancements

* EfficientNet Integration
* ResNet-Based Experiments
* Hyperparameter Optimization
* Ensemble Learning
* 3D CNN for NIfTI MRI Data
* Improved Dataset Diversity
* Better Generalization Across Hospitals
* Streamlit/Flask Deployment
* Real-time MRI Upload Interface

---

# 📜 License

This project is licensed under the MIT License.

You may create a `LICENSE` file using the MIT License template.

---

# 📖 Citation

If you use this project in research or academic work, please cite:

```bibtex
@misc{basim2026brainmri,
  author = {Basim Hassan},
  title = {Brain Tumor MRI Classificationised Prediction},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {https://github.com/BasimHassan2008}
}
```

---

# 👨‍💻 Author

## Basim Hassan

Founder & CEO — Vaigoo Innovations

📧 Email: [basimhassan325@gmail.com](mailto:basimhassan325@gmail.com)

🐙 GitHub: https://github.com/BasimHassan2008

💼 LinkedIn: https://www.linkedin.com/in/basim-hassan-a01523394/

🌐 Portfolio/CV: https://basimhassan2008.github.io/CV/#hero

---

# ⭐ Acknowledgements

* TensorFlow
* Keras
* Google Colab
* MobileNetV2
* MRI Medical Imaging Research Community
* Kaggle BraTS2020 Dataset

---

# ❤️ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the repository
🧠 Contribute improvements
📢 Share with researchers and developers

---
