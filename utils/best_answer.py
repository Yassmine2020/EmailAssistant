import openai
from .keys import openai_key

# Set your OpenAI API key here
openai.api_key = openai_key

def best_answer(customer_email):
    prompt = f"Given the following email summary, generate the best response: \n {customer_email}."
    # prompt = f"Customer support request:\n{customer_email}\n\nProvide the best response to the customer's email."

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=250
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print("An error occurred:", e)
        return None