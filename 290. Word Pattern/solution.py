class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        listS = s.split()
        mapPS = {}
        mapSP = {}
        if len(pattern) != len(listS):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapPS and listS[i] in mapSP:
                if mapPS[pattern[i]] != listS[i] or mapSP[listS[i]] != pattern[i]:
                    return False
            elif pattern[i] in mapPS and listS[i] not in mapSP:
                return False
            elif pattern[i] not in mapPS and listS[i] in mapSP:
                return False
            else: 
                mapPS[pattern[i]] = listS[i]
                mapSP[listS[i]] = pattern[i]

        return True
