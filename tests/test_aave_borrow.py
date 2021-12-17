from scripts.aave_borrow import (
    get_asset_price,
    getLendingPool,
    approve_erc20,
    get_account,
)
from brownie import config, network


def test_get_asset_price():
    asset_price = get_asset_price(config["networks"][network.show_active()]["dai_eth_price_feed"])
    assert asset_price > 0


def test_get_lending_pool():
    lending_pool = getLendingPool()
    assert lending_pool != None


def test_approve_erc20():
    account = get_account()
    lending_pool = getLendingPool()
    amount = 1000000000000000000  # 1
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    approved = approve_erc20(amount, lending_pool.address, erc20_address, account)
    approved.wait(1)
    assert approved is not True