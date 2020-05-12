from .base import Unknown
from .dhl import DHLAWB
from .dhl import DHLEXPRESSBOXNUM
from .fedex import FedExExpress
from .fedex import FedExGround96
from .ontrac import OnTrac
from .ups import UPS
from .usps import USPSIMpb
from .usps import USPSS10
from .usps import USPS20


barcode_classes = ['DHLAWB', 'DHLEXPRESSBOXNUM', 'FedExExpress', 'FedExGround96', 'OnTrac', 'UPS', 'USPSIMpb', 'USPSS10', 'USPS20']
