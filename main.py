import asyncio
import csv
from web3 import AsyncWeb3
from aiohttp import ClientSession
from config import providers
from utils.utils import load_json, CustomAsyncHTTPProvider, hels, get_token_balance


async def main():
    print(hels.__call__())
    token_abi = await load_json('data/abi.json')
    tokens = await load_json('data/tokens.json')

    with open('addresses.txt', 'r') as f:
        addresses = f.read().splitlines()

    output_rows = []  # Список для сохранения результатов
    token_names = []  # Список для хранения названий токенов (для заголовков CSV)

    async with ClientSession() as session:
        for address in addresses:
            row = {"Address": address}  # Начало строки для этого адреса
            for chain in tokens:
                chain_name = chain['chain']
                provider_url = providers.get(chain_name)

                if not provider_url:
                    print(f"Provider for {chain_name} not found.")
                    continue

                custom_provider = CustomAsyncHTTPProvider(provider_url, session)
                web3 = AsyncWeb3(custom_provider)
                for token in chain['tokens']:
                    token_name = token['token_name']
                    token_address = token['address']

                    # Создание уникального названия для токена с учетом сети
                    unique_token_name = f"{chain_name}_{token_name}"

                    # Добавляем уникальное название токена в заголовок, если его еще нет
                    if unique_token_name not in token_names:
                        token_names.append(unique_token_name)

                    # Получение баланса токена
                    balance = await get_token_balance(web3, token_address, address, token_abi)
                    print(f"{address} | {chain_name} {token_name} | {balance}")

                    # Добавляем баланс в строку для этого адреса
                    row[unique_token_name] = balance

            output_rows.append(row)
            print()

    # Добавление заголовков в CSV (названия токенов в первом ряду)
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["Address"] + token_names  # "Address" + список токенов
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(output_rows)

    print("Results have been saved to 'output.csv'.")


# Запуск асинхронного процесса
if __name__ == "__main__":
    asyncio.run(main())
