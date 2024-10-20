
# class int_reverse:

#     def reverse_int(self,num):

#         s = str(num)
#         i = s[::-1]

#         i = int(i)

#         return i
    

# o1= int_reverse()
# print(o1.reverse_int(1234567890))

class Num:

    def __init__(self,my_int):
        self.input_int = my_int

    def reverse(self):
        inp_to_str = str(self.input_int)
        reverse_int =int(inp_to_str[::-1])
        return reverse_int
    
# n1 = Num(34567809)
# print(n1.reverse())