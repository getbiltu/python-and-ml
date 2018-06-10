#Flatning Multi DimenSional List
#by Biltu Maji_CSE
multidimensional_list=[[1,22,[86,9]],[4,5,[2,[4,21],315],6],[87,23]]#Given MultiDimensinal List
multidimensional_list_in_string=str(multidimensional_list)#list converted to single list by convertion to String

flatten_list=[]
flatten_list_index=0

for i in range(0,len(multidimensional_list_in_string)):

    if multidimensional_list_in_string[i].isdecimal()==True:#check If the Element is Decimal Or Not
        if multidimensional_list_in_string[i-1].isdecimal()==True:#chek if the Element is single digit or more the one digit if more then one digit then have to marge
            num=(int(flatten_list[flatten_list_index-1])*10)+int(multidimensional_list_in_string[i])#marging digits
            flatten_list.insert(flatten_list_index-1,num)#inserting Meged digit to previous location
            flatten_list.pop(flatten_list_index)#as insertin an element in a location will move foroward the current location but we dont need that element so we deleted that(bil2)
        else:
            flatten_list.append(int(multidimensional_list_in_string[i]))
            flatten_list_index+=1#flating list index counter

print("Multi Dimentional List Is:", multidimensional_list)
print("\nFlaten List Is:", flatten_list, "\nLength Is:", len(flatten_list))