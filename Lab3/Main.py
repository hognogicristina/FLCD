from Scanner import Scanner

if __name__ == "__main__":
    scanner = Scanner()
    scanner.read_tokens()
    program_file_name = "p1.txt"  # Replace with the actual program file name
    scanner.scan(program_file_name)
