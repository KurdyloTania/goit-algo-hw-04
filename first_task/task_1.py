import re

def total_salary(path):
    salary_list = []
    total = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            contents = file.read()
            if not contents:
                'This file is empty!!'
                return 0, 0
            paterns = r'[,\n]'
            list_of_elements = re.split(paterns, contents)
            for element in list_of_elements:
                if int(element.isdigit()):
                    element = int(element)
                    salary_list.append(element)
            
            for number in salary_list:
                total += number
                average = total // len(salary_list)
                
            return total, average
    except FileNotFoundError:
        print('File not found!!!')
        return 0, 0 
    except FileExistsError:
         print('Permission denied to read the file!!!')
         return 0, 0
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return 0, 0

                   
total, average = total_salary("./salary_file.txt")
print(f"Total salary: {total}, Average salary: {average}")