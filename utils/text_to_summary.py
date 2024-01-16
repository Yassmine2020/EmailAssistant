from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def text_to_summary(text):
  summarized_text = summarizer(text, max_length=130, min_length=30, do_sample=False)
  return summarized_text[0]['summary_text']