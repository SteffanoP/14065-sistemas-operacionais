class Terminal:
    def __init__(self, filesystem):
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
            case 'create':
                if len(parts) < 2:
                    print("Usage: create <file_name>")
                else:
                    content = input("Enter file content: ")
                    self.filesystem.create_file(parts[1], content)
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
