import openai
from transformers import pipeline

pipe = pipeline("text-classification", model="vineetsharma/customer-support-intent-albert")

def categorizer(text_to_classify):
  prediction = pipe(text_to_classify)
  return prediction[0]['label']

# def categorizer(text_to_classify):
#     # prompt = f"Customer support request:\n{customer_email}\n\nProvide the best response to the customer's email."
#     prompt = ''

#     try:
#         response = openai.Completion.create(
#             engine="gpt-3.5-turbo-instruct",
#             prompt=prompt,
#             max_tokens=250
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print("An error occurred:", e)
#         return None