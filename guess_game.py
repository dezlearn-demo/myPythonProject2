import random

def guess_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0

    print("1 से 10 के बीच एक नंबर चुना गया है। कृपया उसका अनुमान लगाएँ।")

    while True:
        try:
            guess = int(input("अपना अनुमान दर्ज करें: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("कृपया 1 और 10 के बीच ही नंबर दर्ज करें।")
                continue

            if guess == number_to_guess:
                print(f"बधाई हो! आपने सही नंबर {number_to_guess} {attempts} प्रयास में पहचान लिया।")
                break
            elif guess < number_to_guess:
                print("आपका अनुमान छोटा है। फिर से प्रयास करें।")
            else:
                print("आपका अनुमान बड़ा है। फिर से प्रयास करें।")
        except ValueError:
            print("कृपया एक वैध संख्या दर्ज करें।")

if __name__ == "__main__":
    guess_game()
