# Complete 30-Day Syllabus

DAILY_LESSONS = [
    {
        "day": 1,
        "topic": "Introduction to Python for ML",
        "description": "Learn about NumPy and pandas - the foundation of Python ML",
        "task": "Install Python, Jupyter, and required libraries. Create a NumPy array and pandas DataFrame.",
        "learning_objectives": [
            "Understand NumPy arrays and their operations",
            "Understand pandas DataFrames and Series",
            "Basic data manipulation"
        ]
    },
    {
        "day": 2,
        "topic": "Data Loading & Exploration",
        "description": "Loading data from CSV, Excel, JSON formats",
        "task": "Load the Titanic dataset from CSV and explore its structure",
        "learning_objectives": [
            "Load data from different file formats",
            "Use head(), info(), describe() for exploration",
            "Understand data types"
        ]
    },
    {
        "day": 3,
        "topic": "Data Wrangling I: DataFrames & Filtering",
        "description": "Working with DataFrames, filtering, handling missing values",
        "task": "Count missing values in Titanic dataset and drop a column",
        "learning_objectives": [
            "Filter DataFrames using boolean conditions",
            "Handle missing values with dropna() and fillna()",
            "Access data with loc and iloc"
        ]
    },
    {
        "day": 4,
        "topic": "Data Wrangling II: Grouping & Merging",
        "description": "Grouping data and merging DataFrames",
        "task": "Calculate average age for male vs female passengers",
        "learning_objectives": [
            "Use groupby() for aggregations",
            "Merge DataFrames with merge() and concat()",
            "Apply functions to columns"
        ]
    },
    {
        "day": 5,
        "topic": "Preprocessing Numerical Data",
        "description": "Scaling and standardization techniques",
        "task": "Standardize the 'Age' feature using StandardScaler",
        "learning_objectives": [
            "Understand Min-Max scaling",
            "Understand Standardization (Z-score)",
            "Use StandardScaler and MinMaxScaler"
        ]
    },
    {
        "day": 6,
        "topic": "Preprocessing Categorical Data",
        "description": "Encoding categorical variables for ML",
        "task": "One-hot encode 'Sex' and 'Embarked' columns",
        "learning_objectives": [
            "Understand one-hot encoding",
            "Use LabelEncoder and OneHotEncoder",
            "Handle categorical features"
        ]
    },
    {
        "day": 7,
        "topic": "Text Preprocessing",
        "description": "Cleaning, tokenization, stopwords",
        "task": "Tokenize a sentence and remove stopwords using NLTK",
        "learning_objectives": [
            "Clean text data (remove punctuation, lowercase)",
            "Tokenize text into words",
            "Remove stopwords"
        ]
    },
    {
        "day": 8,
        "topic": "Model Evaluation I: Train/Test Split",
        "description": "Understanding data splitting and cross-validation",
        "task": "Split Titanic data into training and test sets (80/20)",
        "learning_objectives": [
            "Understand train/test split",
            "Use train_test_split()",
            "Understand why we need validation"
        ]
    },
    {
        "day": 9,
        "topic": "Linear Regression",
        "description": "Simple linear regression for prediction",
        "task": "Train a linear regression model to predict 'Age' from other features",
        "learning_objectives": [
            "Understand linear regression",
            "Use LinearRegression from sklearn",
            "Interpret coefficients"
        ]
    },
    {
        "day": 10,
        "topic": "Logistic Regression",
        "description": "Classification with logistic regression",
        "task": "Train a logistic regression model to predict 'Survived'",
        "learning_objectives": [
            "Understand logistic regression for classification",
            "Use LogisticRegression",
            "Predict class probabilities"
        ]
    },
    {
        "day": 11,
        "topic": "K-Nearest Neighbors",
        "description": "Classification using nearest neighbors",
        "task": "Train a KNN classifier and find optimal k value",
        "learning_objectives": [
            "Understand KNN algorithm",
            "Use KNeighborsClassifier",
            "Find optimal k using cross-validation"
        ]
    },
    {
        "day": 12,
        "topic": "Decision Trees",
        "description": "Building and visualizing decision trees",
        "task": "Train a decision tree classifier and visualize it",
        "learning_objectives": [
            "Understand decision trees",
            "Use DecisionTreeClassifier",
            "Visualize tree structure"
        ]
    },
    {
        "day": 13,
        "topic": "Random Forests",
        "description": "Ensemble learning with random forests",
        "task": "Train a random forest and compare to a single decision tree",
        "learning_objectives": [
            "Understand ensemble learning",
            "Use RandomForestClassifier",
            "Compare performance"
        ]
    },
    {
        "day": 14,
        "topic": "Model Evaluation Metrics",
        "description": "Confusion matrix, precision, recall, F1, ROC",
        "task": "Evaluate your best classifier using these metrics",
        "learning_objectives": [
            "Understand confusion matrix",
            "Calculate precision, recall, F1",
            "Understand ROC curves and AUC"
        ]
    },
    {
        "day": 15,
        "topic": "Support Vector Machines",
        "description": "SVM for classification",
        "task": "Train an SVM classifier to predict 'Survived'",
        "learning_objectives": [
            "Understand SVM and hyperplanes",
            "Use SVC",
            "Understand kernels"
        ]
    },
    {
        "day": 16,
        "topic": "Naive Bayes Classifiers",
        "description": "Gaussian, Multinomial, and Bernoulli Naive Bayes",
        "task": "Train a Gaussian Naive Bayes classifier",
        "learning_objectives": [
            "Understand Bayes' theorem",
            "Use GaussianNB",
            "Understand different NB variants"
        ]
    },
    {
        "day": 17,
        "topic": "Feature Selection & Dimensionality Reduction",
        "description": "PCA, LDA for reducing feature space",
        "task": "Apply PCA to Iris dataset and reduce to 2 components",
        "learning_objectives": [
            "Understand PCA",
            "Use PCA from sklearn",
            "Understand explained variance"
        ]
    },
    {
        "day": 18,
        "topic": "Clustering",
        "description": "K-Means and DBSCAN clustering",
        "task": "Cluster Iris dataset using K-Means and visualize",
        "learning_objectives": [
            "Understand K-Means clustering",
            "Use KMeans from sklearn",
            "Understand DBSCAN"
        ]
    },
    {
        "day": 19,
        "topic": "Bag of Words & TF-IDF",
        "description": "Text vectorization techniques",
        "task": "Convert text documents into TF-IDF matrix",
        "learning_objectives": [
            "Understand Bag of Words",
            "Use CountVectorizer",
            "Use TfidfVectorizer"
        ]
    },
    {
        "day": 20,
        "topic": "Sentiment Analysis",
        "description": "Using Bag of Words for sentiment classification",
        "task": "Build a sentiment classifier for movie reviews",
        "learning_objectives": [
            "Apply ML to text data",
            "Build an end-to-end text classification pipeline",
            "Evaluate on real data"
        ]
    },
    {
        "day": 21,
        "topic": "Topic Modeling",
        "description": "NMF for topic discovery in text",
        "task": "Use NMF to discover topics in news articles (Reuters dataset)",
        "learning_objectives": [
            "Understand topic modeling",
            "Use NMF for topic extraction",
            "Interpret topics"
        ]
    },
    {
        "day": 22,
        "topic": "Introduction to Neural Networks",
        "description": "Building simple NN with Keras/TensorFlow",
        "task": "Build a simple fully-connected neural network",
        "learning_objectives": [
            "Understand neural network architecture",
            "Use Keras Sequential model",
            "Understand activation functions"
        ]
    },
    {
        "day": 23,
        "topic": "Training Neural Networks",
        "description": "Overfitting, early stopping, model evaluation",
        "task": "Implement early stopping in your neural network",
        "learning_objectives": [
            "Understand overfitting in NNs",
            "Use early stopping",
            "Monitor training/validation loss"
        ]
    },
    {
        "day": 24,
        "topic": "CNN for Image Classification",
        "description": "Convolutional Neural Networks",
        "task": "Build and train a CNN to classify MNIST digits",
        "learning_objectives": [
            "Understand CNN architecture",
            "Use Conv2D and MaxPooling2D",
            "Train on image data"
        ]
    },
    {
        "day": 25,
        "topic": "RNN/LSTM for Text",
        "description": "Recurrent Neural Networks for sequence data",
        "task": "Build an LSTM for sentiment analysis",
        "learning_objectives": [
            "Understand RNNs and LSTMs",
            "Use LSTM layer in Keras",
            "Handle sequential text data"
        ]
    },
    {
        "day": 26,
        "topic": "Hyperparameter Tuning",
        "description": "GridSearchCV and RandomizedSearchCV",
        "task": "Use GridSearchCV to find best hyperparameters for Random Forest",
        "learning_objectives": [
            "Understand hyperparameter tuning",
            "Use GridSearchCV",
            "Use RandomizedSearchCV"
        ]
    },
    {
        "day": 27,
        "topic": "Handling Imbalanced Datasets",
        "description": "Upsampling, downsampling, class weights",
        "task": "Apply upsampling to handle an imbalanced dataset",
        "learning_objectives": [
            "Understand class imbalance problem",
            "Use upsampling and downsampling",
            "Use class_weight parameter"
        ]
    },
    {
        "day": 28,
        "topic": "Model Persistence",
        "description": "Saving and loading trained models",
        "task": "Save your best trained model to .pkl or .h5 file",
        "learning_objectives": [
            "Use joblib for sklearn models",
            "Use model.save() for Keras models",
            "Load saved models"
        ]
    },
    {
        "day": 29,
        "topic": "Building ML Pipelines",
        "description": "Creating end-to-end ML pipelines",
        "task": "Build a scikit-learn pipeline that scales data and fits logistic regression",
        "learning_objectives": [
            "Understand Pipeline from sklearn",
            "Combine preprocessing and modeling",
            "Use cross-validation with pipelines"
        ]
    },
    {
        "day": 30,
        "topic": "Course Review & Capstone",
        "description": "Review all topics and build a complete ML application",
        "task": "Choose a dataset and build an end-to-end ML solution",
        "learning_objectives": [
            "Apply all learned concepts",
            "Build production-ready ML code",
            "Present and explain results"
        ]
    }
]

def get_lesson(day_num):
    """Get lesson for a specific day"""
    for lesson in DAILY_LESSONS:
        if lesson["day"] == day_num:
            return lesson
    return None

def get_all_days():
    """Get all lesson days"""
    return [lesson["day"] for lesson in DAILY_LESSONS]