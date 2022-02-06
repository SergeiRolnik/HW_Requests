file_names = ["1.txt", "2.txt", "3.txt"]
write_file = "result.txt"

def read_file(file_name):
    f = open(file_name, encoding = "utf-8")
    file_data = []
    lines = f.readlines()
    file_data.append(len(lines)), file_data.append(file_name), file_data.append(lines)
    f.close()
    return file_data

def write_to_file(write_file, all_files_data):
    f = open(write_file, "a", encoding="utf-8")
    for file in all_files_data:
        f.write(file[1] + "\n")
        f.write(str(file[0]) + "\n")
        for line in file[2]:
            f.write(line)
    f.close()

all_files_data = []
for file in file_names:
    all_files_data.append(read_file(file))
all_files_data.sort()
write_to_file(write_file, all_files_data)