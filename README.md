#S b e r _ t a s k#  
 
Напишите программу для симуляции торговли на финансовых рынках, включая методы для выполнения транзакций покупки и продажи активов и получения текущей стоимости портфеля.  

```
from decimal import Decimal
from enum import Enum

class AssetPrice(Enum):
    # Котировальный список активов.
    LKOH = Decimal(5896)
    SBER = Decimal(250)
    ```
