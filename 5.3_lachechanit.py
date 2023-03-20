import re


# Define an iterator function that yields secret messages from a block of text
def extract_secret_messages(text_block):
    messages = re.findall(r'\b[a-z]{5,}!\b', text_block)
    yield from messages


# Define an iterator class that reads a file in blocks and yields each block
class ReadFileInBlocks:
    def _init_(self, filename, block_size=4096):
        self.filename = filename
        self.block_size = block_size

    def _iter_(self):
        with open(self.filename, 'rb') as f:
            while True:
                block = f.read(self.block_size)
                if not block:
                    break
                yield block


# Use the iterators to read the logo file and extract secret messages
for block in ReadFileInBlocks('logo.jpg'):
    text_block = block.decode('ascii', errors='ignore')
    for message in extract_secret_messages(text_block):
        print(message)