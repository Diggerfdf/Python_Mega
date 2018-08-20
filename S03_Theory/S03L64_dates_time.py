from datetime import datetime

then = datetime(1900, 12, 31, 20, 12, 59, 83845)
now = datetime.now()
whenever = datetime.strptime("2017-12-31", "%Y-%m-%d")
whenever_test = datetime.strptime("23/07/1975", "%d/%m/%Y")

whenever.strftime("%Y")

print(whenever)
print(whenever_test)
print(whenever.strftime("%Y"))
