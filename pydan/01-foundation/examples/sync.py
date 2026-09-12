import time


def fetch_weather():
    print("Fetching weather data...")
    time.sleep(4)
    print("Weather data fetched")


def fetch_news():
    print("Fetching news data...")
    time.sleep(2)
    print("News data fetched")


def main():
    startTime = time.time()
    fetch_weather()
    fetch_news()
    endTime = time.time()

    print(f"Total time taken: {endTime - startTime} seconds")


main()
