# Import the string library to get valuable functions related to string

import string

# Create a class named BookIndex


class BookIndex:

    # Define the constructor of the class using the init
    def __init__(self, pages, exclude_words):

        # Define all the variables within the class
        self.pages = pages
        self.exclude_words = exclude_words
        self.index = {}

    # Define a function that reads the pages

    def read_pages(self):
        """Reads the pages of the book and stores them in a list"""
        self.page_texts = []
        for page in self.pages:
            # Open in read only mode
            with open(page, 'r') as f:
                # Store the texts of the page in the list
                self.page_texts.append(f.read())

    # Define a function which shall store the index og the words in the book

    def create_index(self):
        """Creates an index of words in the book pages"""
        # We already have the excluded set of words
        exclude_set = set(self.exclude_words)
        for i, page_text in enumerate(self.page_texts):
            # remove punctuation and split into words
            words = page_text.translate(str.maketrans(
                '', '', string.punctuation)).lower().split()
            for word in words:
                # If the word does not belongs to the exclude_set and it is not numeric then append to the index list
                if word not in exclude_set and word.isnumeric() == False:
                    if word not in self.index:
                        self.index[word] = set()
                    # add 1 to page number to avoid zero
                    self.index[word].add(i+1)

    # Save the index of the file through the function

    def save_index(self, filename):
        """Saves the index to a file"""
        # Open a file in write only mode
        with open(f"output_files/{filename}", 'w') as f:

            # First manually write the header
            f.write("Word : Page Numbers\n-------------------\n")

            # Sort the words in ascending order(which is by default sorting order)
            for word in sorted(self.index.keys()):
                pages = sorted(self.index[word])
                page_list = ','.join(str(page) for page in pages)
                # Write the data into the file
                f.write(f"{word} : {page_list}\n")

# Create a class ExcludeWords to exclude all the words of the file
class ExcludeWords():
    
    def __init__(self,excluded_file):
        self.excluded_file=excluded_file
        # Store the excluded words in the form of list
        self.exclude_words =[]
    

    def excluded_texts(self):

        '''Open the file in read only mode and exclude all the words present in the file'''
        
        with open(self.excluded_file,"r") as f:
            self.exclude_words=f.read().split()
        return self.exclude_words

# Define the main function

def main():

    # Enter the name of the text files in the form of txt
    pages = ['given_input_files/Page1.txt', 'given_input_files/Page2.txt', 'given_input_files/Page3.txt']
  
  
    # Create a object to get all the excluded words in the form of list
    exclude=ExcludeWords('given_input_files/exclude-words.txt')

    # Store the words in the form of list
    exclude_words=exclude.excluded_texts()

    '''  Create a BookIndex object named book.Pass the list of pages you want to include and the words you want to exluce'''

    book = BookIndex(pages, exclude_words)

    # Call the read_pages function to read all the included pages
    book.read_pages()

    # Call the create_index function to create all the indexes of the words
    book.create_index()

    # Save the output in the form of txt format
    book.save_index('index_string.txt')


if __name__ == '__main__':
    # Call the driving code of the program
    main()
