class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __hash__(self):
        return hash(self.password)
    def __str__(self):
        return f'{self.nickname}'
    def __int__(self):
        return self.age


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
