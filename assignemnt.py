# assignment 1
#a = "jaranwala"
#b = "faislabad"
#c = "lahore"

#cap1 = a[0].upper() + a[1:]
#cap2 = b[0].upper() + b[1:]
#cap3 = c[0].upper() + c[1:]

#print(cap1, cap2, cap3)

#assignment 2

#a = "Jaranwala Faislabad Lahore"

#formatted = a[0:1].lower() + a[1:9].upper() + " " + a[10:11].lower() + a[11:20].upper() + " " + a[20:21].lower() + a[21:].upper()

#print(formatted)

#assignment 3

#st = "Jaranwala Faislabad Lahore Karachi Multan"
#st = (st.replace("J", "j")
        # .replace("F", "f")
        # .replace("L", "l")
        # .replace("K", "k")
        # .replace("M", "m"))

#print(st)

#assignment 4

#Cities = ["Lahore", "Karachi", "Islamabad", "Faisalabad", "Peshawar", 
  #        "Quetta", "Multan", "Rawalpindi", "Sialkot", "Hyderabad"]

#formatted_cities = [x[0].upper() + x[1:-1].lower() + x[-1].upper() for x in Cities]

#print(formatted_cities)




#assignments 5

#tup = ("faisalabad", "jaranwala", "multan")  

#ls = list(tup)  

#new_ls = [] 

#for x in ls:
  #  new_ls.append(x.capitalize())  

#tup = tuple(new_ls)  
#print(tup)

#asiignemnt 6  method 1

#tup1= ("faisalabad", "jaranwala", "multan")  
#tup2= (1,2,3,4,5,6)
#tup3 = tup2 + tup1  
#tup3 = tup3[6:] + tup3[:6]  
#print(tup3)


#asiignemnt 6  method 2

#tup1= ("faisalabad", "jaranwala", "multan")  
#tup2= (1,2,3,4,5,6)
#tup3 = list(tup2) + list(tup1)  
#tup3 = tup3[6:] + tup3[:6]  
#tup3 = tuple(tup3)
#print(tup3)
  
#asiignemnt 6  method 3  

#tup1= ("faisalabad", "jaranwala", "multan")  
#tup2= (1,2,3,4,5,6)
#tup3 =()

#for x in tup2:
   # tup3+=(x,)
#for x in tup1:
  #  tup3+=(x,)
#tup3 = tup3[6:] + tup3[:6] 

#print(tup3)   

#     #asiignemnt 6  method 4

#tup1= ("faisalabad", "jaranwala", "multan")  
#tup2= (1,2,3,4,5,6)
#tup3 = sum((tup2,tup1),())

#tup3 = tup3[6:] + tup3[:6]

#print(tup3)

#     #asiignemnt 6  method 5

#tup1= ("faisalabad", "jaranwala", "multan")  
#tup2= (1,2,3,4,5,6)
#tup3 = (*tup2,*tup1)

#tup3 = tup3[6:] + tup3[:6]

#print(tup3)

# assignment 7

#st={"item 1","item 2"}
#(st1,st2)=st
#print(st1)

#st1="item 3"
#print(st1)

# st1=list(("item3"))
# print(type(st))

# st=tuple(list(("item3")))
# print(type(st))

# assignment 8

# ls=set((["Lahore","Multan","Kasur"]))
# tup=set(((1,2,3)))
# ls.update(tup)
# print(ls)
# print(tup)

# set1={1, 2, 3, 'Lahore', 'Multan', 'Kasur'}
# set2={1, 2, 3}
# set3=set1.difference(set2)
# print(set3)
# set4=set1.union(set2)
# print(set4)
# set5=set1.intersection(set2)
# print(set5)

# assignment 9

# tup=(1,2,3,4,5,6,7,8,9,10)
# (tup1,tup2,tup3,tup4,tup5,tup6,tup7,tup8,*tup9)=tup
# ls=tup9
# print(ls)
# ls=list(tup9)
# print(type(ls))
# ls.append(11)
# print(ls)
# ls=set(list(tup9))
# print(type(ls))

# assignment 10

# set1={"Lahore","Karachi","Islamabad","California",}
# set2={"New York", "New jersey", "Texas", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",}
# set3={1,2,3,4,5,6,7,8,9,10}
# set4={11,12,13,14,}

# set5=set1.union(set2,set3,set4)
# print(set5)

# set5=list([{'New York', 'Islamabad', 1, 2, 3, 'California', 4, 5, 6, 'Oklahoma', 7, 8, 9, 10, 11, 12, 13, 14, 'Pennsylvania', 'Ohio', 'Lahore', 'Karachi', 'Texas', 'Oregon', 'New jersey'}])
# print(type(set5))

# set6=tuple(list([{'New York', 'Islamabad', 1, 2, 3, 'California', 4, 5, 6, 'Oklahoma', 7, 8, 9, 10, 11, 12, 13, 14, 'Pennsylvania', 'Ohio', 'Lahore', 'Karachi', 'Texas', 'Oregon', 'New jersey'}]))
# print(type(set6))

# assignment 11

# dic= {"person":{"name":"Hafiz","age":"20"}}

# dic["person"].pop("name")
# print(dic)

# dic["person"].update({"height":"5.7"})
# print(dic)

# dic["person"]["name"]="ashraf"
# print(dic)

# assignment 12

# dic={}

# dic.update({"name": "Hafiz", "age" : "20","Gender": "Male",})
# dic.update({"address": "Karachi"})
# print(dic)

# name=input({"Enter name:"})
# age=input({"Enter age:"})
# address=input({"Enter address:"})

# student={"name": name,"address":address,"age": age}

# print(student)
 
# assignment 13

# def func_city(ls):
#     b = input('Enter city name ')
#     for city in ls:
#         if(b==city):
#             print("city is clean")
#             break
#     else:
#      print("city not found") 

# ls=["Faisalabad","Lahore","Jaranwala","Multan","Karachi"]           

# func_city(ls)

# part 2

# def func(c):
#     alp= False
#     ls=["Jaranwala","Lahore","Karachi"]

#     for city in ls:
#         if city==c:
#             alp=True                             # by flag methods
#     if(alp):    
#             print("Your city is clean")
#     else:
#             print("Your city is not clean")

# c= input("Please enter the city")
# func(c)

#Part 3

# def func(c):
#     ls=["Jaranwala","Lahore","Karachi"]

#     if c in ls:
#         print("Your city is clean")
#     else:
#         print("Your city is not clean")

# c= input("Please enter the city: ")
# func(c)       


# def func():
#     alp=False
#     num= 50+70-20*2/5

#     if num== 50-500:
#         alp=True
#         print("Your answer is true")
#     if(alp):    
#         print("Your answer is true")    
#     else:
#         print("Your answer is false")

# func()        

     
    
