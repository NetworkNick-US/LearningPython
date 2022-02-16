class NetworkLogger:

    def __init__(self, file_name):
        self.log_file = str(file_name)

    def log(self, data):
        with open(self.log_file, 'a') as f:
            f.write("=" * 50 + '\n')
            f.write(data + '\n')
            f.write("=" * 50 + '\n')
