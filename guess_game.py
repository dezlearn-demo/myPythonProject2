import random

def guess_game():
    """
    एक साधारण संख्या अनुमान लगाने का खेल (1 से 10 के बीच)
    A simple number guessing game between 1 and 10
    """
    # Generate random number between 1 and 10
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("स्वागत है! संख्या अनुमान लगाने के खेल में!")
    print("मैंने 1 से 10 के बीच एक संख्या सोची है।")
    print("आपको इसे अनुमान लगाना है!")
    
    while True:
        try:
            # Get user input
            guess = int(input("\nकृपया अपना अनुमान दर्ज करें (1-10): "))
            attempts += 1
            
            # Check if guess is within valid range
            if guess < 1 or guess > 10:
                print("कृपया 1 से 10 के बीच की संख्या दर्ज करें!")
                continue
            
            # Check the guess
            if guess < secret_number:
                print("आपका अनुमान बहुत कम है! फिर से कोशिश करें।")
            elif guess > secret_number:
                print("आपका अनुमान बहुत अधिक है! फिर से कोशिश करें।")
            else:
                print(f"\nबधाई हो! आपने सही अनुमान लगाया!")
                print(f"सही संख्या {secret_number} थी।")
                print(f"आपने कुल {attempts} प्रयासों में सफलता पाई!")
                break
                
        except ValueError:
            print("कृपया एक वैध संख्या दर्ज करें!")

if __name__ == "__main__":
    guess_game()