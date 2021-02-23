"""
create class to demonstrate "pytest"

Test is excuteed by testcodes
"""
class TargetClass():
    """
    TargetClass to demonstrate test codes
    """
    def add_num_and_double(self,x,y):
        """cal (x+y)*2

        Parameters
        ----------
        x : int
            input val
        y : int
            input val

        Returns
        -------
        int
            result of calcuration

        doctest
        -------
        >>> c = TargetClass()
        >>> c.add_num_and_double(1,2)
        6 #write here assumed return
        """        
        
        if type(x) is not int or type(y) is not int:
            raise ValueError
        
        result = x + y
        result *= 2
        return result

    def even_or_odd(self,v):
        if type(v) is not int:
            raise ValueError

        if v<0:
            return None

        if v%2==0:
            return 0
        else:
            return 1


if __name__=="__main__":
    
    # tar=TargetClass()
    # print(tar.even_or_odd(-3))
    pass