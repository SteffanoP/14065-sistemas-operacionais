class File():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.next = None # IN CASE WE USE LINKED ALLOCATION

    def has_the_same_name(self, another_name: str) -> bool:
        return another_name == self.name

class Folder():
    def __init__(self, name, current_dir) -> None:
        self.name = name
        self.previous_folder = current_dir
        self.subdirectories = []
        self.files = []

class FileSystem():
    def __init__(self, size) -> None:
        self.max_size = size
        self.root_dir = Folder('/', current_dir=None)
        self.current_dir = self.root_dir
        self.directories = []

    def create_file(self, name: str, size: int, *, custom_dir: str = None):
        """ Linked allocation for file """
        # BY CREATING A FILE THE USER NEED TO INFORM THE PATH OF IT. BUT SUPPOSING THIS PATH DOES NOT EXISTS,
        # SHOULD THE PROGRAM CREATE IT AUTOMATICALLY OR JUST TELL THE USER THE FOLDER DOES NOT EXIST?
        if custom_dir is None:
            custom_dir = self.current_dir.name

        if custom_dir != '/':
            folder = self.find_path(custom_dir)
        else:
            folder = self.root_dir

        if isinstance(folder, Folder):
            is_file_in_folder = False
            for folder_file in folder.files:
                if folder_file.has_the_same_name(name):
                    is_file_in_folder = True

            if not is_file_in_folder:
                file = File(name, size)
                folder.files.append(file)
                print(f"File '{name}' created in '{custom_dir}'.")
                return

            print(f"File {name} already exists in {custom_dir}.")
            return

        print(f"Folder '{custom_dir}' not found.")

    def create_folder(self, name) -> None:
        if name[-3::] == '../':
            if self.current_dir.previous_folder is None:
                print("Operation not permitted on root folder")
                return

            self.cd('../')

        final_name = name[2::] if name[-2::] == './' else name
        folder = Folder(final_name, current_dir=self.current_dir)
        self.directories.append(folder)
        self.current_dir += final_name
        return

    # Command change directory
    def cd(self, new_directory):
        dir = self.find_path(new_directory)

        if dir:
            for folder in self.current_dir.subdirectories:
                folder_info = Folder(folder)
                if folder_info.name == dir.name:
                    self.__set_current_dir__(dir)
        else:
            print("The system did not find the specified path.")

    # Command list contents from a directory
    def ls(self, path = None) -> None:
        folder = self.current_dir if path is None else self.find_path(path)

        if isinstance(folder, Folder):
            print(f"Contents of '{path}': ")
            for file in folder.files:
                print(f"File: {file.name} ({file.size} bytes)")

            for subdirectory in folder.subdirectories:
                print(f"Subfolder: {subdirectory.name}")

    def delete(self, name):
        pass

    def find_path(self, path):
        if path == '/':
            return self.root_dir

        if path == './':
            return self.current_dir

        if path == '../' and self.current_dir != self.root_dir:
            return self.current_dir.previous_folder

        folders = path.split("/")
        current_folder = self.current_dir

        for folder_name in folders:
            found = False
            for subfolder in current_folder.subdirectories:
                if subfolder.name == folder_name:
                    current_folder = subfolder
                    found = True
                    break
            if not found:
                return None
        return current_folder
        
    def __set_current_dir__(self, directory):
        self.current_dir = directory
    