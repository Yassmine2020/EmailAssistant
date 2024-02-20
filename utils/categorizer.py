import openai
from .keys import openai_key
import json
# from transformers import pipeline

# pipe = pipeline("text-classification", model="vineetsharma/customer-support-intent-albert")

# def categorizer(text_to_classify):
#   prediction = pipe(text_to_classify)
#   return prediction[0]['label']

openai.api_key = openai_key

categories = ['Login and Account', 'Cancellations and returns', 'Order',
       'Shopping', 'Warranty', 'Shipping']

sub_cat = ['Mobile Number and Email Verification', 'Pickup and Shipping',
       'Replacement and Return Process',
       'Login Issues and Error Messages', 'Order Delivery Issues',
       'Account Reactivation and Deactivation',
       'Cash on Delivery (CoD) Refunds',
       'Product Availability and Status', 'Product Installation',
       'Order Cancellation', 'Lost or Missing Warranty Card',
       'Return and Exchange', 'Start Date of Warranty',
       'Invoice and Payment', 'Account and Shopping', 'Miscellaneous',
       'Accessing Warranty Details',
       'Availability of Faster Delivery Options', 'Returns and Refunds',
       'Warranty Terms and Changes', 'Pricing and Discounts',
       'Login Methods', 'Product Availability for Shipping',
       'Return Checks and Fees', 'Book Pricing Discrepancies',
       'Order Confirmation and Status', 'Product Information and Tags',
       'Loyalty program', 'Installation and Accessories',
       'Warranty Claim Process', 'Product Registration and Warranty',
       'Expedited Delivery', 'Adding and Changing Account Information',
       'Standard Shipping Speeds and Delivery Charges',
       'Shipping Options for Returns', 'Placing an Order',
       'Free Delivery Qualification', 'Delivery Process',
       'Extended Warranty',
       "Contacting Seller's Partnered Courier Service Providers"]

def categorizer(text_to_classify):
    prompt = f'''
    Given the following email summary:
    "{text_to_classify}"
    Identify the category and sub-category from the provided lists.
    Categories: {categories}
    Sub-categories: {sub_cat}
    Provide the answer in the following format:
    ["category", "sub_category"]
    '''
    
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=60,
            temperature=0.5,
            stop=None
        )
        # Assuming the model outputs in a directly usable format, but adding parsing just in case
        parsed_response = response.choices[0].text.strip().strip("=").strip()
        # If the model output includes JSON-like structure, this will parse it
        if parsed_response.startswith("[") and parsed_response.endswith("]"):
            return json.loads(parsed_response)
        else:
            # Fallback or default value if parsing fails
            return ["Unable to determine", "Unable to determine"]
    except Exception as e:
        print("An error occurred:", e)
        return ["error", "error"]