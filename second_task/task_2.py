def get_cats_info(path):
    try: 
        keys = ['id', 'name', 'age']
        list_of_elements = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                lines = line.strip().split(',')
                list_of_elements.append(dict(zip(keys, lines)))
            if not file.readlines():
                print('This file is empty!!')
            return list_of_elements
        
    except FileNotFoundError:
        return('File not found!!!') 
    except FileExistsError:
        return('Permission denied to read the file!!!')
    except Exception as e:
        return(f'An unexpected error occurred: {e}')


cats_info = get_cats_info("./cats_file.txt")
print(cats_info)




