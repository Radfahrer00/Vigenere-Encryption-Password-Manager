from CipherAlphabet import CipherAlphabet
from VigenereCipher import VigenereCipher


def main_menu():
    """
    Displays the main menu and prompts the user for an action.

    Returns:
        str: The user's choice.
    """
    print("Main Menu:")
    print("1. Add a new password")
    print("2. See all encrypted passwords")
    print("3. Retrieve password for a service")
    print("4. Exit")
    choice = input("What do you want to do? Enter the number: ")
    return choice


def add_password(passwords, alphabet, encryption_key):
    """
    Adds a new password to the dictionary after encrypting it.

    Parameters:
        passwords (dict): A dictionary to store service names as keys and encrypted passwords as values.
        alphabet (CipherAlphabet): The alphabet used for encrypting the password.
        encryption_key (str): The key to encrypt the password.
    """
    service = input("Enter the service (e.g., 'email', 'social media'): ")
    password = input("Enter the password: ")

    encrypted_password = vigenere_encryption(alphabet, password, encryption_key)
    passwords[service] = encrypted_password
    print("Password added successfully!")


def vigenere_encryption(alphabet, password, encryption_key):
    """
    Encrypts a password using the Vigenère cipher.

    Parameters:
        alphabet (CipherAlphabet): The alphabet used for the Caesar cipher encryption.
        password (str): The password to be encrypted.
        encryption_key(str): The key to encrypt the password.

    Returns:
        str: The encrypted password.
    """
    cipher = VigenereCipher(alphabet=alphabet)
    encrypted_password = cipher.encrypt(password, encryption_key)
    return encrypted_password


def see_all_passwords(passwords):
    """
    Displays all stored services and their corresponding encrypted passwords.

    Parameters:
        passwords (dict): The dictionary containing the services and their encrypted passwords.
    """
    if passwords:
        print("---------------Your passwords---------------")
        for service, password in passwords.items():
            print(f"Service: {service}, Password: {password}")
        print("--------------------------------------------")
    else:
        print("No passwords stored.")


def retrieve_password_for_service(passwords, alphabet, encryption_key):
    """
    Allows the user to select a service and decrypts the password for that service.

    Parameters:
        passwords (dict): The dictionary containing the services and their encrypted passwords.
        alphabet (CipherAlphabet): The alphabet used for decrypting the password.
        encryption_key (str): The key to decrypt the password
    """
    if not passwords:
        print("No passwords stored.")
        return

    print("----------Services available----------")
    services = list(passwords.keys())
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service}")
    print("--------------------------------------")

    while True:
        try:
            choice = int(input("Enter the number for the service you want to retrieve the password for: "))
            if 1 <= choice <= len(services):
                selected_service = services[choice - 1]
                password_to_decrypt = passwords[selected_service]
                print(f"The encrypted password for {selected_service} is: {password_to_decrypt}")
                cipher = VigenereCipher(alphabet=alphabet)
                decrypted_password = cipher.decrypt(password_to_decrypt, encryption_key)
                print(f"The decrypted password for {selected_service} is: {decrypted_password}")
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a number.")


def main():
    """
    The main function to run the password manager program.
    """
    alphabet = CipherAlphabet("0", "z")
    passwords = {}
    print("Welcome to the Classic Cryptography Password Manager!")

    # Prompt the user for an encryption key
    while True:
        encryption_key = input("Please enter an encryption key: ")
        if len(encryption_key) == 0:
            print("Please enter at least one character!")
        else:
            break

    while True:
        choice = main_menu()
        if choice == "1":
            add_password(passwords, alphabet, encryption_key)
        elif choice == "2":
            see_all_passwords(passwords)
        elif choice == "3":
            retrieve_password_for_service(passwords, alphabet, encryption_key)
        elif choice == "4":
            print("Exiting. Have a good day!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
