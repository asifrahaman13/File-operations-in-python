class Index:
    def __init__(self, exclude_file):
        self.exclude_words = set()
        with open(exclude_file) as f:
            for word in f:
                self.exclude_words.add(word.strip().lower())
        self.index = {}

    def index_file(self, file_name, page_number):
        with open(file_name) as f:
            for line_number, line in enumerate(f):
                words = line.strip().lower().split()
                for word in words:
                    if word in self.exclude_words:
                        continue
                    if word not in self.index:
                        self.index[word] = set()
                    self.index[word].add(page_number)

    def write_index(self, output_file):
        with open(f"output_files/{output_file}", "w") as f:
            for word in sorted(self.index.keys()):
                pages = sorted(list(self.index[word]))
                pages_str = ",".join(str(p) for p in pages)
                f.write(f"{word} : {pages_str}\n")


index = Index("given_input_files/exclude-words.txt")
index.index_file("given_input_files/Page1.txt", 1)
index.index_file("given_input_files/Page2.txt", 2)
index.index_file("given_input_files/Page3.txt", 3)
index.write_index("index_set.txt")
