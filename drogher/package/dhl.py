from .base import Package

class DHL(Package):
    shipper = 'DHL'

class DHLAWB(DHL):
    barcode_pattern = r'^\d{10}$'
    @property
    def valid_checksum(self):
        chars, check_digit = self.tracking_number[:-1], self.tracking_number[-1]
        return int(chars) % 7 == int(check_digit)

class DHLEXPRESSBOXNUM(DHL):
    barcode_pattern = r'([J-Jj-j]{2}[D]{1}[0-9]{18})'

    @property
    def valid_checksum(self):
        return True