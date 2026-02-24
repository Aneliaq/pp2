from datetime import datetime, timedelta

# 1. Subtract five days from current date
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)

# 2. Print yesterday, today, tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

# 3. Drop microseconds from datetime
now_no_microseconds = today.replace(microsecond=0)
print(now_no_microseconds)

# 4. Calculate difference between two dates in seconds
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 24, 15, 30, 0)
diff = date2 - date1
diff_seconds = diff.total_seconds()
print(diff_seconds)

