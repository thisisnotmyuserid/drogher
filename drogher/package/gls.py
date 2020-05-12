from .base import Package


class GLS(Package):
    shipper = 'GLS'
    barcode_pattern = r'\b([0-9]{12,12})\b'

    @property
    def valid_checksum(self):
        return True
