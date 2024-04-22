"""
    dictionaries are used to collect jordered or data of different data types
    to declare a dictionary use the {} curly braces
    also it consist of a value and a key that points to its data

    example:
            OperatingSystem = {"name": "kali", "evention":1978, "version":"Kali Rolling" }
    example2:
            another way to create a dictionary is to use 
            application = dict(recon="nmap", option="--scritp", version="3.13")
            application2 = dict("vulnerability="msfconsole", option="use", version="12.1")

    one can also access the keyvalues and their data by using
    person['name']

    or use get() method if key is not know
    dictionaryName.get("key")
    dictionaryName.get("key","unknown")

    you could also use in to check if key value exits in a dictionary
    example:
            "address "in person return false
    also assigning new-key values

"""
print("\t\t DICTIONARY AND DICTIONARY METHODS")
person = {"name":"Richard", "age": 53, "gender":"Male", "maritalStatus":"married"}
print("the type of our data is {}".format(type(person)))
print("our dictionary is {}".format(person))
person2 = dict(name="kelly", age=23, gender="female", maritalStatus="single")
print(person2)
print(person2['name'])
print(person2.get('age'))#no error if no key is found

result = "address" in person2
print(result)  
print("\n\n")
operatingSystem = dict(name = "kali", purpose = "pentesting & programming", version=11.3, manufacturer="linus Tovalds")
print(operatingSystem)
print(operatingSystem.get("name"))
##modifying values
operatingSystem['name'] = "Windows"
print(operatingSystem.get("name"))
operatingSystem['name'] = "kali linux"
operatingSystem['bestTool'] = "netcat"
print(operatingSystem)