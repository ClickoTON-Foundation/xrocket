class OrderBook:

    """ OrderBook methods wrapper.

    Available methods:

    * order_book_pair()

    """

    async def order_book_pair(self, pair: str):
        """ Get full order book for pair
        
        :param `pair` [str]: Pair name of rates

        """

        return await self.request(method = f'order-book/full/{pair}',
                                  request_method = 'GET')

