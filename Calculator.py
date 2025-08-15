def add_numbers(first_val, second_val):
   
    return first_val + second_val

def subtract_numbers(first_val, second_val):
    
    return first_val - second_val

def multiply_numbers(first_val, second_val):
   
    return first_val * second_val

def divide_numbers(first_val, second_val):
    
    if second_val == 0:
        # Instead of crashing, we give a friendly heads-up!
        return "Oops! You can't divide by zero. Let's pick different numbers next time. 🚫"
    return first_val / second_val

def show_your_options():
    
    print("\n--- What Kind of Math Adventure Are We On Today? ---")
    print("1. Add (+) - Bringing numbers together!")
    print("2. Subtract (-) - Finding the difference!")
    print("3. Multiply (*) - Making numbers bigger (or smaller if negative)!")
    print("4. Divide (/) - Sharing numbers fairly!")
    print("5. Say Goodbye - Ready to take a break?")

def fire_up_the_calculator():
    
    print("Greetings, Math Wizard! I'm your trusty calculator. ✨")

    while True: # We'll keep going until you tell me to stop.
        show_your_options()
        your_choice = input("Just type the number of your choice (1-5): ").strip()

        if your_choice == '5':
            print("It was fun doing math with you! Come back anytime. 👋")
            break 

        # Let's make sure they picked a valid operation.
        if your_choice not in ('1', '2', '3', '4'):
            print("Hmm, that's not quite one of my options. Please choose a number from 1 to 5.")
            continue # Let's show the menu again.

        try:
           
            first_number_str = input("Alright, what's your FIRST number? ").strip()
            first_number = float(first_number_str)
            second_number_str = input("Great! Now, what's your SECOND number? ").strip()
            second_number = float(second_number_str)

        except ValueError:
            # Uh oh! If they type "apple" instead of "5", we catch it here.
            print("Whoops! I need actual numbers to do math. Looks like you typed something else. Let's try again from the start!")
            continue # Go back and ask for input again.

        # Now, let's figure out which operation to perform based on their choice.
        final_result = None # We'll store our answer here.
        operation_char = '' # And the symbol for showing the calculation.

        if your_choice == '1':
            final_result = add_numbers(first_number, second_number)
            operation_char = '+'
        elif your_choice == '2':
            final_result = subtract_numbers(first_number, second_number)
            operation_char = '-'
        elif your_choice == '3':
            final_result = multiply_numbers(first_number, second_number)
            operation_char = '*'
        elif your_choice == '4':
            final_result = divide_numbers(first_number, second_number)
            operation_char = '/'

        if final_result is not None:
            # If it's our special error message from division, print that directly.
            if isinstance(final_result, str) and "Error" in final_result:
                print(final_result)
            else:
                # Otherwise, display the beautiful calculation!
                print(f"\n✨ Ta-da! ✨")
                print(f"You asked me to calculate: {first_number} {operation_char} {second_number}")
                print(f"And the answer is: {final_result}")
                print(f"Wasn't that fun?\n")
        else:
            # Just in case something unexpected happened.
            print("Hmm, I had a little trouble with that calculation. Could you try one more time?")

# This little line makes sure our calculator only starts when you open this file directly.
if __name__ == "__main__":
    fire_up_the_calculator()
