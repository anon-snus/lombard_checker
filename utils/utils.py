import json
from web3.providers.async_base import AsyncBaseProvider
from decimal import Decimal
import asyncio

class CustomAsyncHTTPProvider(AsyncBaseProvider):
    def __init__(self, rpc_url, session):
        self.rpc_url = rpc_url
        self.session = session

    async def make_request(self, method, params):
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }
        async with self.session.post(self.rpc_url, json=payload) as response:
            if response.status != 200:
                raise Exception(f"RPC request failed with status code {response.status}")
            return await response.json()

async def load_json(filepath):

    with open(filepath, 'r') as file:
        return json.load(file)

async def get_token_balance(web3, token_address, user_address, abi):
    for i in range(5):  # Попытки в случае ошибки
        try:
            contract = web3.eth.contract(address=web3.to_checksum_address(token_address), abi=abi)
            balance = await contract.functions.balanceOf(web3.to_checksum_address(user_address)).call()
            decimals = await contract.functions.decimals().call()
            return Decimal(balance) / Decimal(10 ** decimals)
        except Exception:
            await asyncio.sleep(0.01)
    return 'rpc does not work'

def hels():
    return f'Subscribe to https://t.me/degen_statistics 🤫'