from cryptography.fernet import Fernet


class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def write(self, content):
        self.content = content

    def encrypt(self, key):
        fernet = Fernet(key)
        self.content = fernet.encrypt(str(self.content).encode())

    def decrypt(self, key):
        fernet = Fernet(key)
        self.content = fernet.decrypt(self.content).decode()

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
    def __init__(self, block_size=1024, total_blocks=100):
        self.root = Folder("root")
        self.current_folder = self.root
        self.block_size = block_size
        self.total_blocks = total_blocks
        self.free_blocks = total_blocks
        self.allocated_blocks = set()
        self.crypto_key = Fernet.generate_key()
        print("Chave criptográfica do Sistema: ", self.crypto_key.decode())

    def allocate_blocks(self, num_blocks):
        if num_blocks <= self.free_blocks:
            allocated = set()
            for _ in range(num_blocks):
                block_id = self._find_free_block()
                self.allocated_blocks.add(block_id)
                allocated.add(block_id)
                self.free_blocks -= 1
            return allocated
        else:
            return None

    def deallocate_blocks(self, blocks):
        self.allocated_blocks -= set(blocks)
        self.free_blocks += len(blocks)

    def _find_free_block(self):
        for block_id in range(self.total_blocks):
            if block_id not in self.allocated_blocks:
                return block_id
        raise Exception("No free blocks available.")

    def mkdir(self, name):
        new_folder = Folder(name)
        self.current_folder.add_item(new_folder)

    def rmdir(self, folder_name):
        for item in self.current_folder.get_contents():
            if isinstance(item, Folder) and item.name == folder_name:
                if item.get_contents():
                    print(f"Directory '{folder_name}' is not empty. Cannot remove.")
                else:
                    self.current_folder.remove_item(item)
                    print(f"Directory '{folder_name}' removed.")
                return
        print(f"Directory '{folder_name}' not found.")

    def create_file(self, name, content=""):
        num_blocks_needed = (len(content) + self.block_size - 1) #self.block_size
        allocated_blocks = self.allocate_blocks(num_blocks_needed)
        if allocated_blocks is not None:
            new_file = File(name, content)
            self.current_folder.add_item(new_file)
            return new_file

        print("Insufficient free space to create the file.")
        
    def read_file(self, file_name):
        for item in self.current_folder.get_contents():
            if isinstance(item, File) and item.name == file_name:
                return item
        print(f"File '{file_name}' not found.")
        return None

    def remove_file(self, file_name):
        for item in self.current_folder.get_contents():
            if isinstance(item, File) and item.name == file_name:
                self.deallocate_blocks(self.allocated_blocks)
                self.current_folder.remove_item(item)
                print(f"File '{file_name}' removed.")
                return
        print(f"File '{file_name}' not found.")

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

    def calculate_fragmentation(self):
        allocated_blocks_list = sorted(list(self.allocated_blocks))
        fragmentation = 0
        for i in range(1, len(allocated_blocks_list)):
            fragmentation += allocated_blocks_list[i] - allocated_blocks_list[i - 1] - 1
        return fragmentation
