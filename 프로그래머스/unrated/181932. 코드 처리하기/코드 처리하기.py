def solution(code):
    mode = 0  # Initial mode is 0
    ret = ""  # Initialize the result string

   
    for idx in range(len(code)):
        
        if mode == 0:
           
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            
            elif code[idx] == "1":
                mode = 1
        
        else:
            
            if code[idx] != "1" and idx % 2 != 0:
                ret += code[idx]
            
            elif code[idx] == "1":
                mode = 0

    
    if ret == "":
        return "EMPTY"
    else:
        return ret


