class TimeSeries:

    """ TimeSeries methods wrapper.

    Available methods:

    * time_series_pair()

    """

    async def time_series_pair(self, pair: str, start_date: str,
                                     end_date: str, period: str):
        """ Get time series for pair
        
        :param `pair` [str]: Pair name of rates
        :param `start_date` [str]: Start date of time series
        :param `end_date` [str]: End date of time series
        :param `period` [str]: Period of time series
        
        """

        return await self.request(method = f'time-series/{pair}',
                                  request_method = 'GET',
                                  params = {
                                    'startDate': start_date,
                                    'endDate': end_date,
                                    'period': period
                                  })
