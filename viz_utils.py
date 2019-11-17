def vis_2darray(array):
    # Assuming a 2d array is passed.
    for row in array:
        for val in row:
            str_val = str(val)
            padd = 4 - len(str_val)
            
            padd_str = " "*padd
            print(padd_str+str_val, end="")
            
        print("\n")