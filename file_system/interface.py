import fs2, terminal

# Example usage
fs = fs2.Filesystem(block_size=100, total_blocks=1024)
terminal = terminal.Terminal(fs)
terminal.run()
