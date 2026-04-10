class Suspect:
    def __init__(self, name, role, alibi):
        self.name = name
        self.role = role
        self.alibi = alibi

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def get_alibi(self):
        return self.alibi

    def __str__(self):
        return f"{self.name} - Role: {self.role}"
