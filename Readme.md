## Project Overview

This workspace is a hands-on collection of Python notebooks and examples covering data analysis, machine learning, feature engineering, database use, logging, parallel computing, and related workflows.

It is organized into topic-focused folders so you can explore foundational concepts, data preprocessing techniques, model building, algorithm implementations, and applied analysis.

---

## Folder Structure and Content

### 1. Data Analysis with Python
Contains notebooks teaching basic data analysis using Python libraries:
- `01_numpy.ipynb`: Numpy array creation, indexing, broadcasting, and vectorized operations.
- `02_pandas.ipynb`: Pandas Series and DataFrame creation, selection, filtering, aggregation, and manipulation.
- `03_data_manipulation.ipynb`: Data cleaning, transformation, merging, sorting, and reshaping.
- `04_matplotlib.ipynb`: Plotting fundamentals with Matplotlib, line charts, bar plots, histograms, and customization.
- `05_seaborn.ipynb`: Statistical plotting with Seaborn, including distributions, relationships, and categorical plots.
- `06_missingvalue_dataset.ipynb`: Handling missing data, imputation, and dataset preparation.
- Sample datasets: `Sales.csv`, `sample_sales.csv`, `student grade.csv`, `task.csv`.

### 2. Working with Databases
- `01_sqlite.ipynb`: Learn SQLite database creation, SQL queries, table management, and integration with Python.

### 3. Logging In Python
Focuses on structured logging and real-world logging examples:
- `01_python_logging.ipynb`: Python logging concepts, logger configuration, handlers, and formatters.
- `02_multiple_loggers.ipynb`: Managing multiple loggers and logging from different modules.
- `logs/logger.py`: Example logger setup used in sample applications.
- `logs/test.py`: Test script for validating logging behavior.
- `real world problem/app.py`: A real-world Python example using logging for application events.

### 4. Multiprocessing and Multithreading
Explores concurrency and parallelism in Python:
- `01_multithreading.ipynb`: Thread-based concurrency, thread creation, synchronization, and shared data.
- `02_multiprocessing.py`: Process-based parallelism and use of the multiprocessing module.
- `03_advance_multithreading.py`: Advanced multithreading patterns and thread coordination.
- `04_advanec_multiprocessing.py`: Advanced multiprocessing usage and process communication.
- `05_MT_real_wolrd_use_case.py`: Multithreading applied to a real-world use case.
- `06_MP_real_world_use_case.py`: Multiprocessing applied to a real-world use case.

### 5. Feature Engineering
Covers preprocessing techniques that improve model performance:
- `01_handling_missing_values.ipynb`: Missing value detection and imputation strategies.
- `02_handling_imbalance_dataset.ipynb`: Techniques for handling imbalanced datasets.
- `03_handling_outliers.ipynb`: Outlier detection and treatment methods.
- `04_OneHOTencoding.ipynb`: One-hot encoding for categorical variables.
- `05_LabelEncoding.ipynb`: Label encoding for categorical variables.
- `06_TGOE.ipynb`: Target guided ordinal encoding.
- `07_SMOTE.ipynb`: Synthetic Minority Over-sampling Technique for imbalanced classes.

### 6. EDA
Exploratory data analysis notebooks with real datasets:
- `01_RedWineDataset.ipynb`: EDA on the red wine quality dataset.
- `02_FlightPricePrediction.ipynb`: Flight price analysis and visualization.
- `03_googlePlayStore.ipynb`: Analysis of Google Play Store apps.
- `04_LeoDataset.ipynb`: Analysis of the Leo dataset.
- Datasets: `flight_price.csv`, `googleplaystore.csv`, `Leo_dataset.csv`, `winequality-red.csv`.
- `Data/google_Cleaned.csv`: Cleaned dataset for analysis.

### 7. MACHINE LEARNING
A large collection of machine learning examples and algorithm notebooks.
The main folders include:
- `[1]. Linear Regression`: Simple, multiple, polynomial regression, and regularization.
  - `01_simple_lr.ipynb`, `02_simple_lr_scratch.ipynb`, `03_simple_lr_using_GD.ipynb`: Linear regression from scratch and using gradient descent.
  - `height-weight.csv`, `placement.csv`: Example datasets.
- `[2]. SVM`: Support Vector Classification (`SVC`) and Regression (`SVR`).
- `[3]. Logistic Regression`: Binary and multi-class classification, handling imbalanced datasets, and ROC/AUC.
- `[4]. Naive Baysian Classifier`: Naive Bayes classification examples.
- `[5]. KNN`: k-Nearest Neighbors classification and regression.
- `[6]. Decision Tree`: Decision tree classification and regression implementations.
- `[7]. Random Forest`: Ensemble learning with Random Forest classifiers and regressors.
- `[8]. BOOSTING`: Boosting algorithms and gradient boosting examples.
- `[9]. Clustering`: Unsupervised learning with clustering methods.
  - `[1]. Kmeans`: K-Means clustering.
  - `[2]. Hierarichal`: Hierarchical clustering.
  - `[3]. DBSCAN`: Density-based clustering.

### 8. PCA
- `01_pca.ipynb`: Principal Component Analysis for dimensionality reduction, explained variance, and visualization.

### Questions
Contains organized question-driven notebooks and datasets for practice:
- `EDA+MODEL_TRAINING/`: End-to-end examples with EDA and model training on datasets like Iris, tip prediction, salary prediction, and wine quality.
- `Numpy/`: Additional Numpy practice notebooks.
- `Pandas/`: Additional Pandas practice notebooks.

---

## Algorithms and Techniques Covered
- Data manipulation with Numpy and Pandas
- Visualization with Matplotlib and Seaborn
- SQL database queries using SQLite
- Python logging best practices
- Multithreading and multiprocessing in Python
- Feature engineering: missing values, imbalance, outliers, encoding, SMOTE, and more
- Exploratory data analysis (EDA) for datasets in finance, health, and apps
- Regression algorithms: simple, multiple, polynomial, ridge, lasso, and elastic net
- Classification algorithms: logistic regression, SVM, KNN, Naive Bayes, decision trees, random forests, boosting
- Unsupervised learning: K-Means, hierarchical clustering, DBSCAN
- Dimensionality reduction: PCA

## How to Use
1. Open a folder of interest in Jupyter Notebook or JupyterLab.
2. Run notebooks sequentially to follow concepts from basic data analysis through machine learning.
3. Use the dataset files inside each folder when prompted by notebooks.
4. Modify code cells to try new data, algorithms, or hyperparameters.

## Notes
- This workspace is ideal for learners exploring Python-based data science and machine learning.
- Many notebooks demonstrate both theoretical concepts and practical implementation.
- The structure is intentionally modular to allow focused learning on each topic.
