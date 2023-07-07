import requests
import os
import openai

class OpenAIClient:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")

    def generate_text(self, text):
        response = openai.Edit.create(
            model="text-davinci-edit-001",
            input=text,
            instruction="Turn this text into an SQL query",
            
        )
        return response.choices[0].text.strip()

    def validate_sql(self, sql, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a very helpful SQL checking assistant. You will return the SQL statement if it is valid, and return a corrected version of it if it is not valid. The user will provide the intended behavior and then the sql that was generated for the user."},
                {"role": "user", "content": text},
                {"role": "system", "content": "The user will now supply the generated SQL statement."},
                {"role": "user", "content": sql}
            ]
        )
        return response.choices[0]['message']['content'].strip()


