class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def write(self, content):
        self.content = content

    def read(self):
        return self.content

    def __str__(self):
        return self.name


class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def remove_item(self, item):
        self.contents.remove(item)

    def get_contents(self):
        return self.contents

    def __str__(self):
        return self.name


class Filesystem:
    def __init__(self, size):
        self.root = Folder("root")
        self.current_folder = self.root
        self.size = 50
        self.current_size = 0
        self.blocks = []

    def mkdir(self, name):
        new_folder = Folder(name)
        self.current_folder.add_item(new_folder)

    def create_file(self, name, content=""):
        new_current_size = len(content) + self.current_size
        if new_current_size > self.size:
            print("The disk is full! Try cleaning unused files.")
            return

        new_file = File(name, content)
        self.current_folder.add_item(new_file)

    def cd(self, folder_name):
        if folder_name == "..":
            if self.current_folder != self.root:
                self.current_folder = self._get_parent_folder(self.current_folder)
        else:
            folder = self._get_subfolder(self.current_folder, folder_name)
            if folder:
                self.current_folder = folder

    def ls(self):
        return [str(item) for item in self.current_folder.get_contents()]

    def _get_subfolder(self, folder, name):
        for item in folder.get_contents():
            if isinstance(item, Folder) and item.name == name:
                return item
        return None

    def _get_parent_folder(self, folder):
        # Traverse the filesystem to find the parent folder of the current folder
        # This function assumes a simple folder structure without loops
        return self._find_parent(self.root, folder)

    def _find_parent(self, current, target):
        for item in current.get_contents():
            if isinstance(item, Folder):
                if item == target:
                    return current
                result = self._find_parent(item, target)
                if result is not None:
                    return result
        return None
