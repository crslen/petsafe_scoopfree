import petsafe_scoopfree as sf

# replace with your email address
client = sf.PetSafeClient(email="<email>")
client.request_code()

# check your email for a code
code = input("Enter email code: ")
token = client.request_tokens_from_code(code)

print("email:", client.email)
print("id_token:", client.id_token)
print("refresh_token:", client.refresh_token)
print("access_token:", client.access_token)
