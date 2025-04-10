import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_name, "r") as data:
        reader = json.load(data)
        if field in reader:
            sequencial_data = reader[field]
            return sequencial_data
        else:
            return "None"


def linear_search(seq, number):
    pos_list=[]
    count = 0
    for i, seq_number in enumerate(seq):
        if number == seq_number:
            pos_list.append(i)
            count += 1
        else:
            continue
    output_dict = {"positions": pos_list, "counts": count}
    return output_dict

def pattern_search(seq, pattern):
    pos_list = []
    for i in range(0, len(seq)-2):
        seq_pattern = seq[i] + seq[i+1] + seq[i+2]
        if pattern == seq_pattern:
            pos_list.append(i)
    return set(pos_list)

def main():
     read_unordered = read_data("sequential.json", "unordered_numbers")
     linear_search(read_unordered, 5)
     read_seq = read_data("sequential.json", "dna_sequence")
     print(pattern_search(read_seq, "ATA"))


if __name__ == '__main__':
    main()