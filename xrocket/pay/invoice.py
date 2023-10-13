from typing import Union


class Invoice:

    """ Invoice methods wrapper. 
    
    Available methods:

    * invoice_create()
    * invoice_list()
    * invoice_info()
    * invoice_delete()

    """

    async def invoice_create(self, amount: Union[int, float], currency: str,
                                   description: str = '', num_payments: int = 1,
                                   hidden_message: str = '', 
                                   comments_enabled: bool = False,
                                   min_payment: Union[int, float, None] = None,
                                   callback_url: str = '', 
                                   payload: str = '', expired_in: int = 0):
        """ Create invoice

        :param `amount` Union[int, float]: Amount of invoice
        :param `min_payment` Union[int, float]: Minimal payment of invoice
        :param `num_payments` [int]: Number payments of invoice
        :param `description` [str]: Description of invoice
        :param `hidden_message` [str]: Hidden message of invoice
        :param `comments_enabled` [bool]: Is comments enabled of invoice
        :param `callback_url` [str]: Callback url of invoice
        :param `payload` [str]: Payload of invoice
        :param `expired_in` [int]: Expired in of invoice

        """
        return await self.request(method = 'tg-invoices',
                                  request_method = 'POST',
                                  json = {
                                    'amount': amount,
                                    'minPayment': min_payment,
                                    'numPayments': num_payments,
                                    'currency': currency,
                                    'description': description,
                                    'hiddenMessage': hidden_message,
                                    'commentsEnabled': comments_enabled,
                                    'callbackUrl': callback_url,
                                    'payload': payload,
                                    'expiredIn': expired_in
                                  })

    async def invoice_list(self, limit: int = 100, offset: int = 0):
        """ Get list of invoices

        :param `limit` [int]: Limit of invoices list
        :param `offset` [int]: Offset of invoices list

        """

        return await self.request(method = 'tg-invoices',
                                  request_method = 'GET',
                                  params = {
                                    'limit': limit,
                                    'offset': offset
                                  })

    async def invoice_info(self, invoice_id: str):
        """ Get invoice info

        :param `invoice_id` [str]: Invoice id of invoice

        """

        return await self.request(method = f'tg-invoices/{invoice_id}',
                                  request_method = 'GET')

    async def invoice_delete(self, invoice_id: str):
        """ Delete invoice

        :param `invoice_id` [str]: Invoice id of invoice

        """

        return await self.request(method = f'tg-invoices/{invoice_id}',
                                  request_method = 'DELETE')

