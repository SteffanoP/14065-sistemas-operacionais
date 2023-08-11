class File():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.next = None # IN CASE WE USE LINKED ALLOCATION

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
        """ Linked allocation for file """
        # BY CREATING A FILE THE USER NEED TO INFORM THE PATH OF IT. BUT SUPPOSING THIS PATH DOES NOT EXISTS,
        # SHOULD THE PROGRAM CREATE IT AUTOMATICALLY OR JUST TELL THE USER THE FOLDER DOES NOT EXIST?
        folder = self.find_path(custom_dir)
        if folder:
            new_file = file
            if not folder.files:
                folder.files = new_file # WOULD IT BE AN append() INSTEAD?
            else:
                current_file = File(folder.files)
                while current_file.next:
                    current_file = current_file.next
                current_file.next = new_file
                print(f"File '{name}' created in '{custom_dir}'.")
        else:
            print(f"Folder '{custom_dir}' not found.")
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

    # Command list contents from a directory
    def ls(self, path):
        dir = self.find_path(path)

        if dir:
            print(f"Contents of '{path}': ")
            if dir.files:
                current_file = File(dir.files)

                while current_file:
                    print(f"File: {current_file.name} ({current_file.size} bytes)")
                    current_file = current_file.next # IN CASE WE USE LINKED ALLOCATION
            
            if Folder(dir.subdirectories): # DOES THIS WORKS LOGICALLY?
                for subdirectory in dir.subdirectories:
                    print(f"Subfolder: {subdirectory.name}")

    def find_path(self, path):
        folders = path.split("/")
        current_folder = Folder(self.current_dir)

        for folder_name in folders:
            found = False
            for subfolder in current_folder:
                if subfolder.name == folder_name:
                    current_folder = subfolder
                    found = True
                    break
            if not found:
                return None
        return current_folder
        
    def __set_current_dir__(self, directory):
        self.current_dir = directory
    