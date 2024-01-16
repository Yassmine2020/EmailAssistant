from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def classify_review(review):
  inputs = tokenizer(review, return_tensors="pt")

  with torch.no_grad():
    logits = model(**inputs).logits

  predicted_class_id = logits.argmax().item() + 1
  return predicted_class_id