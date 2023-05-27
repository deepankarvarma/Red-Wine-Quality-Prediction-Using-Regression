# Red Wine Price Prediction Using Regression

This repository contains code for applying regression models to predict the quality of Red Wine using other user-inputted parameters. It also includes exploratory data analysis (EDA) and outlier analysis methods.

## Models and Accuracy

The following regression models were implemented and evaluated for the prediction of Red Wine quality:

1. Random Forest: 55.16% accuracy
2. Linear Regression: 59.11% accuracy
3. Ridge Regression: 46.26% accuracy

Please note that the provided accuracy scores are indicative of the performance achieved by the models based on the given dataset and problem statement.

## Dataset

The dataset used for this project can be found at the following link:

[Red Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

The dataset contains various input parameters for Red Wine, such as acidity levels, sugar content, pH, alcohol content, and more. It also includes a quality rating for each wine sample.

## Application

To visualize and interact with the Red Wine quality prediction model, you can access the Streamlit application using the following link:

[Red Wine Quality Prediction Application](https://deepankarvarma-red-wine-quality-prediction-using-reg-app-usduxo.streamlit.app/)

The Streamlit application provides a user-friendly interface where users can input the relevant parameters for a Red Wine sample and receive a predicted quality rating based on the trained regression models.

## Usage

To run the code locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Install the required dependencies. It is recommended to use a virtual environment:

```bash
cd your-repository
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).

Feel free to explore the code and customize it to suit your needs.

## Contributing

If you would like to contribute to this project, you can fork the repository and submit a pull request with your proposed changes. Contributions are always welcome!

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.

## Acknowledgments

Special thanks to the authors of the [Red Wine Quality Dataset](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009) for providing the dataset used in this project.

