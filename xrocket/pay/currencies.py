class Currencies:

    """ Currencies methods wrapper.
    
    Available methods:

    * currencies_available()

    """

    async def currencies_available(self):
        """ Get available currencies"""

        return await self.request(method = 'currencies/available',
                                  request_method = 'GET')
