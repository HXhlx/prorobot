from aiohttp import request


async def get_weather_of_city(city: str) -> str:
    weather_type = ['now', 'forecast', 'hourly', 'lifestyle']
    parameters = {'version': 'v6', 'city': city}
    url = 'https://www.tianqiapi.com/api/?'
    async with request('GET', url, params=parameters) as resp:
        print(resp.url)
        data = await resp.json()
        return f"{city}的天气是{data.get('wea', '')},温度{data.get('tem', '')}℃,湿度{data.get('humidity', '')},能见度{data.get('visibility', '')}"
