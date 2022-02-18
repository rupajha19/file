file_data=open("people1-exercise.txt","r")
count=0
for i in file_data:
    count=count+1
print(count)
file_data.close()
