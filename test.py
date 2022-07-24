import jwt
from datetime import datetime, timedelta

encoded_jwt = jwt.encode({}, "secret", algorithm="HS256")

print('jwt')
print(encoded_jwt)

timestamp = datetime.now() + timedelta(hours = 1)
print(timestamp)

decode_data = jwt.decode(encoded_jwt, 'secret123', algorithms=['HS256'])
print(decode_data)