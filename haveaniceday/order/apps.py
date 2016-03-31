from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = 'Orders Application'

    def ready(self):
        import order.signals
