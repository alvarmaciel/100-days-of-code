from app_example_1.module_1.submodule_1_1.submodule_1_1_1.print_messages import PrintMessage

class UsePrintMessage:
        
    def print_message_uppercase(self, PrintMessage_method_call: PrintMessage, message) -> str:
        if isinstance(PrintMessage_method_call, PrintMessage) == True:
                return PrintMessage_method_call.print_message(message).upper()
        else:
            raise AttributeError("error, argument is not an implementation of print_message method")