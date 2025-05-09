import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination + joke data
destinations = {
    "mountains": ["Rishikesh", "Leh-Ladakh", "Mussoorie"],
    "beaches": ["Goa", "Alleppey", "Kovalam"],
    "cities": ["Delhi", "Agra", "Mumbai", "Bangalore"]
}

jokes = [
    "Why do programmers like nature? 🌿 It has no bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "Why don’t scientists trust atoms anymore? Because of all that hot gossip!"
]

# Helper function to normalize user input (remove extra spaces, add lowercase)
def normalize_input(text):
    return re.sub(r'[^\w\s]', '', text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestion)
def recommend():
    print(f"{Fore.BLUE}🧭 TravelBot: Beaches, mountains, or cities?")
    preference = input(f"{Fore.YELLOW}➤ You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(f"{Fore.GREEN}✈️ TravelBot: How about {suggestion}?")

        answer = input(f"{Fore.YELLOW}➤ You (yes/no): ").strip().lower()
        if answer == "yes":
            print(f"{Fore.CYAN}🌟 TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(f"{Fore.YELLOW}🔁 TravelBot: Let’s try another...")
            recommend()
        else:
            print(f"{Fore.RED}❌ TravelBot: Sorry, I didn’t understand that.")
    else:
        print(f"{Fore.RED}❌ TravelBot: Sorry, I don’t have that type of destination.")

# Show packing tips based on user's destination and duration
def packing_list():
    print(f"{Fore.BLUE}📦 TravelBot: Where to?")
    location = normalize_input(input(f"{Fore.YELLOW}➤ You: "))
    duration = input(f"{Fore.YELLOW}➤ How long? (in days): ")

    print(f"{Fore.GREEN}📋 TravelBot: Packing tips for {duration} days in {location}:")

    if "beach" in location:
        print("- Pack your swimsuit, flip-flops, and sunscreen.")
    elif "mountain" in location:
        print("- Bring warm clothes, boots, and a camera.")
    elif "city" in location:
        print("- Don’t forget walking shoes and maps/apps.")
    else:
        print("- General tip: check the weather forecast.")

# Tell a random joke
def tell_joke():
    print(f"{Fore.MAGENTA}😂 TravelBot: {random.choice(jokes)}")

# Help menu
def show_help():
    print(f"{Fore.MAGENTA}🆘 TravelBot Help")
    print(f"{Fore.CYAN}- Type 'recommend' to get a travel suggestion.")
    print(f"{Fore.CYAN}- Type 'packing' for a list of what to bring.")
    print(f"{Fore.CYAN}- Type 'joke' if you’d like a laugh.")
    print(f"{Fore.CYAN}- Type 'bye' to end the conversation.")

# Run the chatbot
if __name__ == "__main__":
    print(f"{Fore.CYAN}👋 Hello! I’m TravelBot. 🌍")
    print(f"{Fore.CYAN}Type 'help' to see what I can do.")

    while True:
        user_input = input(f"{Fore.YELLOW}➤ You: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input:
            recommend()
        elif "packing" in user_input:
            packing_list()
        elif "joke" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "bye" in user_input or "exit" in user_input:
            print(f"{Fore.CYAN}👋 Bye! Safe travels! Goodbye!")
            break
        else:
            print(f"{Fore.RED}🤖 TravelBot: Could you rephrase?")
