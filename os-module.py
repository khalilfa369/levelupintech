#importing the os module
import os

#creating the function
def get_file_info(dir_path='.'):

    #file infor lis
    
    file_info_list = []

    #try-except block to enable error handeling
    try:
        for foldername, subfolders, filenames in os.walk(dir_path):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                file_size = os.path.getsize(filepath)
                file_info_list.append({
                    'name': filename,
                    'path': filepath,
                    'size': file_size
                })
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return file_info_list

if __name__ == "__main__":
    # Ask the user to enter a path, and store it in a variable
    user_path = input("Please enter the directory path (press enter to use the current working directory): ")
    
    # If user_path is an empty string, call the function without a parameter
    # Otherwise, call it with the user provided path
    info = get_file_info(user_path) if user_path else get_file_info()
    
    
    
    data = info

# Header
print(f"{'Name':<20} {'Size (bytes)':<15} {'Path':<30}")
print('-' * 65)  # Adding a separator line

# Data
for file_info in data:
    print(f"{file_info['name']:<20} {file_info['size']:<15} {file_info['path']:<30}")

