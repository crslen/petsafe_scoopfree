# PetSafe Scoopfree - Python API
Connect and control a PetSafe Scoopfree device using the PetSafe-Scoopfree API.

> **BREAKING CHANGE:** Version 2.0 uses the new PetSafe API.
> You will need to request new tokens.

> PetSafe will lock your account if you request data more often than once per 5 minutes.

## Installation
`pip install petsafe-scoopfree`

If installing from source code,
`python setup.py install`

## Login tokens
You **must** use tokens to interact with the PetSafe Scoopfree API.  
There are two methods to retrieve tokens:

#### Get tokens using command line
1. Execute `python -m petsafe_scoopfree [email_address]` to request an email code.
2. Check your email for an email code from PetSafe.
3. Enter your code to generate tokens.

#### Get tokens using Python
```python
import petsafe_scoopfree as sf


# replace with your email address
client = sf.PetSafeClient(email="email@example.com")
client.request_code()

# check your email for a code
code = input("Enter email code: ")
token = client.request_tokens_from_code(code)

print("email:", client.email)
print("id_token:", client.id_token)
print("refresh_token:", client.refresh_token)
print("access_token:", client.access_token)
```


## Example usage
#### List devices

```python
import petsafe_scoopfree as sf

client = sf.PetSafeClient(email="email@example.com",
                       id_token="YOUR_ID_TOKEN",
                       refresh_token="YOUR_REFRESH_TOKEN",
                       access_token="YOUR_ACCESS_TOKEN")
devices = sf.devices.get_scoopers(client)

# print all devices
for device in devices:
    print(device)

```
#### Rake scooper
```python
import petsafe_scoopfree as sf

client = sf.PetSafeClient(email="email@example.com",
                       id_token="YOUR_ID_TOKEN",
                       refresh_token="YOUR_REFRESH_TOKEN",
                       access_token="YOUR_ACCESS_TOKEN")
devices = sf.devices.get_scoopers(client)

# get the first scooper
scooper = devices[0]
scooper.rake_now()

```
#### reset count
```python
import petsafe_scoopfree as sf

client = sf.PetSafeClient(email="email@example.com",
                       id_token="YOUR_ID_TOKEN",
                       refresh_token="YOUR_REFRESH_TOKEN",
                       access_token="YOUR_ACCESS_TOKEN")
devices = sf.devices.get_scoopers(client)

# get the first scooper
scooper = devices[0]
scooper.reset()

```
#### reset rake delay to 25 seconds
```python
import petsafe_scoopfree as sf

client = sf.PetSafeClient(email="email@example.com",
                       id_token="YOUR_ID_TOKEN",
                       refresh_token="YOUR_REFRESH_TOKEN",
                       access_token="YOUR_ACCESS_TOKEN")
devices = sf.devices.get_scoopers(client)

# get the first scooper
scooper = devices[0]
scooper.modify_timer(amount=25)

```

## Contributing
All contributions are welcome. 
Please, feel free to create a pull request!
