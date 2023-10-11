from typing import Union


class Orders:

    """ Orders methods wrapper.

    Available methods:

    * order_list()
    * order_execute()

    """

    async def order_list(self, limit: int = 100, offset: int = 0, only_active: bool = True):
        """ Get list of orders

        :param `limit` [int]: Limit of orders list
        :param `offset` [int]: Offset of orders list
        :param `only_active` [bool]: Show only active orders

        """

        return await self.request(method = 'orders',
                                  request_method = 'GET',
                                  params = {
                                    'limit': limit,
                                    'offset': offset,
                                    'onlyActive': only_active
                                  })

    async def order_list_by_pair(self, pair: str,
                                       limit: int = 100, offset: int = 0, only_active: bool = True):
        """ Get list of orders by pair

        :param `pair` [str]: Pair of order
        :param `limit` [int]: Limit of orders list
        :param `offset` [int]: Offset of orders list
        :param `only_active` [bool]: Show only active orders

        """

        return await self.request(method = f'orders/{pair}',
                                  request_method = 'GET',
                                  params = {
                                    'limit': limit,
                                    'offset': offset,
                                    'onlyActive': only_active
                                  })

    async def order_execute(self, pair: str, order_type: str, execute_type: str,
                                  rate: Union[int, float], amount: Union[int, float],
                                  currency: str):
        """ Execute order

        :param `pair` [str]: Pair of order
        :param `order_type` [str]: Type of order
        :param `execute_type` [str]: Execute type of order 
        :param `rate` Union[int, float]: Rate of order
        :param `amount` Union[int, float]: Amount of order 
        :param `currency` [str]: Currency of order 

        """

        return await self.request(method = 'orders',
                                  request_method = 'POST',
                                  json = {
                                    'pair': pair,
                                    'type': order_type,
                                    'executeType': execute_type,
                                    'rate': rate,
                                    'amount': amount,
                                    'currency': currency
                                  })

    async def order_info(self, order_id: str):
        """ Get order info

        :param `order_id` [str]: Order id of order

        """

        return await self.request(method = f'orders/{order_id}',
								  request_method = 'GET')

    async def order_delete(self, order_id: str):
        """ Delete order

        :param `order_id` [str]: Order id of order

        """

        return await self.request(method = f'orders/{order_id}',
                                  request_method = 'DELETE')
