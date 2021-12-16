def one():
    f = "EE00D40C823060"
    k = ""
    for i in list(f):
        
        t = int(i,16)
        k += ""+ "{0:04b}".format(t)
    
    packet_version = int(k[:3],2)
    type_id = int(k[3:6],2)
    
    

    #literal Value
    if type_id == 4:
        A = k[7:11]
        B = k[12:16]
        C = k[17:21]
        literal_value = int(A+B+C,2)
    
    #Operator
    else:
        length_id = int(k[6])
        bits = []

        #15 bits
        if length_id == 0:
            L = int(k[8:22],2)

        #11 bits
        else:
            L = int(k[8:18],2)
           
        print(L)

one()