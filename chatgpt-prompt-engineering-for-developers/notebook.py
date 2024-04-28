# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: R
#     langauge: R
#     name: ir
# ---

# # Introduction to Prompt Engineering Best Practices
#
# ## Creating the get_response() function
#
# Most of the exercises in this course will call the `chat.completions`
# endpoint of the OpenAI API with a user prompt. Here, you will create a
# `get_response()` function that receives a prompt as input and returns
# the response as an output. You will then use this function to generate a
# poem about ChatGPT. In future exercises, this function will be
# pre-loaded for you.
#
# Please note that DataCamp does not store keys used in the exercises.
#
# **Note**: Some exercises can take longer to run due to API calls and
# lengthy responses.
#
# The `OpenAI` package has been pre-loaded for you.
#
# **Instructions**
#
# - Set your API key to `api_key` within the `OpenAI()` class.
# - Create a request to the `chat.completions` endpoint inside the
#   `get_response()` function.
# - Assign the `"user"` role and the content, the `prompt` parameter, for
#   the message to be sent within the `get_response()` function.
# - Try out the function with a prompt that asks the model to write a poem
#   about ChatGPT.
#
# **Answer**
#

# +
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

# -

# ## Exploring prompt engineering
#
# Prompt engineering refers to crafting effective prompts to elicit
# desired responses from the language model. By refining your prompts, you
# can achieve better results and guide the model towards generating more
# accurate and useful responses. Your task in this exercise is to modify
# the prompt you used in the previous exercise.
#
# The `OpenAI` package and the `get_response()` function have been
# pre-loaded for you.
#
# **Instructions**
#
# - Set your API key to `api_key` within the `OpenAI()` class.
# - Craft a `prompt` that asks the model to generate a poem about ChatGPT
#   while ensuring that it is written in basic English that a child can
#   understand.
# - Get the `response` using the `get_response()` function.
#
# **Answer**
#
