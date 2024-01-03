import pyotp
import time

totp = pyotp.TOTP('base32secret3232')
a = totp.now() # => '492039'

# OTP verified for current time
print(totp.verify(a)) # => True
time.sleep(30)
print(totp.verify(a)) # => False
