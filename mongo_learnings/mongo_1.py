###https://pymodm.readthedocs.io/en/latest/getting-started.html
from pymodm import connect

# Connect to MongoDB and call the connection "my-app".
connect("mongodb://localhost:27017/myDatabase", alias="my-app")
