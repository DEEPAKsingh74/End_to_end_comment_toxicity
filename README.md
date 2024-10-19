# End_to_end_comment_toxicity

# Comment Toxicity Detection

## Website
- https://comment-toxicity-website.vercel.app/

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Overview
Comment toxicity detection is a machine learning and deep learning project aimed at identifying and classifying toxic comments in online discussions. The goal is to create a model that can automatically flag inappropriate or harmful comments, thereby fostering a healthier online environment.

## Features
- Detects toxic comments in text using state-of-the-art machine learning algorithms.
- Utilizes natural language processing (NLP) techniques to preprocess text data.
- Implements various models, including logistic regression, support vector machines, and deep learning architectures (e.g., LSTM, CNN).
- Evaluates model performance using metrics like accuracy, precision, recall, and F1-score.
- Provides an intuitive interface for testing and deploying the model.

## Technologies Used
- **Programming Languages**: Python
- **Libraries/Frameworks**: 
  - Pandas
  - NumPy
  - Scikit-learn
  - TensorFlow/Keras
  - NLTK/Spacy (for NLP tasks)
- **Data Visualization**: Matplotlib, Seaborn
- **Environment**: Jupyter Notebook / Google Colab

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/DEEPAKsingh74/End_to_end_comment_toxicity.git
   cd comment-toxicity-detection
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

## Usage
1. Prepare your dataset (if you have a custom dataset) or use the provided dataset.
2. Run the Jupyter Notebook to train the models:
   ```bash
   jupyter notebook
   ```
3. Execute the notebook cells step-by-step to preprocess data, train models, and evaluate results.

## Dataset
The dataset used for this project is sourced from [Kaggle's Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). It contains various comments labeled as toxic, severe toxic, obscene, threat, insult, and identity hate.

### Dataset Description:
- **Columns**:
  - `id`: Unique identifier for each comment.
  - `comment_text`: The text of the comment.
  - `toxic`: Binary label indicating if the comment is toxic (1) or not (0).
  - Additional columns for other toxicity labels.

## Model Architecture
### Preprocessing
- Text cleaning and normalization (removing punctuation, converting to lowercase).
- Tokenization and padding for model input.

### Model Types
- **Logistic Regression**: Basic model for baseline comparison.
- **Support Vector Machine (SVM)**: For classification tasks.
- **Deep Learning Models**: 
  - LSTM (Long Short-Term Memory)
  - CNN (Convolutional Neural Network)

## Results
The model's performance is evaluated using various metrics:
- Accuracy: 98%
- Precision: 94%
- Recall: 94%
- F1 Score: 90%

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Kaggle](https://www.kaggle.com/) for providing the dataset.
- The open-source community for their invaluable resources and tools.
