# Netflix Recommendation System

## Overview
This repository features a Netflix recommendation system that suggests shows similar to the user-provided input. The system uses the TFIDF (Term Frequency-Inverse Document Frequency) technique to analyze and recommend content based on user preferences.

## Key Features
- **TFIDF Technique:** Applies TFIDF to weight words in content descriptions, enhancing the accuracy of recommendations.
- **Recommendation Engine:** Provides content recommendations similar to the user's watched list.

## Project Structure
- **`tfidf.py`**: Implements the recommendation engine using TFIDF.
- **`netflix_eda.py`**: Performs exploratory data analysis (EDA) on the Netflix dataset.
- **`netflix_titles.csv`**: CSV file containing Netflix titles and related data.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Technologies Used
- **Python Libraries:**
  - `pandas` for data manipulation
  - `scikit-learn` for implementing TFIDF
  - `nltk` for natural language processing, including stopwords removal
- **Dataset:** Netflix titles in CSV format

## Setup Instructions
1. **Install Dependencies:** Use the following command to install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
2. **NLTK Stopwords:** Ensure the NLTK stopwords list is installed by running:
    ```python
    import nltk
    nltk.download('stopwords')
    ```

## Usage
1. **Run `tfidf.py`:** Executes the recommendation engine. Provide a show title to receive similar recommendations.
2. **Run `netflix_eda.py`:** Performs exploratory data analysis on the dataset for insights and understanding.

## Example
To see the recommendation system in action, execute the `tfidf.py` script with a show title input to get similar recommendations.

## Contributing
Contributions are welcome! Please open issues or submit pull requests for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information, visit the [GitHub repository](https://github.com/fey0/Netflix-Recommender).
