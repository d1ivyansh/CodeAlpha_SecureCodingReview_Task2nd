#Let's choose Python as the programming language for this review. 

import os

def delete_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            os.remove(os.path.join(directory, filename))

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    delete_files(directory)
    print("Files deleted successfully.")



