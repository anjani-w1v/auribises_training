class FileHelper:

    def __init__(self, file_name='user1.csv'):
        self.file = open(file_name, 'a')

    def write_in_file(self, data):
        self.file.write(data)

    def close_file(self):
        self.file.close()