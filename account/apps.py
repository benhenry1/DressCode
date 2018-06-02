from django.apps import AppConfig, apps


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):
        from actstream import registry
        from django.contrib.auth.models import User
        registry.register(User)


