from brownie import network, accounts

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'hardhat','ganache-local', 'mainnet-fork', 'ganache-cli']

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]