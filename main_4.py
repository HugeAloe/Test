import asyncio

from eth_async.client import Client
from eth_async.models import Networks, TokenAmount

from data.config import pk
from tasks.woofi import WooFi
from data.models import Contracts


async def main():
    client = Client(private_key=pk, network=Networks.Arbitrum)
    print('1')
    woofi = WooFi(client=client)
    print('2')
    eth_amount = TokenAmount(amount=0.001)
    res = await woofi.swap_eth_to_usdc(amount=eth_amount)
    print('3')
    print(res)

    # usdc_amount = TokenAmount(amount=10, decimals=6)
    # res = await woofi.swap_usdc_to_eth(amount=usdc_amount)
    # print(res)

    # arb_amount = TokenAmount(amount=2, decimals=18)
    # res = await woofi.swap_usdc_to_arb(arb_amount)
    # print(res)
    #
    # arb_amount = TokenAmount(amount=0.5 , decimals=18)

if __name__ == '__main__':
    asyncio.run(main())
