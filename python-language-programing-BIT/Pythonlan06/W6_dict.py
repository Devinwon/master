dict={'name':'abc','pwd':'123'}             #define dict
print('print the dict:',dict,sep='')
print('search the name key:'+dict['name']) #visit key-'name'
print('Now append status-off to dict')
dict['status']='off'                        #append key-value
print('Newer dict:',end='')
print(dict)
#list operation in dict
print('\n-----------------')
for key in dict:
    print(key+':'+str(dict[key]))
    
print('-----------------')  
print('print all keys')
for key in dict.keys():
    print(key)
    
print('-----------------')  
print('print all values')
for value in dict.values():
    print(value)

print('-----------------')  
print('print all items')
for item in dict.items():
    print(item)

print('-----------------')  
print('print keys values')
for key,value in dict.items():
    print(key,value)
         
print('-----------------') 
print('Delete the name key in dict:')
del dict['name']                #delete the key and the value
print(dict)  

for key in dict:
    print(key+':'+str(dict[key]))
    
print('key name exist or not:','name' in dict,sep='')
