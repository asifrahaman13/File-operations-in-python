# Import the re library which will provide convenient way to check regular expressions /string

import re


'''Create a class named BookIndex'''


class BookIndex:

    '''Define the constructor and assign the value of the variables'''


    def __init__(self, pages_filenames, exclude_words_filename, index_filename):
        self.pages_filenames = pages_filenames
        self.exclude_words_filename = exclude_words_filename
        self.index_filename = index_filename
        # Create a dictionary to store the information about the words and the index pages
        self.index = {}

    
    # The function adds the correct words to the index dictionary
    def build_index(self):
        # Call the _read_words_file function to exclude the words to ignore from the required file
        exclude_words = self._read_words_file(self.exclude_words_filename)
        
        for page_num, page_filename in enumerate(self.pages_filenames, start=1):
            page_words = self._read_words_file(page_filename)
            # If a word in not in excluded words and not a numeric word then add this to the dictionary
            for word in page_words:
                if word not in exclude_words and word.isnumeric()==False:
                    if word not in self.index:
                        self.index[word] = set()
                    self.index[word].add(page_num)
    

    '''The function allows to write the desired outpout into the file'''

    def write_index(self):
        # Open any file in the write only mode
        with open(f"output_files/{self.index_filename}", 'w') as f:
            # Manually write the header first in the file
            f.write("Word : Page Numbers\n-------------------\n")

            # Sort the items (by default in asceding order)
            for word, pages in sorted(self.index.items()):
                pages_str = ', '.join(map(str, sorted(pages)))
                f.write(f"{word} : {pages_str}\n")
    
    '''The function allows to read the txt file'''
    def _read_words_file(self, filename):
        # Open the file in read only mode
        with open(filename, 'r') as f:
            text = f.read()
        words = re.findall(r'\b\w+\b', text.lower())
        # Return set object of words
        return set(words)


def main():
    
    # Create an object and enter the necessary arguments
    book_index = BookIndex(
    pages_filenames=['given_input_files/Page1.txt', 'given_input_files/Page2.txt', 'given_input_files/Page3.txt'],
    exclude_words_filename='given_input_files/exclude-words.txt',
    index_filename='index_re.txt'
    )
    
    # Call the functions to perform the required task
    book_index.build_index()
    book_index.write_index()


'''Call the main function to drive the code'''
if __name__ == '__main__':

    main()