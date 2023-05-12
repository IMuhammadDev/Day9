from art import logo

print(logo)

condition = True
dic_of_all = {}
max_key = ""
max_val = 0

while condition:
    name = input("what is your name ?\n")
    bid = int(input("How much is your bid ? \n$"))
    dic_of_all[name]=bid
    ask = input("if there other user (yes or no) ? \n")
    if ask == "no":
        condition = False

for key in dic_of_all:
    if dic_of_all[key] > max_val:
        max_key = key
print(f"Winner off {max_key} with {dic_of_all[max_key]}$ ")