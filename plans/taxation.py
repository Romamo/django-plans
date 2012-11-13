from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class TaxationPolicy(object):
    """
    Abstract class for defining taxation policies.
    Taxation policy is a way to handle what tax rate should put on the order, this depends
    on user billing data.
    """

    def get_default_tax(self):
        return getattr(settings, 'TAX', None)

    def get_issuer_country_code(self):
        return getattr(settings, 'VAT_COUNTRY', None)

    def get_tax_rate(self, vat_id, country_code):
        raise NotImplementedError('Method get_tax_rate should be implemented.')
