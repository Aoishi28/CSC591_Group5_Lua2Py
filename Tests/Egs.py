class Egs:
    def __init__(self, help_input) -> None:
        self.help = help_input
        self.egs = dict()

    def eg(self,key,str,fun):
        """
        Test format for different example scenarios
        """
        self.egs[key] = fun
        self.help += "  -g  {0}\t{1}\n".format(key,str)