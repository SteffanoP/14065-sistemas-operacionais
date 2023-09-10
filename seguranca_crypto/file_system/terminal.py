from fs2 import Filesystem

class Terminal:
    def __init__(self, filesystem: Filesystem):
        self.filesystem = filesystem

    def run(self):
        print("Welcome to the Terminal!")
        while True:
            command = input(f"{self.filesystem.current_folder}> ").strip()
            if command == "exit":
                break
            self.process_command(command)

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return

        main_command = parts[0]
        match main_command:
            case 'mkdir':
                if len(parts) < 2:
                    print("Usage: mkdir <folder_name>")
                else:
                    self.filesystem.mkdir(parts[1])
            case 'rmdir':
                if len(parts) < 2:
                    print("Usage: rmdir <folder_name>")
                else:
                    self.filesystem.rmdir(parts[1])
            case 'create':
                if len(parts) < 2:
                    print("Usage: create <file_name>")
                else:
                    content = input("Enter file content: ")
                    file_content = self.filesystem.create_file(parts[1], content)
                    content = input("Do you want to encrypt the file? (y/N): ") or 'N'
                    if content == 'y':
                        file_content.encrypt(self.filesystem.crypto_key)
            case 'read':
                if len(parts) < 2:
                    print("Usage: read <file_name>")
                else:
                    file = self.filesystem.read_file(parts[1])
                    file_content = file.read()
                    if isinstance(file_content, str):
                        print(file_content)
                        return

                    if isinstance(file_content, bytes):
                        content = input("The file is encrypted, give the key to decrypt it:") or 'N'
                        if content == 'N':
                            print("No key found, printing encrypted content:\n")
                            print(file_content.decode())
                            return

                        try:
                            file.decrypt(content)
                            print(file.content)
                            file.encrypt(content)
                        except ValueError:
                            print("Wrong key, printing encrypted content:\n")
                            print(file_content.decode())
                            return

            case 'rm':
                if len(parts) < 2:
                    print("Usage: rm <file_name>")
                else:
                    self.filesystem.remove_file(parts[1])
            case 'cd':
                if len(parts) < 2:
                    print("Usage: cd <folder_name>")
                else:
                    self.filesystem.cd(parts[1])
            case 'ls':
                contents = self.filesystem.ls()
                print("\n".join(contents))
            case 'frag':
                print(self.filesystem.calculate_fragmentation())
            case _:
                print(f"Unknown command: {main_command}")
