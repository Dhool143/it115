#

import json

#
data1 = {
    
    'name': 'Fathiya Yoosef',
    'age': 40,
    'city': 'Washigton, Seattle',
    'interests':['Traveling', 'Shopping', 'Eating new Food', 'Watch Movies'],
    'is_student': False, 

 
}
#
with open('data1.json', 'w') as json_file:
    
    #Dump the Date Dictionary into the json file.
    json.dump(data1,json_file,indent=4)
    
print("You have successfully written to datal.json")
    
