from lesson_2_send_transactions.eth_async.models import RawContract, DefaultABIs
from lesson_2_send_transactions.eth_async.utils.utils import read_json
from lesson_2_send_transactions.eth_async.classes import Singleton

from lesson_2_send_transactions.data.config import ABIS_DIR


class Contracts(Singleton):
    # Arbitrum
    ARBITRUM_WOOFI = RawContract(
        title="WooFi",
        address='0x9aed3a8896a85fe9a8cac52c9b402d092b629a30',
        abi=read_json(path=(ABIS_DIR, 'woofi.json'))
    )

    ARBITRUM_USDC = RawContract(
        title='USDC',
        address='0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
        abi=DefaultABIs.Token
    )

    ARBITRUM_ETH = RawContract(
        title='ETH',
        address='0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        abi=DefaultABIs.Token
    )

    ARBITRUM_ARB = RawContract(
        title='ARB',
        address='0x912CE59144191C1204E64559FE8253a0e49E6548',
        abi=DefaultABIs.Token
    )

    ARBITRUM_WBTC = RawContract(
        title='WBTC',
        address='0x2f2a2543B76A4166549F7aaB2e75Bef0aefC5B0f',
        abi=DefaultABIs.Token
    )
