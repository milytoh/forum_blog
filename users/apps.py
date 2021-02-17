from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #adding users frofile signals
    def ready(self):
        import users.signals
