class Teacher(object):
    def __init__(self, name, password):
        import tools
        self.name = name
        self.password = tools.encrypt_password(password)
