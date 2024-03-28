def Write_to_file(filename, content):
  """
  Writes content to a new file in write mode.  

  Args:
  filename: The name of the file to write to.
  content: A list of strings or a single string to write to the file.
  """
  try:
    with open(filename, 'w') as file:
      if isinstance(content, list):
        file.writelines(content)
      else:
        file.write(content)
    print(f"Successfully wrote to {filename}")
  except PermissionError:
    print(f"Error: Insufficient permision to write to {filename}") 
  except Exception as e:
    print(f"An unexpected error occured: {e}")

def read_from_file(filename):
  """
  Reads the contentsof file and displays them on the console.

  Args:
    filename: The name of the file to read from.
    """
  try:
    with open(filename, 'r') as file:
      contents = file.read() 
      print(f"Contents of {filename}:\n{contents}") 
  except FileNotFoundError:
    print(f"Error: File {filename} not found")  
  except Exception as e:
    print(f"An unexpected error occuredd: {e}")  

def append_to_file(filename, content):
  """
  Appends content to an existing file in append mode.

  Args:
  filename: The name of the file to append to.
  content: A list of strings or a single string to append to the file.
  """
  try:
    with open(filename, 'a') as file:
      if isinstance(content, list):
        file.writelines(content) 
      else:
        file.write(content + "\n")  # Add for better formating
        print(f"Successfully appended to {filename}") 
  except PermissionError:
    print(f"Error: Insuffient permissions to append to {filename}") 
  except Exception as e:
    print(f"An unexpected error occured: {e}")

# Createthe file
content_to_write = [
  "Python is a versatile programing language.\n",
  "It is used in web development, data analysis and Artificial Inteligence.\n",
  "Learning python opens up many opportunity in tech industries.\n",
]  
Write_to_file("my_file.txt", content_to_write) 

# Read and display the file contents
read_from_file("my_file.txt")

# Append additional content
content_to_append = [
  "Today's weather forecast.\n",
  "Sunny with high 75F.\n",
  "No chances of raining today.\n",
]
append_to_file("my_file.txt", content_to_append)

# Read and display the file content again to see the appended text
read_from_file("my_file.txt")
  
