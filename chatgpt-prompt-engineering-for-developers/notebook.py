# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # Assign the role and content for the message
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Write a poem about ChatGPT")
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Write a poem about ChatGPT. Use basic English that a child can understand."

# Get the response
response = get_response(prompt)

print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks. 
 ```{story}```"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to complete the story
prompt = f"""Complete the story delimited by triple backticks with only two paragraphs using the style of William Shakespeare. 
 ```{story}```"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = "Generate a table containing 10 books I should read if I am a sci-fi lover, with columns for Title, Author, and Year."

# Get the response
response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language, then generate a suitable title for it. "

# Create the output format
output_format = """Use the following format for the output:
         - Text: <the text>
         - Language: <the text language>
         - Title: <the generated title>"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language and the number of sentences it contains. Then, if the text has more than one sentence, generate a suitable title for it. Otherwise, if the text contains only one sentence, write 'N/A' for the title."

# Create the output format
output_format = """The output should follow this format:
          - Text: <the given text>
          - Language: <the text language>
          - N_sentences: <number of sentences>
          - Title: <the generated title>'."""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a one-shot prompt
prompt = """
     Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = {1, 3, 7, 19}
     Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:
"""

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  # Provide the examples as previous conversations
  messages = [{"role": "user",
         "content": "The product quality exceeded my expectations"},
              {"role": "assistant",
         "content": "1"},
              {"role": "user",
         "content": "I had a terrible experience with this product's customer service"},
              {"role": "assistant",
         "content": "-1"}, 
              # Provide the text for the model to classify
              {"role": "user",
         "content": "The price of the product is really fair given its features"}
             ],
  temperature = 0
)
print(response.choices[0].message.content)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "Help me plan a beach vacation."

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """
     Help me plan a beach vacation.
     Step 1 - Specify four potential locations for beach vacations
     Step 2 - State some accommodation options in each
     Step 3 - State activities that could be done in each
     Step 4 - Evaluate the pros and cons for each destination
    """

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""
     Analyze the correctness of the function delimited by triple backticks according to the following criteria:
      1- It should have correct syntax
      2- The function should receive only 2 inputs
      3- The function should return only one output
      ```{code}```
    """

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = "Compute the age of my friend's father in 10 years, given that now he's double my friend's age, and my friend is 20. Give a step by step explanation."

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2. Adding them: 10+4+2=16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14} 
             A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the self_consistency instruction
self_consistency_instruction = "Imagine three completely independent experts who reason differently are answering this question. The final answer is obtained by majority vote. The question is: "

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + problem_to_solve

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = "Generate a table that contains the top 10 pre-trained language models, with columns for language model, release year, and owners."

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
School begins tomorrow -> No explicit emotion
Time flies like an arrow ->
"""

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""
Summarize the report delimited by triple backticks with a maximum of 5 sentences, while focusing on aspects related to AI and data privacy.
 ```{report}```
"""

response = get_response(prompt)

print("Summarized report: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f"""
Summarize the product description delimited by triple backticks, in at most five bullet points while focusing on the product features and specifications
 ```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""
Expand the product description for the Smart Home Security Camera delimited by triple backticks to provide a comprehensive overview of its features, benefits, potential applications, without bypassing the limit of one paragraph. 
 ```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f"""Translate the English marketing message delimited by triple backticks to French, Spanish, and Japanese
 ```{marketing_message}```
"""

response = get_response(prompt)

print("English:", marketing_message)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""
Write the email delimited by triple backticks using a professional, positive, and user-centric tone:
 ```{sample_email}```
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f"""Transform the text delimited by triple backticks with the following two steps:
Step 1 - Proofread it without changing its structure
Step 2 - Change the tone to be formal and friendly
 ```{text}```"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""Classify the ticket delimited by triple backticks as technical issue, billing inquiry, or product feedback. Your response should just contain the class and nothing else.
 ```{ticket}```"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""Ticket: {ticket_1} -> Entities: {entities_1}
            Ticket: {ticket_2} -> Entities: {entities_2}
            Ticket: {ticket_3} -> Entities: {entities_3}
            Ticket: {ticket_4} -> Entities: """

response = get_response(prompt)

print("Ticket: ", ticket_4)
print("Entities: ", response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = "Write a Python function that accepts a list of 12 numbers representing sales for each month of the year, and outputs the month with the highest sales value"

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 24
input = [5, 2, 4] -> output = 12
input = [2, 1, 3] -> output = 7
input = [8, 4, 6] -> output = 19
"""

# Craft a prompt that asks the model for the function
prompt = f"""You are provided with input-output examples delimited by triple backticks for a Python function where different factors are associated with project completion time. Each example includes numerical values for the factors and the corresponding estimated completion time. Write a code for this function.
 ```{examples}```"""

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
     return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""Modify the script delimited by triple backticks as follows:
             - The function should return the perimeter of the rectangular floor as well.
             - The inputs (floor dimensions) should be positive. Otherwise, appropriate error messages should be displayed.
           ```{function}```"""

response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Explain what the function delimited by triple backticks does. Let's think step by step
 ```{function}```
"""
 
response = get_response(prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
          {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-3.5-turbo", messages= messages, temperature=0)

  return response.choices[0].message.content

# Try the function with a system and user prompt of your choice 
response = get_response("You are an expert data scientist that explains complex concepts in understandable terms", "Define AI")
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. "

# Define audience guidelines
audience_guidelines = "Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Maintain a professional and user-friendly tone in your responses."

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(base_system_prompt, "My new headphones aren't connecting to my device")
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "If the user is asking about an order, and did not specify the order number, reply by asking for this number. "

# Define the technical issue condition
technical_issue_condition = "If the user is talking about a technical issue, start your response with `I'm sorry to hear about your issue with ...` "

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "If the user's query does not include details about their background, experience, or goals, kindly ask them to provide the missing information."

# Define response guidelines
response_guidelines = "Don't recommend more than three textbooks in the learning path"

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = "You are a customer service chatbot for MyPersonalDelivery, a delivery service that offers a wide range of delivery options for various items. You should respond to user queries in a gentle way."

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": context_question},
            {"role": "assistant", "content": context_answer},
            {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)

# Set your API key
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks. You should respond to user queries in a gentle way.
 ```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)

