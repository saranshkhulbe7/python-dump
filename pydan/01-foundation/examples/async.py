import time
import asyncio


async def fetch_weather():
    print("Fetching weather data...")
    await asyncio.sleep(4)
    print("Weather data fetched")


async def fetch_news():
    print("Fetching news data...")
    await asyncio.sleep(2)
    print("News data fetched")


async def main():
    startTime = time.time()
    await asyncio.gather(fetch_weather(), fetch_news())
    endTime = time.time()

    print(f"Total time taken: {endTime - startTime} seconds")


await main()
