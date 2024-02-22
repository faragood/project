from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tommorow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tommorow:", tommorow.strftime("%Y-%m-%d"))
