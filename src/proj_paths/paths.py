import os
import re

class Paths():
    """
    A pythonic way of accessing your project file directory
    
    A python object that allows easy access to all of your
    project files and directories.
    
    Attributes
    ----------
    root: str 
        Root directory of the project. Determined by first .root file
        found moving up from cwd
    path: str
        Full path to directory associated with the Paths object
    subdirs: list
        List of directories beneath the current Paths directory
    files: list
        List of files in Paths directory
    filepaths: list
        List of files as absolute paths in Paths directory
    
    Methods
    ---------
    None yet
    """
    
    def __init__(self, path=None, root=None, quiet=True, use_cwd=True):

        if root is None: 
            self.root = self.get_root_path()
        else:
            self.root = root

        if path is None:
            self.path = self.root    
        else:
            self.path = path

        self.use_cwd = use_cwd

        subdirs = [directory for directory in os.listdir(self.path) if os.path.isdir(self.join_to_path(directory))]
        self.subdirs = subdirs
        self.set_subdirs(subdirs)        
        
        self.files = [file for file in os.listdir(self.path) if os.path.isfile(self.join_to_path(file))]
        self.filepaths = [self.join_to_path(file) for file in self.files]

        if quiet is False and self.root is self.path:
            print(f"Root directory: {self.root}")

    def __repr__(self):
        """Represent object as class name and path"""

        return f"<{str(self.__class__).strip('<>')}: {self.path}>"

    def set_subdirs(self, subdirs):
        """Create Paths objects for each subdir"""

        for subdir in subdirs:
            setattr(self, subdir, Paths(self.join_to_path(subdir), self.root))

    def join_to_path(self, path):
        """Join path to objects internal path"""

        return os.path.join(self.path, path)
    
    def get_root_path(self):
        """Walk up directories from `cwd` or `__file__` until `.root` file is found
        Set that to root directory of the project"""

        if self.use_cwd:
            current_dir = os.getcwd()
        else:
            current_dir = __file__

        path = current_dir

        while path != os.environ['HOME']:
            for file in os.listdir(path):
                if file == '.root':
                    return path
                
            path = os.path.dirname(path)
        
        raise IOError(".root file not found")
    
    def search_files(self, substring):
        """Search files in path by substring"""

        files = [file for file in self.filepaths if substring in file]

        if len(files) == 1:
            return files[0]

        return files

if __name__ == '__main__':
    pass
