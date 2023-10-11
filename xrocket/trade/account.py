class Account:

    """ Account methods wrapper.

    Available methods:

    * balance()
    * balance_coin()

    """

    async def balance(self):
        """ Get all balances"""
        return await self.request(method = 'account/balance',
                                  request_method = 'GET')

    async def balance_coin(self, coin: str):
        """ Get balance of coin

        :param `coin` [str]: Coin of balance

        """

        return await self.request(method = f'account/balance/{coin}',
                                  request_method = 'GET')
