class File():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Folder():
    def __init__(self, name) -> None:
        self.name = name
        self.subdirectories = []
        self.files = []

class FileSystem():
    def __init__(self, size) -> None:
        self.max_size = size
        self.current_dir = '/'
        self.directories = []

    def create_file(self, name: str, size: int, *, custom_dir: str):
        file = File(name, size)
        # TODO: Allocation for file
        pass

    def create_folder(self, name) -> None:
        if name[-3::] == '../':
            # TODO: Create allocation for directory for this case
            return

        final_name = name[2::] if name[-2::] == './' else name
        folder = Folder(final_name)
        self.directories.append(folder)
        self.current_dir += final_name
        return

    # Command change directory
    def cd(self, new_directory):
        pass
        
    def __set_current_dir__(self, directory):
        self.current_dir = directory
    