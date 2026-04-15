class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #res = ""
        if len(s) <= 2 or numRows == 1 or numRows >= len(s) :
            return s
        #for row in range(1,numRows+1) :
         #   i = row-1
          #  res += s[i]
           # if row == numRows :
            #    Up = 1
            #else :
             #   Up = 0
            #while i < len(s) :
             #   if Up == 0 :
              #      i += 2*(numRows-row)
               #     if row != 1 :
                #        Up = 1
                #else :
                 #   i += 2*row-2
                  #  if row != numRows :
                   #     Up = 0
                #if i < len(s) :
                 #   res += s[i]
            #if row == numRows :
             #   Up = 1
            #else :
             #   Up = 0
        #return res

        id = 0
        UpOrDown = 1
        res = ['']*numRows
        for char in s :
            res[id] += char
            if id == numRows-1 :
                UpOrDown = -1
            if id == 0 :
                UpOrDown = 1
            id += UpOrDown
        return ''.join(res)
