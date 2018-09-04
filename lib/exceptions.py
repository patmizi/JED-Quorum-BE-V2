class ArgumentNullException(RuntimeError):
    def __init__(self, param_name):
        super().__init__("Parameter cannot be null or empty: `%s`" % param_name)
