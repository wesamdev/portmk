import re

def parse(foldergame):
  # Define a regular expression pattern to match the desired values
  pattern = r'VALUE "(FileVersion|ProductName)"\s*,\s*"([^"]+)"'
  with open(foldergame+"\\"+"pck.txt", "r") as pck_file:
    pck = pck_file.read()
  # Find all matches in the version_info using the pattern
  matches = re.findall(pattern, pck)

  # Create a dictionary from the matches
  version_info_dict = dict(matches)

  # Access the values
  file_version = version_info_dict.get("FileVersion")
  product_name = version_info_dict.get("ProductName")

  print(f"FileVersion: {file_version}")
  print(f"ProductName: {product_name}")
  return file_version, product_name


