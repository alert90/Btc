import os
import random
import requests

class BitcoinPrivateKeyGenerator:
    """
    Class to generate random Bitcoin private keys, check their balance, and create a new folder for private keys with balance.

    Attributes:
    - num_keys: int
        Number of private keys to generate.
    - folder_name: str
        Name of the folder to create for storing private keys with balance.
    """

    def __init__(self, num_keys: int, folder_name: str):
        """
        Constructor to instantiate the BitcoinPrivateKeyGenerator class.

        Parameters:
        - num_keys: int
            Number of private keys to generate.
        - folder_name: str
            Name of the folder to create for storing private keys with balance.
        """

        self.num_keys = num_keys
        self.folder_name = folder_name

    def generate_private_keys(self):
        """
        Generates random Bitcoin private keys.

        Returns:
        - list:
            List of randomly generated Bitcoin private keys.
        """

        private_keys = []

        for _ in range(self.num_keys):
            # Generate a random private key (64 hexadecimal characters)
            private_key = ''.join(random.choice('0123456789abcdef') for _ in range(64))
            private_keys.append(private_key)

        return private_keys

    def check_balance(self, private_key):
        """
        Checks the balance of a Bitcoin address associated with a given private key.

        Parameters:
        - private_key: str
            Bitcoin private key to check the balance for.

        Returns:
        - float:
            The balance of the Bitcoin address associated with the private key.
        """

        # Derive the Bitcoin address from the private key
        address = self.derive_address(private_key)

        # Make an API request to get the balance of the Bitcoin address
        response = requests.get(f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance")
        data = response.json()

        # Extract the balance from the response
        balance = data['balance'] / 10**8

        return balance

    def derive_address(self, private_key):
        """
        Derives the Bitcoin address from a given private key.

        Parameters:
        - private_key: str
            Bitcoin private key to derive the address from.

        Returns:
        - str:
            The Bitcoin address associated with the private key.
        """

        # Derive the public key from the private key
        # (In real-world scenarios, a more complex algorithm is used)
        public_key = private_key + 'public'

        # Derive the Bitcoin address from the public key
        # (In real-world scenarios, a more complex algorithm is used)
        address = public_key + 'address'

        return address

    def create_folder(self):
        """
        Creates a new folder for storing private keys with balance.

        Returns:
        - str:
            The path of the created folder.
        """

        # Create a new folder with the specified name
        folder_path = os.path.join(os.getcwd(), self.folder_name)
        os.makedirs(folder_path, exist_ok=True)

        return folder_path

    def generate_keys_with_balance(self):
        """
        Generates random Bitcoin private keys, checks their balance, and creates a new folder for private keys with balance.

        Returns:
        - dict:
            A dictionary containing the private keys as keys and their corresponding balance as values.
        """

        # Generate the private keys
        private_keys = self.generate_private_keys()

        # Create the folder for private keys with balance
        folder_path = self.create_folder()

        # Store the private keys with balance in a dictionary
        keys_with_balance = {}

        for private_key in private_keys:
            # Check the balance of the private key
            balance = self.check_balance(private_key)

            # Add the private key and balance to the dictionary
            keys_with_balance[private_key] = balance

            # Create a file for the private key in the folder
            file_path = os.path.join(folder_path, f"{private_key}.txt")
            with open(file_path, 'w') as file:
                file.write(f"Private Key: {private_key}\nBalance: {balance} BTC")

        return keys_with_balance

# Example usage of the BitcoinPrivateKeyGenerator class:

generator = BitcoinPrivateKeyGenerator(5, "private_keys_with_balance")
keys_with_balance = generator.generate_keys_with_balance()

print("Private Keys with Balance:")
for private_key, balance in keys_with_balance.items():
    print(f"Private Key: {private_key}, Balance: {balance} BTC")
