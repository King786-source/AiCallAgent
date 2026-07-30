from ai import ask_ai

print("==================================")
print("     AI Call Agent Started")
print("==================================")

user_name = input("Enter your name: ")

response = ask_ai(user_name)

print(f"Hello, {user_name}!")
print(response)
print("Welcome to AI Call Agent 🚀")