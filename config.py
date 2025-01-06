providers = {
'Ethereum' : 'https://eth.llamarpc.com',
'BSC' : 'https://binance.llamarpc.com',
'Base' : 'https://base-rpc.publicnode.com',
'Corn' : 'https://mainnet.corn-rpc.com',
'Swell' : 'https://rpc.ankr.com/swell'
}

'''
если рпс не работают: 
https://chainlist.org/
https://account.getblock.io/sign-up
https://dashboard.alchemyapi.io/

если уверены что в какой то сети не нужно проверять баланс (там точно нет) поставьте перед ней #
это значительно ускорит работу
пример 
мне не нужна сеть корн, бск и свелл, 
providers = {
'Ethereum' : 'https://ethereum.blockpi.network/v1/rpc/public',
#'BSC' : 'https://binance.llamarpc.com',
'Base' : 'https://base-rpc.publicnode.com',
#'Corn' : 'https://mainnet.corn-rpc.com',
#'Swell' : 'https://rpc.ankr.com/swell'
}
'''
