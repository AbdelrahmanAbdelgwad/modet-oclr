import re


def remove_all_zeros(file_list):
    # Define a regular expression pattern to match strings with all zeros in the filename
    pattern = re.compile(r"00000")

    # Filter out strings with all zeros in the filename
    filtered_list = [item for item in file_list if not pattern.search(item)]

    return filtered_list


# Example usage:
file_list = ["bear/00001.jpg", "cat/02345.jpg", "dog/00000.jpg", "bird/00123.jpg"]
result_list = remove_all_zeros(file_list)

print(result_list)
