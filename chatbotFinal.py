import gradio as gr
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nalini2004",
    database="employee"
)

def execute_query(query):
    try:
        # Execute SQL query
        cursor = conn.cursor()
        cursor.execute(query)
        
        # Fetch data
        result = cursor.fetchall()
        
        if result:
            # Return fetched data
            return result
        else:
            return "No data found."
        
        # Close database connection
        cursor.close()
    except Exception as e:
        return f"Error executing SQL query: {e}"

#import gradio as gr
import google.generativeai as genai

# Configure the Generative AI with your API key
genai.configure(api_key="AIzaSyDoR10wPWSnCCLXHZWWrlrAg7XCXFzzpx8")  # Replace "YOUR_API_KEY" with your actual API key

# Create a GenerativeModel instance
model = genai.GenerativeModel(model_name="gemini-pro")

# Define the chat_with_gemini function to interact with the Generative AI
def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text  # Extract the generated text from the response object

def chatbot_response(user_input):
    if user_input.lower() in ["quit", "exit", "bye"]:
        return "Goodbye!"
    response = chat_with_gemini("give the sql command for "+user_input)
    #response = chat_with_gemini(user_input)
    if "employee" in response:
        response = chat_with_gemini("give the sql command for "+user_input+" in employee_data table")

    trimmed_res = response[6:-3]

    res=execute_query(trimmed_res)



    return res

inputs = gr.Textbox(lines=2, label="You")
output = gr.Textbox(label="Chatbot")

gr.Interface(fn=chatbot_response, inputs=inputs, outputs=output).launch()
