class Rates:

    """ Rates methods wrapper.

    Available methods:

    * rates_fiat_available()
    * rates_crypto_in_fiat()
    * rates_crypto_available()
    * rates_crypto_in_crypto()

    """

    async def rates_fiat_available(self):
        """ Get fiat rates"""
        return await self.request(method = 'rates/fiat/available',
                                  request_method = 'GET')

    async def rates_crypto_in_fiat(self, crypto: str, fiat: str):
        """ Get rate crypto in fiat
        
        :param `crypto` [str]: Crypto symbol of rates
        :param `fiat` [str]: Fiat symbol of rates

        """

        return await self.request(method = f'rates/fiat/{crypto}/{fiat}',
                                  request_method = 'GET')

    async def rates_crypto_available(self):
        """ Get crypto rates"""
        return await self.request(method = 'rates/crypto/available',
                                  request_method = 'GET')

    async def rates_crypto_in_crypto(self, base: str, quote: str):
        """ Get rate crypto in fiat
        
        :param `base` [str]: Base symbol of rates
        :param `quote` [str]: Quote symbol of rates

        """

        return await self.request(method = f'rates/crypto/{base}/{quote}',
                                  request_method = 'GET')
