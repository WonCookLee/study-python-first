from random import randint
from requests import get

# print("Welcome Python Casino")
#
# pc_choice = randint(1, 50)
# playing = True
#
# while playing:
#     user_choice = int(input("Choose number."))
#     if user_choice == pc_choice:
#         print("you won!")
#         playing = False
#     elif user_choice > pc_choice:
#         print("Lower!")
#     elif user_choice < pc_choice:
#         print("Higher!")

websites = (
    "https://google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com"
)

results = {
    
}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    # print(response.status_code)
    
    if (response.status_code == 200) :
        # print(f"{website} is ok")
        results[website] = "OK"
    else :
        # print(f"{website} is not ok")
        results[website] = "FAILED"

print(results)