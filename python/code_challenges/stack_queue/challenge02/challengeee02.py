# Write here the code challenge solution
 
def Valid_Parentheses(sequence):
       '''
       function that get a string as parmiter and check it  when an open parentheses is in openinig_list push it in the stack, and when closed parenthesis is encountered,
        match it with the top of stack and pop it.
        If stack is empty at the end, return True otherwise, False.
       '''
      
       stack = []
       open_list = ['(','{','[']
       close_list = [')','}',']']
       
       for i in sequence :
           if i in open_list :
               stack.append(i)
           if i in close_list :
               if not stack :# check if the stack is empty
                   return False
           
               curr_char = stack.pop()  
               if curr_char == '(':  
                   if i != ")":  
                    return False  
               if curr_char == '{':  
                   if i != "}":  
                      return False  
               if curr_char == '[':  
                 if i != "]":  
                    return False 
               else :
                   continue
       if not stack :
           return True
       else :
           return False

print(Valid_Parentheses("[(hello))]"))
print(Valid_Parentheses("[{(())}]"))
print(Valid_Parentheses("[{((JKJO}]"))

# print(checkBalance("[(hello)()]"))