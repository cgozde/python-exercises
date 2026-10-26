class Solution(object):
    def romanToInt(self, s):
        tplm = 0
        symbol = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        length = len(s)
        for i in range(length):
            deger = symbol[s[i]]

            if i + 1 < length and deger < symbol[s[i+1]]:
                tplm -= deger
            else:
                tplm += deger
        return(tplm)
        