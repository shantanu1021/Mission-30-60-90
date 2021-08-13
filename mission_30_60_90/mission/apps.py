from django.apps import AppConfig


class MissionConfig(AppConfig):
    name = 'mission'

    def ready(self):
        import mission.signals