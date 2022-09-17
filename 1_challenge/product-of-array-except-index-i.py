def recursiveOperation(my_list):
    #print(my_list)
    if len(my_list) == 1:
        return my_list[0]
    product = my_list[len(my_list) -1]
    my_list.pop()
    
    return  product * recursiveOperation(my_list)


def run():
    #my_list = [1, 2, 3, 4, 5]
    my_list = [3, 2, 1]
    product_list = []

    for index, value in enumerate(my_list):
        temp_list = my_list[:]
        temp_list.pop(index)
        product_list.append(recursiveOperation(temp_list))

    print(product_list)

if __name__ == '__main__':
    run()