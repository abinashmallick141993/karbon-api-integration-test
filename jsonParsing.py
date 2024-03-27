import json
import requests

#with open('C:\\Users\\AbinashMallick\\PycharmProjects\\JsonFiles\\Sample01.json') as f:
    #data = json.load(f)
    #print(data)
    #print(type(data))
    #print(data['links']['next'])
    #print(type(data['links']))
    #print("#############")
    #print(data['data'])
    #print("#############")
    #print(data['included'])
    #print("#############")

with open('C:\\Users\\AbinashMallick\\PycharmProjects\\JsonFiles\\POST01.json') as f:
    data = json.load(f)
    print(data)
    #print(type(data))
    for item in data:
        print(item['id'])
        print(item['caseType'])
        products = item['products']
        for prod in products:
            print("Values available in product:"+prod)
            print(type[prod])
            print(item['jurisdiction'])
            if (item['jurisdiction'])== 'US':
                assert (item['jurisdiction']) == 'US'
                print("Correct jurisdiction")
            if(item['legalEntityName'])== 'ABC Corporation':
                assert (item['legalEntityName']) == 'ABC Corporation'
                print("Correct legalEntityName")
with open('C:\\Users\\AbinashMallick\\PycharmProjects\\JsonFiles\\Sample01.json') as f1:
    data2 = json.load(f1)
    assert data2 != data

with open('C:\\Users\\AbinashMallick\\PycharmProjects\\JsonFiles\\Post02.json') as f2:
    data3 = json.load(f2)
    assert data3 == data













