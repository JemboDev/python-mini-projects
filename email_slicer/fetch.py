# Your task is to write a python script that can fetch
# the username and domain name from the email.
#
# by JemboDev @ 07.02.21

email = input("Hey, enter your e-mail here: ")

while "@" not in email:
    print("Invalid e-mail, try again!")
    email = input("Hey, enter your e-mail here: ")

split_email = email.split("@")

username = split_email[0]
domain = split_email[1]

print(f"username: {username}")
print(f"domain: {domain}")
