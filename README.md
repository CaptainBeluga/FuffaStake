# FUFFA STAKE
Mini-casino dApp (decentralized application) | (basic shell games, GUI soon) | BET using ETH 

- **Fuffa Stake Minigames**:
    - 100% customizable and you can create your own
    - Stored in `games` directory 
    - Must include ```from basic_casino import *``` to access Casino Basic functions
    - Everything inside a function called `main()` | `def main():` 

<br/>

- **Critical Information are stored in `.env`**:
    - BANK_ADDRESS (Main Bank ETH Address)
    - BANK_PRIVATE_KEY (sign transaction from `BANK` to `PLAYER`) | (e.g. when the player win the bet)
 
    - PLAYER_ADDRESS (Player ETH Address)
    - PLAYER_PRIVATE_KEY (sign transaction from `PLAYER` to `BANK`) | (e.g. when the player bet)  

<br/>

- **Recommended Requirements**:
    - *INFURA API KEY* => https://www.infura.io/ (MUST REGISTER)
        - In `basic-casino.py` change `API_URL` = `https://goerli.infura.io/v3/<API_KEY>`.<br/>
          ⚠️ I used `Goerli` Network for Test purposes but you can choose whatever network you want ⚠️
  
  <br/>
  
    - *METAMASK WALLET* => https://metamask.io/
        - WALLET PRIVATE KEY
        - Some GOERLI ETHs (if you're using Goerli Network)
          - Mine Test ETHs => https://goerli-faucet.pk910.de/
         
  <br/>
  
    - *WEB3 Python Module*
        - `pip install web3`

  <br/>


- **EXAMPLE**:
  - Create a first wallet which is the `PLAYER WALLET` w/ metamask
  - Store its PRIVATE KEY
     
  - Create a second wallet which is the `BANK WALLET`
  - Store its PRIVATE KEY
     
  - Mine some ETHs in both wallets with the online miner ⬆️

  - In Metamask enable `Advanced network` option (in settings)
  - Select `Goerli` as current network and you'll see your withdrawn ETHs
     
  - Store ADDRESS and PRIVATE KEY of both wallets in `.env` file to their respective fields.

  
- **GUI**:
   - Soon... 💯
