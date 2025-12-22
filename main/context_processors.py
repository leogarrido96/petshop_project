from .models import SiteConfiguration


def site_config(request):
    """
    Disponibiliza as configurações do site em todos os templates.
    """
    config = SiteConfiguration.objects.first()  # Pega o primeiro registro
    return {'site_config': config}
