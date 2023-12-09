from typing import Union


class Cheque:

    """ Cheque methods wrapper. 
    
    Available methods:

    * cheque_create()
    * cheque_list()
    * cheque_info()
    * cheque_edit()
    * cheque_delete()

    """

    async def cheque_create(self, currency: str, 
                                  amount: Union[int, float], 
                                  ref_program: int = 0,
                                  activations: int = 1, 
                                  password: str = '', description: str = '',
                                  send_notifications: bool = True, 
                                  enable_captcha: bool = True,
                                  telegram_resources_ids: list = [], 
                                  for_premium: bool = False,
                                  linked_wallet: bool = False, 
                                  disabled_languages: list = []):
        """ Create cheque

        :param `currency` [str]: Currency of cheque
        :param `amount` Union[int, float]: Total amount of cheque
        :param `activations` [int]: Activations of cheque
        :param `ref_program` [int]: Referral program of cheque
        :param `password` [str]: Password of cheque
        :param `description` [str]: Description of cheque
        :param `send_notifications` [bool]: Is send notifications of cheque
        :param `enable_captcha` [bool]: Is enable captcha of cheque
        :param `telegram_resources_ids` [list]: Telegram resources ids of cheque
        :param `for_premium` [bool]: Is for premium of cheque
        :param `linked_wallet` [bool]: Is linked wallet of cheque
        :param `disabled_languages` [list]: Disabled languages of cheque

        """
		
        return await self.request(method = 'multi-cheque',
                                  request_method = 'POST',
                                  json = {
                                    'currency': currency,
                                    'chequePerUser': amount / activations,
                                    'usersNumber': activations,
                                    'refProgram': ref_program,
                                    'password': password,
                                    'description': description,
                                    'sendNotifications': send_notifications,
                                    'enableCaptcha': enable_captcha,
                                    'telegramResourcesIds': telegram_resources_ids,
                                    'forPremium': for_premium,
                                    'linkedWallet': linked_wallet,
                                    'disabledLanguages': disabled_languages
                                  })

    async def cheque_list(self, limit: int = 100, offset: int = 0):
        """ Get list of cheques

        :param `limit` [int]: Limit of cheques list
        :param `offset` [int]: Offset of cheques list

        """

        return await self.request(method = 'multi-cheque',
                                  request_method = 'GET',
                                  params = {
                                    'limit': limit,
                                    'offset': offset
                                  })

    async def cheque_info(self, cheque_id: str):
        """ Get cheque info

        :param `cheque_id` [str]: Cheque id of cheque

        """

        return await self.request(method = f'multi-cheque/{cheque_id}',
                                  request_method = 'GET')

    async def cheque_edit(self, cheque_id: str, password: str = '', 
                                description: str = '',
								send_notifications: bool = True, 
                                enable_captcha: bool = True,
                                telegram_resources_ids: list = [], 
                                for_premium: bool = False,
                                linked_wallet: bool = False, 
                                disabled_languages: list = []):
        """ Edit cheque

        :param `password` [str]: Password of cheque
        :param `description` [str]: Description of cheque
        :param `send_notifications` [bool]: Is send notifications of cheque
        :param `enable_captcha` [bool]: Is enable captcha of cheque
        :param `telegram_resources_ids` [list]: Telegram resources ids of cheque
        :param `for_premium` [bool]: Is for premium of cheque
        :param `linked_wallet` [bool]: Is linked wallet of cheque
        :param `disabled_languages` [list]: Disabled languages of cheque

        """

        return await self.request(method = f'multi-cheque/{cheque_id}',
                                  request_method = 'PUT',
                                  json = {
                                    'password': password,
                                    'description': description,
                                    'sendNotifications': send_notifications,
                                    'enableCaptcha': enable_captcha,
                                    'telegramResourcesIds': telegram_resources_ids,
                                    'forPremium': for_premium,
                                    'linkedWallet': linked_wallet,
                                    'disabledLanguages': disabled_languages
                                  })

    async def cheque_delete(self, cheque_id: str):
        """ Delete cheque

        :param `cheque_id` [str]: Cheque id of cheque

        """

        return await self.request(method = f'multi-cheque/{cheque_id}',
                                  request_method = 'DELETE')

