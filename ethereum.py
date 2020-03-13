import json
from web3 import Web3
from web3.contract import ConciseContract
def main(idf, hashipfs) :
    infura_url = "https://rinkeby.infura.io/v3/36760cff416d4607a364224ee849c779"
    web3 = Web3(Web3.HTTPProvider(infura_url))

    abi = json.loads('[{"constant": false,"inputs": [{"name": "d","type": "string"},{"name": "h","type": "string"}],"name": "addData","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function"},{"constant": true,	"inputs": [],"name": "adminAddress","outputs": [{"name": "","type": "address"			}		],		"payable": false,		"stateMutability": "view",		"type": "function"	},	{		"constant": true,		"inputs": [			{				"name": "",				"type": "uint256"			}		],		"name": "data",		"outputs": [			{				"name": "date",				"type": "string"			},			{				"name": "hash",				"type": "string"			}		],		"payable": false,		"stateMutability": "view",		"type": "function"	},	{		"constant": true,		"inputs": [			{				"name": "idf",				"type": "uint256"			}		],		"name": "getDataHash",		"outputs": [			{				"name": "",				"type": "string"			}		],		"payable": false,		"stateMutability": "view",		"type": "function"	}]')

    address = web3.toChecksumAddress("0x09755e59ab799b230a975b813b530cd99ce7490b")
    accountAddress = web3.toChecksumAddress("0xf35916267aa19bFe08f3da29f3753915a120a70F")
    contract = web3.eth.contract(address=address, abi=abi)
    privateKey = "9f9ee6a4a02e917913902b806132b98e6feba76460507afc57a0a61d9adb731b"
    hash = contract.functions.getDataHash(0).call()
    print(hash)
    print(web3.eth.accounts)
    print(idf, hashipfs)
    tx = contract.functions.addData(idf,hashipfs).buildTransaction({'nonce': web3.eth.getTransactionCount(accountAddress)})
    signed_tx = web3.eth.account.signTransaction(tx, private_key=privateKey)
    web3.eth.sendRawTransaction(signed_tx.rawTransaction)
