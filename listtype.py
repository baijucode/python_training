# types of list
# append:adds one datainsert:
# data=[1,2,3,4,5,6,7]
# data.append(2)
# a=[1,2,3,4,5,6,7]
# b=[1,2,3,4,5,6,7]
# a.extends(b)
# data.inset(12456,"hello")
# print(data)
# print(b)

# concat
# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c)
# a=[1,2,3,4,5,6,7]
# b=[1,2,3,4,5,6,7]
# a.extends(b)


# remove

# del:can remove entire data
# remove :one at a time
# pop:last data
# clear:empty 

#removes certain data at a time
# data=["kathmandu","bhaktapur","Iran","nepal"]
# data.remove("nepal")
# print(data)


#del all or specific data del.data(0)
# data = ["kathmandu", "bhaktapur", "Iran"]
# del data
# print(data)


#pop removes last data also shows which data is removed(cant remove the whole data)
# data = ["kathmandu", "bhaktapur", "Iran"]
# remove_data=data.pop()
# print(data)
# print(remove_data)

# clear removes all data (becomes empty)
# data.clear()
# print(data)

#count() counts the repetation of the value
# data = ["kathmandu", "bhaktapur", "Iran"]
# c=data.count("Iran")
# print(c)


#index shows the index of the value
# data = ["kathmandu", "bhaktapur", "Iran"]
# i=data.index("kathmandu")
# print(i)

#reverse 
# data = ["kathmandu", "bhaktapur", "Iran"]
# r=data.reverse()
# print(data)

# data.sort

# a=[1,2,3,["hello",'hi'],19]
# b=a[3]
# print(b[1])


#dictionary
a={
    "name":"hari",
    "address":"kathmandu",
    "age":1,
    "age":12,
    "height":5,
    "weight":54,
    "religion":"Hindu"
}
# print(type(a))
# print(len(a))
# print(a['name'])
# print(a.keys())
# print(a.values())

# a['address']='Kathmandu'
# a['age']=14
# a['phone']=986
# print(a)

# #update
# a.update({'name':"Ashmita","address":"Bhaktapur","age":23,"phone":98615})
# print(a)

# del a['name']
# print(a)

# data=a.popitem()
# print(data)
# print(a)

# a.clear()
# print(a)

# print(a.keys())
# print(a)

#give default value or sends none if the value is not available
# print(a.get("Name","not found"))

# print(a["name"])

# user_info={
#     "name":"Ashmita",
#     "address":{
#         "temp":"Kathmandu",
#         "per":"Bhaktapur"
#     }
# }

# print(user_info.values())
# print(user_info["address"]["per"])

user_info={
    "name":"Ashmita",
    "phone":[
        {
            "type":"ntc",
            "number":988888
        },
        {
            "type":"smart",
            "number":950

        }
       
    ]
}


print("my name is",user_info["name"],"my" ,user_info["phone"][0]["type"]," number is" ,user_info["phone"][0]["number"] , "and " ,"my" ,user_info["phone"][1]["type"]," number is" ,user_info["phone"][1]["number"])