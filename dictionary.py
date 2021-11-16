#list -> collection of elements ordered ele in seq
#set -> doesnt maintain seq (unique elements)
#sometimes we need key for evry value
#DICTIONARY -> PYTHON

#key shud be immutable and unique
data = {1:'Swetha',2:'Poojitha',3:'Abhishek',4:'Oswin',5:'Wally',6:'Pranee',7:'Asee',8:'Devi'}
print(data)
print(data[5])
# data.get -> to fetch values
# print(data.get(1)) -> starts with 1
print(data.get(0,'Not Found'))
print(data.get(9,'Index Out of Bound'))
#Merge into dictionary
keys = ['Abhi','Swetha']
values = ['Amazon','Pelatro']
dic = dict(zip(keys,values))
print(dic)

dic['Avinash'] = 'Accenture'
dic['Shivi'] = 'Factset'
print(dic['Shivi'])

prog = {'JS':'Atom','CPP':'VS','Python':['Pycharm','Sublime'],'Java':['JSE','Netbeans'],'J2EE':'Eclipse'}
print(prog['Java'])



