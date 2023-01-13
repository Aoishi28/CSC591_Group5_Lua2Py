class Eg:
    """
    Test class for the
    """

    def egs(self, key,str,fun):
        """
        Test format for different example scenarios
        """
        eg = {}
        eg[key] = fun
        help = help.format("-g  %s\t%s\n",key,str)
        return help