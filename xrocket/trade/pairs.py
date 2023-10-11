class Pairs:

    """ Pairs methods wrapper.

    Available methods:

    * pairs()
    * pair_by_name()

    """

    async def pairs(self):
        """ Get all pairs"""
        return await self.request(method = 'pairs',
                                  request_method = 'GET')

    async def pair_by_name(self, name: str):
        """ Get pair by name

        :param `name` [str]: Name of pair

        """

        return await self.request(method = f'pairs/{name}',
                                  request_method = 'GET')
