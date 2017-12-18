import os
def rename_file():

    #1 get the file name
    file_list=os.listdir(r"C:\Users\ABHISHEK\Downloads\neha")
    print(file_list)
    saved_path= os.getcwd()
    print("current working directory is"+saved_path)
    os.chdir(r"C:\Users\ABHISHEK\Downloads\neha")
    
    #2for each file, rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.strip("01234567789"))
        
    os.chdir(saved_path)


rename_file()
