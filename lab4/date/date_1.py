from datetime import datetime, timedelta
x = datetime.now()
y = x - timedelta(days=5)
print("Current date:", x.strftime("%Y-%m-%d"))
print("Subtract five days from current date:", y.strftime("%Y-%m-%d"))
