from django.apps import AppConfig


class DesignConfig(AppConfig):
    name = 'design'

    def ready(self):
        from actstream import registry
        registry.register(self.get_model('Design'))
        registry.register(self.get_model('DesignComment'))
        registry.register(self.get_model('Status'))
        registry.register(self.get_model('StatusComment'))