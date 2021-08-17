import matplotlib.pyplot as plt
import pandas

''' This program gives the heat maps of 1) Theft Crime, 
                                        2) Homicide Crime (extra heat map to help in predictive policing),
                                        3) Vacant Buildings.
                                        4) Predictive Policing; All by Wards. '''

                           
def ward_count(df, col, value, unique_id, ward_num):
    ''' Returns count of unique_id in df ward_num rows w/entry value in column col. '''
    rows = df[ df[col] == value] # boolean slice of rows we want
    if ward_num not in rows['Ward'].values:
        return 0
    grouped = rows.groupby('Ward')
    return grouped[unique_id].count()[ward_num]




def make_ward_dictionary(df, col, value, unique_id):
    ''' Returns a dictionary that has keys as ward numbers, 
        and the values as the number of times 'value' is present in 'col'. '''
        
    my_dict = {}
    
    for i in range(1,51):
        my_dict.update({i: ward_count(df, col, value, unique_id, i)})
        
    return my_dict


fileref = open('Crimes_-_2010_to_present.csv', 'r')
crime_df = pandas.read_csv(fileref, low_memory = False)


'''Plot 1: Theft Crimes'''
my_list = []
crime_dict = make_ward_dictionary(crime_df, 'Primary Type', 'THEFT', 'Case Number')

for i in crime_dict.values():
    my_list.append(i)

mega_list = []
y = 5
i = 0
while i < 47:
    mega_list.append(my_list[i:y])
    i += 5
    y += 5


plt.figure(1)    
plt.pcolor(mega_list)
plt.summer()
plt.colorbar()
plt.title('Theft Crime in Chicago By Wards')
    


'''Plot 2: Homicide Crimes'''
my_listz = []
crime_dictz = make_ward_dictionary(crime_df, 'Primary Type', 'HOMICIDE', 'Case Number')

for i in crime_dictz.values():
    my_listz.append(i)

mega_listz = []
y = 5
i = 0
while i < 47:
    mega_listz.append(my_listz[i:y])
    i += 5
    y += 5


plt.figure(2)    
plt.pcolor(mega_listz)
plt.summer()
plt.colorbar()
plt.title('Homicide Crime in Chicago By Wards')
            

    

'''Plot 3: Abandoned Buildings'''
fileref2 = open('311_Service_Requests_-_Vacant_and_Abandoned_Buildings_Reported.csv', 'r')
crime_df2 = pandas.read_csv(fileref2, low_memory = False)


my_list2 = []
crime_dict2 = make_ward_dictionary(crime_df2, 'SERVICE REQUEST TYPE', 'Vacant/Abandoned Building', 'SERVICE REQUEST NUMBER')

for i in crime_dict2.values():
    my_list2.append(i)

mega_list2 = []

y = 5
i = 0
while i < 47:
    mega_list2.append(my_list2[i:y])
    i += 5
    y += 5


plt.figure(3)
plt.pcolor(mega_list2)
plt.summer()
plt.colorbar()
plt.title('Vacant Buildings Reported by Wards')





'''Mapping the city according to the scaled crimes'''

list_theft_scaled = []
list_of_theft = list(crime_dict.values())
for i in list_of_theft:
    list_theft_scaled.append(i / max(list_of_theft))
    
    
    
list_vacant_scaled = []
list_of_vacant = list(crime_dict2.values())
for i in list_of_vacant:
    list_vacant_scaled.append(i / max(list_of_vacant))



list_homicide_scaled = []
list_of_homicide = list(crime_dictz.values())
for i in list_of_homicide:
    list_homicide_scaled.append(i / max(list_of_homicide))
    
    


'''Theft is twice as intense as vacant buildings; Homicide is twice as intense as theft'''
list_final_scaled = []
for i in range(50):
    list_final_scaled.append((2 * list_theft_scaled[i]) + (1 * list_vacant_scaled[i]) + (4 * list_homicide_scaled[i]))

mega_list_final = []
y = 5
i = 0
while i < 47:
    mega_list_final.append(list_final_scaled[i:y])
    i += 5
    y += 5
    
''' Crime Heat Map by wards'''    
plt.figure(4)    
plt.pcolor(mega_list_final)
plt.plasma()
plt.colorbar()
plt.title('Predictive Policing Based On Homicides, Theft and Vacant Buildings')

final_dict = {}
for i in range(50):
    final_dict.update({i + 1:list_final_scaled[i]})
    


