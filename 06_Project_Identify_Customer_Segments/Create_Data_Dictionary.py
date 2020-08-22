#!/usr/bin/env python
# coding: utf-8

def create_data_dictionary():
    # Read File
    file_obj = open('Data_Dictionary.md', 'r')
    buf      = file_obj.read()
    file_obj.close()

    # String -> List
    text_data = buf.split('\n')

    # Get Name & Explanation
    flag_find_key    = 0
    tmp_name_list    = []
    name_list        = []
    explanation_list = []
    id_1_list        = []
    id_2_list        = []
    id_3_list        = []
    #-----------------------------------------------
    for line in text_data:
        # Ignore "Table of Contents"
        if line.find("Table of Contents") > -1:
            continue
        
        # Find Key Word
        pos_find = line.find("###")
        
        #------------------------------------------
        # get name of columns
        if pos_find >= 0:
            # remove ","
            line = line.replace("," , "")
            
            # translate multi-space to single-space
            for i in range(5):
                line = line.replace("  ", " ")
            
            # split line by space       
            flag_find_key += 1
            line_split     = line.split(" ")
            
            # save names as list
            if flag_find_key == 1:
                tmp_id_1  = line_split[1][0:-1]
                tmp_id_2  = tmp_id_1.split(".")
                data_id_1 = tmp_id_2[0]
                #
                if len(tmp_id_2) == 1:
                    data_id_2 = "0"
                else:
                    data_id_2 = tmp_id_2[1]
                #
                tmp_name_list.extend(line_split[2:])
            else:
                tmp_name_list.extend(line_split[1:])
                
        #------------------------------------------
        # get explanations of columns
        if (pos_find == -1) and (flag_find_key > 0):
            # save data as list 
            for name in tmp_name_list:
                name_list.append(name)
                explanation_list.append(line)
                id_1_list.append(data_id_1)
                id_2_list.append(data_id_2)
                #
                data_id_3 = str( int(data_id_1)*100 + int(data_id_2) )
                id_3_list.append(data_id_3)
                
            # initilize
            flag_find_key = 0
            tmp_name_list      = []
            
    # Write to Text File
    with open('Data_Dictionary.csv', 'w') as file_obj:
        cnt = 0
        # write header
        file_obj.write("id_1" + "\t" + "id_2" + "\t" + "id_3" + "\t" + "name" + "\t" + "explanation" + "\n")
        #
        for name, explanation, id_1, id_2, id_3 in zip(name_list, explanation_list, id_1_list, id_2_list, id_3_list):
            cnt +=1
            if cnt < len(name_list):
                file_obj.write(id_1 + "\t" + id_2 + "\t" + id_3 + "\t" + name + "\t" + explanation + "\n")
            else:
                file_obj.write(id_1 + "\t" + id_2 + "\t" + id_3 + "\t" + name + "\t" + explanation)        