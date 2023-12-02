
i = 0
row = 0
r = 0
with open("autors.txt", "r", encoding = "utf-8") as file:
    for line in file:
        row = row+1
        data = line.split(" ")
        data_pupil = [data[0], data[1], int(data[2])]
        i = i+data_pupil[2]      
        if data_pupil[2] == 5:
            r+=1           
                    
print(i/row)
print(r)