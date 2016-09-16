print("Добро пожаловать в мою программу!")
print()

ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
print(ivan)
print(darja)
emps = [ivan, darja]

for i in emps:
    for j in i['children']:
        if j['age']>18:
            print (i['name'])
            break