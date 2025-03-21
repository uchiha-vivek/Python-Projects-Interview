import os


def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f'File {filename} : created successfully')
    except FileExistsError:
        print(f'File {filename} already exists !')
    except Exception as e:
        print('An error occured')

""" View all the files """
def view_all_files():
    files=os.listdir()
    if not files:
        print('No files found')
    else:
        print('Files found in directory')
        for file in files:
            print(file)        

""" Deleting the Files  """
def delete_files(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been removed successfully')
    except FileNotFoundError :
        print('File Not found')
    except Exception as e :
        print('Some error occured')


""" Read all files """
def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f'Content of file is : \n{content}')
    except FileNotFoundError :
        print(f"{filename} does not exist")
    except Exception as e:
        print('An error occured')

"""Edit the file"""
def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input('Enter the data :')
            f.write(content+"\n")
            print(f'content added to {filename}')
    except FileNotFoundError :
        print('file not found error')
    except Exception as e:
        print('Error occured')


def main():
    while True:
        print('FILE MANAGEMENT TERMINAL APP')
        print('1: Create file')
        print('2: View all files')
        print('3: Delete files')
        print('4: Read files')
        print('5: Edit file')
        print('6: Exit')
        choice=input('Enter your choice from (1-6) :')
        if choice=='1':
            file_name = input('Enter file name to create :')
            create_file(file_name)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            file_name=input('enter the name of file you want to delete :')
            delete_files(file_name)
        elif choice=='4':
            file_name = input('Enter file you want to read : ')
            read_file(file_name)
        elif choice=='5':
            file_name=input('Enter the file you want to edit')
            edit_file(file_name)
        elif choice=='6':
            print('Closing the app....')
            break
        else: 
            print('Invalid choice !')


if __name__=="__main__":
    main()