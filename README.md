# xRocket 

xRocket Python SDK.

## Description

Pay and Trading xRocket API.

## Getting Started

### Dependencies

* httpx

### Installing

```
pip install xrocket
```

### Using PayAPI

```py
import asyncio
from xrocket import PayAPI

async def main():
    api = PayAPI(api_key='your api key here')

    cheque = await api.cheque_create(currency='BOLT', amount=1, enable_captcha=False)
    await api.cheque_delete(cheque['data']['id'])

    invoice = await api.invoice_create(currency='BOLT', amount=1)
    await api.invoice_delete(invoice_id=invoice['data']['id'])

    await api.transfer(user_id=6037851294, currency='TONCOIN', amount=0.1)

    await api.withdrawal(network='TON', currency='TONCOIN', amount=0.1,
                         address='EQAsl59qOy9C2XL5452lGbHU9bI3l4lhRaopeNZ82NRK8nlA')

asyncio.run(main())
```

### Using TradeAPI
```py
import asyncio
from xrocket import TradeAPI

async def main():
    api = TradeAPI(api_key='your api key here')

    balance = await api.balance()
    print(balance)

    await api.order_execute(pair='BOLT-TONCOIN', order_type='BUY', execute_type='LIMIT',
                            rate=0.02, amount=5, currency='BOLT')

    price = await api.rates_crypto_in_fiat(crypto='BOLT', fiat='USD')
    print(f"1 BOLT = {price['data']['rate']} USD")

asyncio.run(main())
```

## Authors

[@shibdev](https://t.me/dogpy)
[@VladPavly](https://t.me/dalvpv)

## Version History

* 0.1.0
    * Initial version

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Donate

If you like the library, I will be glad to accept donations.

* TON: EQCgphx8rTI0PukwmgpVqiPgqguTujhQscg2h7jgc4U0t347

## Acknowledgments

* [xrocket-pay-docs](https://pay.ton-rocket.com/api)
* [xrocket-trade-docs](https://trade.ton-rocket.com/api)

