import tabula
import pandas as pd

def convert_pdf_to_table(pdf_urls):
    try:
        # Create a Pandas Excel writer
        excel_writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")

        # Iterate over the PDF URLs and process each PDF
        for i, pdf_url in enumerate(pdf_urls):
            # Process the PDF and convert it to a DataFrame
            # Assuming you have a function named `process_pdf_to_dataframe()` that takes a PDF URL and returns a DataFrame
            df = tabula.read_pdf(pdf_url, pages='all', multiple_tables=True)
            
            # Concatenate all tables into a single DataFrame
            combined_df = pd.concat(df)

            # Reset the index of the DataFrame
            combined_df.reset_index(drop=True, inplace=True)
            

            # Write the DataFrame to a new sheet in the Excel file
            sheet_name = f"Sheet{i+1}"  # Sheet name based on the iteration
            combined_df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

        # Save the Excel file
        excel_writer.save()


    except Exception as e:
        print(f"Error: {e}")
        return None

# URL of the PDF file
# pdf_url = "https://www.sbp.org.pk/ecodata/kibor/2023/Jun/Kibor-01-Jun-23.pdf"

# Convert PDF to table
# result_df = convert_pdf_to_table(pdf_url)

# if result_df is not None:
#     print(result_df)
#     result_df.to_excel("output.xlsx")
# else:
#     print("Failed to convert PDF to table.")
