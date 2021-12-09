"""Helpers for creating actions on atomictoolsx contract. By Vyryn, licenesed under AGPL."""
from aioeos import types

contract = 'atomictoolsx'


def announcelink(creator: str, key: str, asset_ids: [int], memo: str, authorization=[]) -> types.EosAction:
    return types.EosAction(
        account=contract,
        name='announcelink',
        authorization=authorization,
        data={
            'pqxra.wam': creator,
            'PUB_K1_7Hi1HpyCG6igdH2FKRCc4rLMCu6dhMkSLMegk9dwxNmzuaQjqa': key,
            '1099565564101': asset_ids,
            'memo': memo
        }
    )
