list = []

try:
    while True:
        print('Item amount : ', len(list))
        print('Inventory : ', list)

        if len(list) >= 4:
            raise Exception('Inventory Lack')
        item = 'item' + str(len(list))
        list.append(item)
except Exception as e:
    print('Inventory Full')
    print(e)