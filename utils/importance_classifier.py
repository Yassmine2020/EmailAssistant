import joblib
import pandas as pd

# Load the model and encoders
best_model = joblib.load('knn_model.joblib')
encoder = joblib.load('onehot_encoder.joblib')
label_encoder = joblib.load('label_encoder.joblib')

def issue_complexity(category, sub_category, sentiment):
    if (category, sub_category) == ('error','error'):
        predicted_complexity = 'less'
    else:
        # Prepare new data for encoding
        new_data = pd.DataFrame([[category, sub_category, sentiment]], columns=['issue_area', 'issue_category', 'customer_sentiment'])
        
        # Encode the new data using loaded OneHotEncoder
        encoded_new_data = encoder.transform(new_data)
        
        # Predict using the loaded model
        predicted_complexity_encoded = best_model.predict(encoded_new_data)
        
        # Decode the predicted complexity using loaded LabelEncoder
        predicted_complexity = label_encoder.inverse_transform(predicted_complexity_encoded)
    
    return predicted_complexity