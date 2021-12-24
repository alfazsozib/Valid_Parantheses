class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        look_dic = {")":"(","}":"{","]":"["}
        
        
        for i in s:
            if i in look_dic.values():
                stack.append(i)
            elif stack and look_dic[i] == stack[-1]:
                stack.pop()
                
            else:
                return False
            
        return stack == []