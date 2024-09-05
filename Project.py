import pandas as pd

def display_excel_content(file_path, sheet_name=None):
    """
    Function to read an Excel file and display its content in a tabular format.
    
    Parameters:
    - file_path: str, the path to the Excel file.
    - sheet_name: str or None, the sheet to read from the Excel file. If None, the first sheet is read.
    """
    try:
        # Read the Excel file
        if sheet_name:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        else:
            df = pd.read_excel(file_path)

        # Display the DataFrame
        print("Data from the Excel file:")
        print(df.to_markdown(tablefmt="grid", index=False))
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the path to your Excel file
    file_path = input("Enter the path of the Excel file: ")
    sheet_name = input("Enter the sheet name (or press Enter to use the first sheet): ")
    sheet_name = sheet_name.strip() if sheet_name else None

    # Display the Excel content
    display_excel_content(file_path, sheet_name)
