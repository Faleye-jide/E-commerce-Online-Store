from ratelimit import limits, sleep_and_retry

# 2 calls per minute
CALLS = 5
RATE_LIMIT = 60

@sleep_and_retry
@limits(calls=CALLS, period=RATE_LIMIT)
def check_api_limit():
    return 