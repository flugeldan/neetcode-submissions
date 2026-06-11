class Solution:

    def encode(self, strs: List[str]) -> str:
        code=[]
        for element in strs:
            element=str(len(element))+'#'+element
            code.append(element)
        self.code=''.join(code)
        return self.code
    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1

            length=int(s[i:j])
            word = s[j+1 : j+1+length] 
            result.append(word)
            i=j+1+length
        return result



                



