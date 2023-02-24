data_path =r'dsts.txt'
with open(data_path,'w') as file_manager:
    #file_manager.write('Hello,world\n')
    data = file_manager.readline()
    print(data)
    #file_manager.close()