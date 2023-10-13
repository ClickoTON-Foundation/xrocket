from typing import Union

class Subscription:
    """ Subscription methods wrapper.
    
    Available methods:

    * subscription_create()
    * subscription_list()
    * subscription_info()
    * subscription_delete()
    * subscription_check()
    * subscription_interval_create()
    * subscription_interval_info()
    * subscription_interval_edit()
    * subscription_interval_delete()

    """

    async def subscription_create(self, name: str, currency: str, 
                                        chat_id: Union[int, str],
                                        referral_percent: Union[int, float], 
                                        return_url: str,
                                        description: str = '', interval: list = []):
        """ Create subscription

        :param `name` [str]: Name of subscription
        :param `currency` [str]: Currency of subscription
        :param `chat_id` Union[int, str]: Telegram chat id of subscription
        :param `referral_percent` Union[int, float]: Referral percent of subscription
        :param `return_url` [str]: Return url of subscription
        :param `description` [str]: Description of subscription
        :param `interval` [list]: Intervals list of subscription

        """

        return await self.request(method = 'subscriptions',
                                  request_method = 'POST',
                                  json = {
                                    'name': name,
                                    'currency': currency,
                                    'tgResource': chat_id,
                                    'referralPercent': referral_percent,
                                    'returnUrl': return_url,
                                    'description': description,
                                    'interval': interval
                                  })

    async def subscription_list(self, limit: int = 100, offset: int = 0):
        """ Get list of subscriptions

        :param `limit` [int]: Limit of subscriptions list
        :param `offset` [int]: Offset of subscriptions list

        """

        return await self.request(method = 'subscriptions',
                                  request_method = 'GET',
                                  params = {
                                    'limit': limit,
                                    'offset': offset
                                  })

    async def subscription_info(self, subscription_id: str):
        """ Get subscription info

        :param `subscription_id` [str]: Subscription id of subscription

        """

        return await self.request(method = f'subscriptions/{subscription_id}',
                                  request_method = 'GET')

    async def subscription_delete(self, subscription_id: str):
        """ Delete subscription

        :param `subscription_id` [str]: Subscription id of subscription

        """

        return await self.request(method = f'subscriptions/{subscription_id}',
                                  request_method = 'DELETE')

    async def subscription_check(self, subscription_id: str, user_id: int):
        """ Check subscription

        :param `subscription_id` [str]: Subscription id of subscription
        :param `user_id` [int]: Telegram user id of subscription

        """

        return await self.request(method = f'subscriptions/check/{subscription_id}',
                                  json = {
                                    'userId': user_id
                                  },
                                  request_method = 'POST')

    async def subscription_interval_create(self, subscription_id: str,
                                                 interval: str, 
                                                 amount: Union[int, float], 
                                                 status: str):
        """ Create subscription interval

        :param `interval` [str]: Interval of subscription interval
        :param `amount` Union[int, float]: Amount of subscription interval
        :param `status` [str]: Status of subscription interval

        """

        return await self.request(method = f'subscriptions/{subscription_id}/interval',
                                  request_method = 'POST',
                                  json = {
                                    'interval': interval,
                                    'amount': amount,
                                    'status': status
                                  })

    async def subscription_interval_info(self, subscription_id: str, 
                                               interval_code: str):
        """ Get subscription interval info

        :param `subscription_id` [str]: Subscription id of subscription
        :param `interval_code` [str]: Interval code of subscription interval

        """

        return await self.request(
            method = f'subscriptions/{subscription_id}/interval/{interval_code}',
            request_method = 'GET'
        )

    async def subscription_interval_edit(self, subscription_id: str, interval_code: str,
                                               status: str):
        """ Edit subscription interval

        :param `subscription_id` [str]: Subscription id of subscription
        :param `interval_code` [str]: Interval code of subscription interval
        :param `status` [str]: New status of subscription interval

        """

        return await self.request(
            method = f'subscriptions/{subscription_id}/interval/{interval_code}',
            request_method = 'PUT',
            json = {
                'status': status
            }
        )
    
    async def subscription_interval_delete(self, subscription_id: str, 
                                                 interval_code: str):
        """ Delete subscription interval

        :param `subscription_id` [str]: Subscription id of subscription
        :param `interval_code` [str]: Interval code of subscription interval

        """

        return await self.request(
            method = f'subscriptions/{subscription_id}/interval/{interval_code}',
            request_method = 'DELETE'
        )

