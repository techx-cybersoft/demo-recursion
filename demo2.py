lstDemo = [
    {
        "id": 1, 
        "value": [
            {
                "id": 2,
                "value": [
                    {
                        "id": 3,
                        "value": [
                            {
                                "id": 4,
                                "value": []
                            }
                        ]
                    }
                ]
            },
            {
                "id": 6,
                "value": []
            }
        ]
    },
    {
        "id": 5, 
        "value": []
    }
]

# dictResult:object = []

def getList(lstData):
    result = []
    for item in lstData:
        print(item) # check to make sure that the recursion function is working
        data = {
            "id": item["id"]
        }
        result.append(data)

        if item["value"] != 0:
            result.extend(getList(item["value"]))
        
    return result

print(getList(lstDemo))