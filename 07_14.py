
source_file = "file15.txt"
output_file = "new_file15.txt"

def to_indexed(source_file, output_file):

    with open(source_file, "r") as fn, open(output_file, "w") as f:
        for num, line in enumerate(fn):
                text = f"{num}: {line}"
                f.write(text)

to_indexed(source_file, output_file)