# remove_vocab_counts.py

def remove_counts(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            token = line.split()[0]  # Assumes count is separated by space and is after the token
            outfile.write(token + '\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python remove_vocab_counts.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file, output_file = sys.argv[1], sys.argv[2]
    remove_counts(input_file, output_file)
