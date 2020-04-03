class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        Reverse an interger i.e. 321 -> 123
        """

        #keep track of negative number
        if(x < 0):
            x = str(x)
            x = "-" + x[::-1]
            x = x[:len(x)-1]
        else:
            x = str(x)[::-1]

        #return an integer
        x = int(x)
        if((x > 2147483647) or (x < -2147483648)):
            return 0
        else:
            return(int(x))
