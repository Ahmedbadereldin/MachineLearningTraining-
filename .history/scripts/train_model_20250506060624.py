from data_loader import load_data
from preprocess import split_data
from utils.metrics import evaluate_model

from sklearn.ensemble import RandomForestClassifier

def main():
    # تحميل البيانات
    df = load_data('PhishingData.arff')  # تأكد أن الملف موجود
    print("✅ Data loaded")

    # تقسيم البيانات
    X_train, X_test, y_train, y_test = split_data(df)
    print("✅ Data split")

    # تدريب النموذج
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    print("✅ Model trained")

    # التقييم
    y_pred = model.predict(X_test)
    evaluate_model(y_test, y_pred)

if __name__ == "__main__":
    main()