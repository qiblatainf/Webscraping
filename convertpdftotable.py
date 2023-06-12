import tabula
import pandas as pd

def convert_pdf_to_table(url):
    try:
        # Read the PDF from the URL
        df = tabula.read_pdf(url, pages='all', multiple_tables=True)

        # Concatenate all tables into a single DataFrame
        combined_df = pd.concat(df)

        # Reset the index of the DataFrame
        combined_df.reset_index(drop=True, inplace=True)
        

        return combined_df

    except Exception as e:
        print(f"Error: {e}")
        return None

# URL of the PDF file
pdf_url = "https://www.sbp.org.pk/ecodata/kibor/2023/Jun/Kibor-01-Jun-23.pdf"

# Convert PDF to table
result_df = convert_pdf_to_table(pdf_url)

if result_df is not None:
    print(result_df)
    result_df.to_excel("output.xlsx")
else:
    print("Failed to convert PDF to table.")
