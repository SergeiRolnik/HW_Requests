file_names = ["1.txt", "2.txt", "3.txt"]
all_files_data = []
for file_name in file_names:
    f = open(file_name, encoding = "utf-8")
    current_file_data = []
    lines = f.readlines()
    current_file_data.append(len(lines)), current_file_data.append(file_name), current_file_data.append(lines)
    all_files_data.append(current_file_data)
    f.close()
all_files_data.sort()
f_result = open("result.txt", "a", encoding ="utf-8")
for file in all_files_data:
    f_result.write(file[1] + "\n")
    f_result.write(str(file[0]) + "\n")
    for line in file[2]:
        f_result.write(line)
f_result.close()