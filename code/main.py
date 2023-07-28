#   #   import statements   #   #
# for reading data
import os
# for conversion of pdf to text
import fitz


def read_pdf(name):
    """
    Function to read text data from the given pdf file
    Returns the data in form of dictionary:
    key->pg no  value-> text on that page
    """
    # text storage
    data = {}
    # storage directory path
    dir_path = '../input_data'
    # check if the file is present in the directory
    try:
        file_path = os.path.join(dir_path, name)
        # if it exists
        if os.path.exists(file_path):
            # we read the data
            with fitz.open(file_path) as pdf_doc:
                for page_num in range(pdf_doc.page_count):
                    text = pdf_doc.load_page(page_num).get_text()
                    if text:
                        data[page_num+1] = text
        else:
            print(f"The file '{name}' does not exist in the directory '{dir_path}'.")
    except Exception as e:
        print(f"An error occured:{e}")
    finally:
        return data
    

def generate_summary(text, from_page, to_page):
    """
    Code to generate the summary of the given text data from the
    requested page till the given page number
    Returns a string as result
    """
    pass


if __name__ == '__main__':
    FILE_PATH = input("Enter the name of the file")
    FROM = int(input("Enter starting page number"))
    TO = int(input("Enter ending page number"))
    # reading the file from the directory
    TEXT = read_pdf(FILE_PATH)
    summary = generate_summary(TEXT, FROM, TO)
    print(summary)