
#always ask for more information
#don't take it for granted
def run():
    my_list = [10, 15, 3, 7]
    temp_list = []
    value_provide = 17
    value_a = 0
    value_b = 0
    
    for element in my_list:
        temp_list.append(element)
        if len(temp_list) > 1:
            for elemento_t in temp_list:
                if element + elemento_t == value_provide:
                    value_a = elemento_t 
                    value_b = element
                    ##print('number found: element b:'+str(value_b)+'element e:'+str(value_a))
                    break
        
        if value_a + value_b == value_provide: 
            break

    print('Value of a: '+str(value_a))
    print('Value of b: '+str(value_b))

if __name__ == '__main__':
    run()