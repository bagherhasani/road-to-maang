


class Solution(object):
    
    def romanToInt(self, s):
        seen={}
        result=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="I":
                if "V" in seen or "X" in seen:
                    result-=1
                else:
                    result+=1

                seen[s[i]]="1"

            elif s[i]=="V":
                result+=5
                seen[s[i]]="1"

            elif s[i]=="X":
                if "C" in seen or "L" in seen:
                    result-=10
                else:
                    result+=10

                seen[s[i]]="X"

            elif s[i]=="L":
                result+=50
                seen[s[i]]="L"

            elif s[i]=="C":
                if "M" in seen or "D" in seen:
                    result-=100
                else:
                    result+=100

                seen[s[i]]="1"
                
            elif s[i]=="D":
                result+=500
                seen[s[i]]="1"

            elif s[i]=="M":
                result+=1000
                seen[s[i]]="1"

            
            

    
        return result
   
        

    
    

if __name__=="__main__":
    s = "MCMXCIV"
    sol=Solution()
    print(sol.romanToInt(s))
    print("--------------")


    seen={}
    result=0
    for i in range(len(s)-1,-1,-1):
        if s[i]=="I":
            

            if "V" in seen:
                result-=1
            else:
                result+=1

            seen[s[i]]="1"

        elif s[i]=="V":
            result+=5
            seen[s[i]]="1"

        elif s[i]=="X":
            if "C" in seen:
                result-=10
            else:
                result+=10

            seen[s[i]]="X"

        elif s[i]=="L":
            result+=50
            seen[s[i]]="L"

        elif s[i]=="C":
            if "M" in seen:
                result-=100
            else:
                result+=100

            seen[s[i]]="1"
            
        elif s[i]=="D":
            result+=500
            seen[s[i]]="1"

        elif s[i]=="M":
            result+=1000
            seen[s[i]]="1"

        
        

    print(result)
    