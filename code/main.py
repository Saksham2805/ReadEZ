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
    pass


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