"""Helpers for creating actions on atomictoolsx contract. By Vyryn, licenesed under AGPL."""
from aioeos import types

contract = 'atomictoolsx'


def announcelink(creator: str, key: str, asset_ids: [int], memo: str, authorization=[]) -> types.EosAction:
    return types.EosAction(
        account=contract,
        name='announcelink',
        authorization=authorization,
        data={
            'creator': creator,
            'key': key,
            'asset_ids': asset_ids,
            'memo': memo
        }
    )
