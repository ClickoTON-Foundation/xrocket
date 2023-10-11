from httpx import AsyncClient
from .trade import Account, OrderBook, Orders, Pairs, Rates, TimeSeries


class TradeAPI(Account, OrderBook, Orders, Pairs, Rates, TimeSeries):
    """
    Class for working with trade.ton-rocket.com.

    :author: shibdev [t.me/shibdev]

    :license: MIT
    """

    def __init__(self, api_key: str, api_url = "https://trade.ton-rocket.com"):
        """
        Class initialization.

        :param `api_key` [str]: API key
        """

        self.api_key = api_key
        self.api_url = api_url
        self.client = AsyncClient(headers={'Rocket-Exchange-Key': self.api_key})

    async def request(self, method: str, request_method = "POST", **kwargs):
        """ Send request to Exchange API 
        
        :param `method` [str]: Method of API
        :param `request_method` [str]: Request method of API
        :param `*kwargs`: Other params
        """
        try:
            request = await self.client.request(
                method = request_method,
                url = self.api_url + "/" + method,
                **kwargs
            )
            try:
                res = request.json()
            except BaseException:
                return {'error': 'Invalid response', 'context': request.text}

            if res.get('errors'):
                return {'error': res['errors'][0]['error']}

            return res
        except BaseException as e:
            return {'error': f"{e}"}
