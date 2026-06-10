class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        


if __name__=="__main__":
    strs = ["flower","flow","flight"]
    prefix=""
    for i in range(1,len(strs)):
        for j in range(len(strs[i])):
            if strs[0][0]!=strs[1][0]:
                print("no common prefix")
                
            elif strs[i][j]==strs[i+1][j]:
                print("Equal: "+strs[i][j])
            