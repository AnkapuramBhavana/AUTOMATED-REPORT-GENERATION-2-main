import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def read_data(file_path):
    """Reads data from a CSV file and returns a DataFrame."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    return pd.read_csv(file_path)

def format_dataframe(df):
    """Formats the DataFrame as a readable string with spacing."""
    return df.to_string(index=False)

def analyze_data(df):
    """Performs basic data analysis and returns a summary."""
    if df is None or df.empty:
        return "No data available for analysis."
    return df.describe().to_string()

def generate_pdf(report_path, data_content, summary):
    """Generates a PDF report with CSV contents followed by the analysis report."""
    
    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter

   
    c.setFont("Times-Roman", 18)
    c.drawString(200, height - 50, "Data Analysis Report")

   
    def add_text(text, start_y, spacing=15):
        y = start_y
        text_lines = text.split("\n")
        c.setFont("Times-Roman", 11)
        for line in text_lines:
            if y < 50:  
                c.showPage()
                c.setFont("Times-Roman", 11)
                y = height - 50  
            c.drawString(50, y, line)
            y -= spacing  
        return y

  
    c.setFont("Times-Roman", 13)
    c.drawString(50, height - 80, "CSV File Contents:")
    y_position = add_text(data_content, height - 100, spacing=18)

 
    y_position -= 30

    
    c.setFont("Times-Roman", 13)
    c.drawString(50, y_position, "Data Analysis Summary:")
    add_text(summary, y_position - 20, spacing=18)

    c.save()

def main():
    input_file = r"c:\Users\hp\Documents\reports\top_software_engineer_jobs.csv" #ADD CSV FILE PATH HERE
    output_pdf = r"c:\Users\hp\Documents\reports\report.pdf"
    
    df = read_data(input_file)
    if df is not None:
        data_content = format_dataframe(df)  
        summary = analyze_data(df)  
        generate_pdf(output_pdf, data_content, summary)
        print(f"Report generated successfully at {output_pdf}!")

if __name__ == "__main__":
    main()


