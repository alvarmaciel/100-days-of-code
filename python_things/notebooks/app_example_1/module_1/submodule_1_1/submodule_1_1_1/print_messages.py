class PrintMessage:
    
    def print_message(self, arg: str) -> str:
        if isinstance(arg, str) == True:
                return arg
        else:
            raise TypeError("error, argument is not a string type")