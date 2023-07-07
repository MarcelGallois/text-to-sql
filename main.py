import gradio as gr
import sql_converter

converter = sql_converter.SQLConverter()

def convert_text_to_sql(text):
    sql = converter.convert_to_sql(text)
    valid_sql = converter.check_sql(text, sql)
    return valid_sql

iface = gr.Interface(fn=convert_text_to_sql, 
                     inputs="text", 
                     outputs="text",
                     title="Text to SQL Converter",
                     description="Enter a query to convert it into an SQL query.")
iface.launch()

