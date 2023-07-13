def sort_file(input_file):
    input_file = open('INPUT_HERE/'+input_file,'r')
    Earth_Space = open('OUTPUT\Earth_Space.txt','a')
    Energy = open('OUTPUT\Energy.txt','a')
    Math = open('OUTPUT\Math.txt','a')
    Life_Science = open('OUTPUT\Life_Science.txt','a')
    Physical_Science = open('OUTPUT\Physical_Science.txt','a')
    General_Science = open('OUTPUT\General_Science.txt','a')

    input_list = []

    for row in input_file:
        input_list.append(row)
    ran = 0
    for item in input_list:
        if ('Earth and Space' in item) or ('EARTH SCIENCE' in item):
            for item in input_list[ran-1:]:
                Earth_Space.write(item)
                if 'ANSWER:' in item:
                    Earth_Space.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
        if ('Energy' in item):
            for item in input_list[ran-1:]:
                Energy.write(item)
                if 'ANSWER:' in item:
                    Energy.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
        if ('Math' in item) or ('MATH' in item):
            for item in input_list[ran-1:]:
                Math.write(item)
                if 'ANSWER:' in item:
                    Math.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
        if ('Life Science' in item) or ('LIFE SCIENCE' in item):
            for item in input_list[ran-1:]:
                Life_Science.write(item)
                if 'ANSWER:' in item:
                    Life_Science.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
        if ('Physical Science' in item) or ('PHYSICAL SCIENCE' in item):
            for item in input_list[ran-1:]:
                Physical_Science.write(item)
                if 'ANSWER:' in item:
                    Physical_Science.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
        if ('General Science' in item) or ('GENERAL SCIENCE' in item):
            for item in input_list[ran-1:]:
                General_Science.write(item)
                if 'ANSWER:' in item:
                    General_Science.write('\n'+'------------------------------------------------------------------------------------------'+'\n')
                    break
            
        ran += 1
    print('Program ran successfully :)')

    
    input_file.close()
    Physical_Science.close()
    Life_Science.close()
    Math.close()
    Energy.close()
    Earth_Space.close()
    General_Science.close()

