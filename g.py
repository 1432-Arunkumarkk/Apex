
import google.generativeai as genai

# Set your API key here
api_key = 'AIzaSyBPe5w7FG1OQ1AMP_mMPwOJpwMj3M5JN1s'

genai.configure(api_key=api_key)

# Initialize the GenerativeModel without specifying 'name'
model = genai.GenerativeModel()

# Generate content using the model
response = model.generate_content('Please summarise this document: ...')

# Print the generated content
print(response.text)
