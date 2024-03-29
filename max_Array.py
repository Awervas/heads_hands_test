import random


def array_max(input_array):
    
    if not isinstance(input_array, list):
        return {'code':'is not array'}
    
    elif not input_array:
        return {'code':'empty array'}
  
    
    max_value_index = 0
    for i in range(len(input_array)):
        try:
            if input_array[i] > input_array[max_value_index]:
                max_value_index = i
        except TypeError:
            return {'code':'type error'}
    return {
            'code':'ok',
            'max_index_value':max_value_index,
            'max_array_value':input_array[max_value_index],
            }
   

if __name__ == '__main__':

    size_array = 200
    cur_array = []
    for _ in range(size_array):
        cur_array.append(random.randint(0,10000))
        
    print(cur_array)
    rez = array_max(cur_array)
    if rez['code'] == 'ok':
        
        print('Максимальное значение массива: Индекс элемента {}, значение элемента {}'.format(str(rez['max_index_value']),str(rez['max_array_value'])))
    else:
        print(rez['code'])
        
