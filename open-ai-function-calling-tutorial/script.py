import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

student_1_description = "David Nguyen is a sophomore majoring in computer science at Stanford University. He is Asian American and has a 3.8 GPA. David is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after graduating." OpenAIWas this helpful? Yes No


# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_1}]
)

openai_response.choices[0].message.content

'{\n  "name": "David Nguyen",\n  "major": "computer science",\n  "school": "Stanford University",\n  "grades": "3.8 GPA",\n  "club": "Robotics Club"\n}' OpenAIWas this helpful? Yes No


import json

# Loading the response as a JSON object
json_response = json.loads(openai_response.choices[0].message.content)
json_response

student_2_description="Ravi Patel is a sophomore majoring in computer science at the University of Michigan. He is South Asian Indian American and has a 3.7 GPA. Ravi is an active member of the university's Chess Club and the South Asian Student Association. He hopes to pursue a career in software engineering after graduating." OpenAIWas this helpful? Yes No


# Generating response back from gpt-3.5-turbo
openai_response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': prompt_2}]
)

# Loading the response as a JSON object
json_response = json.loads(openai_response.choices[0].message.content)
json_response

{'name': 'David Nguyen', 'major': 'computer science', 'school': 'Stanford University', 'grades': 3.8, 'club': 'Robotics Club'} 

{'name': 'Ravi Patel', 'major': 'computer science', 'school': 'University of Michigan', 'grades': 3.7, 'club': 'Chess Club'}

school_1_description = "Stanford University is a private research university located in Stanford, California, United States. It was founded in 1885 by Leland Stanford and his wife, Jane Stanford, in memory of their only child, Leland Stanford Jr. The university is ranked #5 in the world by QS World University Rankings. It has over 17,000 students, including about 7,600 undergraduates and 9,500 graduates23. "


{'name': 'David Nguyen', 'major': 'computer science', 'school': 'Stanford University', 'grades': 3.8, 'club': 'Robotics Club'} 

{'name': 'Stanford University', 'ranking': 5, 'country': 'United States', 'no_of_students': 17000}

def extract_student_info(name, major, school, grades, club):
    
    """Get the student information"""

    return f"{name} is majoring in {major} at {school}. He has {grades} GPA and he is an active member of the university's {club}."

def extract_school_info(name, ranking, country, no_of_students):
    
    """Get the school information"""

    return f"{name} is located in the {country}. The university is ranked #{ranking} in the world with {no_of_students} students."



descriptions = [
    student_1_description, 
    "Who was a Abraham Lincoln?",
    school_1_description
    ]

for i, sample in enumerate(descriptions):
    response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [{'role': 'user', 'content': sample}],
    functions = custom_functions,
    function_call = 'auto'
    )
    
    response_message = response.choices[0].message
    
    if dict(response_message).get('function_call'):
        
    # Which function call was invoked
    function_called = response_message.function_call.name
        
    # Extracting the arguments
    function_args  = json.loads(response_message.function_call.arguments)
        
    # Function names
    available_functions = {
    "extract_school_info": extract_school_info,
    "extract_student_info": extract_student_info
    }
        
    fuction_to_call = available_functions[function_called]
    response_message = fuction_to_call(*list(function_args .values()))
        
    else:
    response_message = response_message.content
    
    print(f"\nSample#{i+1}\n")
    print(response_message)

Sample#1

David Nguyen is majoring in computer science at Stanford University. He has 3.8 GPA and he is an active member of the university's Robotics Club.

Sample#2

Abraham Lincoln was the 16th President of the United States. He served as president from March 1861 until his assassination in April 1865. Lincoln led the country through its greatest internal crisis, the American Civil War, and his Emancipation Proclamation declared slaves in Confederate territory to be free. He is known for his leadership, his commitment to preserving the Union, and his efforts to abolish slavery. Lincoln's presidency is widely regarded as one of the most transformative in American history.

Sample#3

Stanford University is located in the United States. The university is ranked #5 in the world with 17000 students.

