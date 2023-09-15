from decimal import Decimal
from enum import Enum


class AssetPrice(Enum):
    """
    This class contains information about
    the shares available for purchase and their value.
    """
    LKOH = Decimal(5896)
    SBER = Decimal(250)
