from typing import Union
import os


class App:

    """ App methods wrapper.

    Available methods:

    * info()
    * transfer()
    * withdraw()

    """

    async def info(self):
        """ Get information about your application"""
        return await self.request(method = 'app/info',
                                  request_method = 'GET')

    async def transfer(self, user_id: int, currency: str, amount: Union[int, float],
                             transfer_id: Union[str, None] = None, description: str = ''):
        """ Make transfer of funds to another user

        :param `user_id` [int]: Telegram user id
        :param `currency` [str]: Currency of transfer
        :param `amount` Union[int, float]: Amount of transfer
        :param `transfer_id` [int]: Id of transfer
        :param `description` [str]: Description of transfer

        """

        if not transfer_id:
            transfer_id = os.urandom(32).hex()

        return await self.request(method = 'app/transfer',
                                  request_method = 'POST',
                                  json = {
                                    'tgUserId': user_id,
                                    'currency': currency,
                                    'amount': amount,
                                    'transferId': transfer_id,
                                    'description': description
                                  })

    async def withdrawal(self, network: str, address: str, currency: str, amount: Union[int, float],
                               withdrawal_id: Union[str, None] = None, comment: str = ''):
        """ Make withdrawal of funds to external wallet

        :param `network` [str]: Network of withdrawal
        :param `address` [str]: Address of withdrawal
        :param `currency` [str]: Currency of withdrawal
        :param `amount` Union[int, float]: Amount of withdrawal
        :param `withdrawal_id` [int]: Id of withdrawal
        :param `comment` [str]: Comment of withdrawal

        """

        if not withdrawal_id:
            withdrawal_id = os.urandom(32).hex()

        return await self.request(method = 'app/withdrawal',
                                  request_method = 'POST',
                                  json = {
                                    'network': network,
                                    'address': address,
                                    'currency': currency,
                                    'amount': amount,
                                    'withdrawalId': withdrawal_id,
                                    'comment': comment
                                  })
