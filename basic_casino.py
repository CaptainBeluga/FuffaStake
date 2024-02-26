from web3 import Web3
from dotenv import dotenv_values
import os

API_URL = "https://goerli.infura.io/v3/<API_KEY>" #infura.io
w3 = Web3(Web3.HTTPProvider(API_URL))


ENV = dotenv_values(".env")
bankAddress = ENV["BANK_ADDRESS"]
bankPrivateKey = ENV["BANK_PRIVATE_KEY"]

playerAddress = ENV["PLAYER_ADDRESS"]
playerPrivateKey = ENV["PLAYER_PRIVATE_KEY"]

def test_connection():
    return Web3(Web3.HTTPProvider(API_URL)).is_connected()

def balance(address):
    return w3.from_wei(w3.eth.get_balance(address), 'ether')


def send(amount,sender,receiver,senderKey):   

    tx = {
        "nonce" : w3.eth.get_transaction_count(sender),
        "to" : receiver,
        "value" : w3.to_wei(amount,"ether"),
        "gasPrice" : w3.to_wei(1, 'gwei')

    }

    gas = w3.eth.estimate_gas(tx)
    tx["gas"] = gas

    signed_tx = w3.eth.account.sign_transaction(tx,senderKey)


    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    print("\nWAITING FOR TRANSACTION.....\n")
    w3.eth.wait_for_transaction_receipt(tx_hash)


def on_started():
    if(test_connection()):

        os.system("cls")
        print(f"YOUR AMOUNT => {balance(playerAddress)} ETH\n")

        bet = float(input("PLACE YOUR BET => "))
        send(bet,playerAddress,bankAddress,playerPrivateKey)

        return bet
    else:
        print("\nFUFFA STAKE APIs NOT AVAILABLE ATM !\n")
        exit()