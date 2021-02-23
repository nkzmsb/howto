"""
create class to demonstrate "docktest"

It is possible to demonstrate "docktest" with this file alone.
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
        result = x + y
        result *= 2
        return result


if __name__=="__main__":
    
    import doctest

    doctest.testmod()