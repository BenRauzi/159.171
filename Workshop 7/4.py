def incrementValues(matrix): #shouldn't this be called something else?
   
   return [[int(x/2) if x % 2== 0 else x for x in i] 
                for i in matrix]