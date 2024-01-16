from transformers import pipeline

pipe = pipeline("text-classification", model="vineetsharma/customer-support-intent-albert")

def categorizer(text_to_classify):
  prediction = pipe(text_to_classify)
  return prediction[0]['label']