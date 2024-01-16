import openai

# Set your OpenAI API key here
openai.api_key = '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'

def get_gpt3_response(customer_email):
    prompt = f"Customer support request:\n{customer_email}\n\nProvide the best response to the customer's email."

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

# Example usage
customer_email = """
    Hi Support Team,

    I'm having trouble with my account login. I've tried resetting my password,
    but it's not working. Can you please assist me in resolving this issue?

    Thank you,
    [Customer Name]
"""

best_answer = get_gpt3_response(customer_email)
if best_answer:
    print("Best response:", best_answer)
else:
    print("Unable to get a response.")
