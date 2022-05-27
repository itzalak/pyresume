import os


class FileUtils:

    @staticmethod
    def locate_folder(path):
        """Check if the given path is a directory"""
        return os.path.isdir(path)

    @staticmethod
    def locate_file(path):
        print(path)
        """Check if the given path is a file"""
        return os.path.isfile(path)
