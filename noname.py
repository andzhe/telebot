def usr_result(file_log):
    n = ''
    y = ''
    f_u = open(file_log)
    f_l = f_u.read()
    a = f_l.index('Ненайденые')
    y = f_l[:a-1]
    n = f_l[a:]
    return y
    
print(usr_result())
    
    

