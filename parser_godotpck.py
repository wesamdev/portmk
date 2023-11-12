import re

def parse(game_folder):
    file_path = game_folder + "\\" + "pck.txt"
    
    with open(file_path, 'rb') as file:
        content_binary = file.read()

    # Decode the content
    content = content_binary.decode('utf-16le')  # Assuming the file is encoded in UTF-16LE

    print("File Content:")
    print(content)

    # Define patterns to extract product name and file version
    product_name_pattern = r'VALUE "ProductName",\s+"([^"]+)"'
    file_version_pattern = r'VALUE "FileVersion",\s+"([^"]+)"'

    # Search for matches in the content
    product_name_match = re.search(product_name_pattern, content, re.DOTALL)
    file_version_match = re.search(file_version_pattern, content, re.DOTALL)

    print("Product Name Match:")
    print(product_name_match)

    print("File Version Match:")
    print(file_version_match)

    # Extract the values from the matches
    product_name = product_name_match.group(1) if product_name_match else None
    file_version = file_version_match.group(1) if file_version_match else None

    return product_name, file_version
