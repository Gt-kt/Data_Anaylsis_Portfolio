import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

def analyze_csv_data(csv_file_path, question):
    try:
        df = pd.read_csv(csv_file_path)
        
        llm = OpenAI(
            api_token="Your API ",
            model="gpt-4o",
            temperature=0.2
        )
        
        smart_df = SmartDataframe(df, config={"llm": llm})
        
        response = smart_df.chat(question)
        
        return response
    
    except Exception as e:
        return f"Error analyzing data: {str(e)}"

def main():
    csv_file = r"C:\Users\c\Downloads\Bank_analysis\Pandas_AI\Data\fortune1000_2024.csv" 
    
    # Sample questions you can ask about your data
    sample_questions = [
        "What is the basic statistical summary of the dataset?",
        "Show me the correlation between columns",
        "What are the main trends in this data?",
        "Can you identify any outliers?",
        "Generate visualizations for key insights"
       
    ]
    
    for question in sample_questions:
        print(f"\nQuestion: {question}")
        result = analyze_csv_data(csv_file, question)
        print(f"Analysis Result: {result}")

if __name__ == "__main__":
    main()
