import os

class Paths():

    def __init__(self, path=None):
        
        self.root = self.get_root_path()

        if path is None:
            self.path = self.root    
        else:
            self.path = path

        subdirs = [directory for directory in os.listdir(self.path) if os.path.isdir(self.join_to_path(directory))]
        self.subdirs = subdirs
        self.set_subdirs(subdirs)        
        
        self.files = [file for file in os.listdir(self.path) if os.path.isfile(self.join_to_path(file))]
        self.filepaths = [self.join_to_path(file) for file in self.files]

    def set_subdirs(self, subdirs):

        for subdir in subdirs:
            setattr(self, subdir, Paths(self.join_to_path(subdir)))

    def join_to_path(self, path):

        return os.path.join(self.path, path)
    
    def get_root_path(self):

        current_dir = os.path.dirname(__file__)

        path = current_dir

        while True:
            for file in os.listdir(path):
                print(file)
                if file == '.root':
                    return path
                
            path = os.path.dirname(path)


