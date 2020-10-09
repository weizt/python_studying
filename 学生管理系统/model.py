class Teacher(object):
    def __init__(self, name, password):
        import tools
        self.name = name
        self.password = tools.encrypt_password(password)


class Student(object):
    def __init__(self, s_id, name, age, sex, tel):
        self.s_id = s_id
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
