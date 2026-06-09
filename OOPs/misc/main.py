
class InstanceCounter(object):

    # class attribute // access by classname.X
    count = 0

    def __init__(self, val=0):
        self._val = val
        InstanceCounter.count += 1

    @property
    def val(self):
        return self._val 

    @val.setter
    def val(self,value):
        if value<0:
            raise ValueError("value can't be zero")
        self._val=value

    @classmethod
    def get_count(cls):
        print(InstanceCounter.count)


    @staticmethod
    def count_stars()->float:
        """
        staticemethod nothing to do about class, method, simply it's just general method
        To make logically grouped we are using it
        
        :return: Infinite stars on the planet
        :rtype: float
        """
        return float('inf')




if __name__=="__main__":
    i = InstanceCounter()
    i = InstanceCounter()
    print(InstanceCounter.count)
    print(i.val)


    i = InstanceCounter()    
    i.val = -129
    print(i.val)

    # i._val still be accessible

    print(InstanceCounter.count_stars())