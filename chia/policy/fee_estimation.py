from dataclasses import dataclass
from datetime import datetime

from chia.util.ints import uint64, uint32


@dataclass(frozen=True)
class FeeMempoolInfo:
    """
    Information from Mempool and MempoolItems needed to estimate fees.

    Attributes:
        current_mempool_cost (uint64):This is the current capacity of the mempool, measured in XCH per CLVM Cost
        max_size_in_cost (uint64): This is the maximum capacity of the mempool, measured in XCH per CLVM Cost
        minimum_fee_per_cost_to_replace (uint64): Smallest FPC that  might be accepted to replace another SpendBundle
        time (datetime): Local time this sample was taken

        Note the reasons we do not use "Blockchain time" for the timestamp above
    """

    max_size_in_cost: uint64  # Mempool max allowed CLVM cost total
    minimum_fee_per_cost_to_replace: uint64
    current_mempool_cost: uint64  # Current sum of CLVM cost of all SpendBundles in mempool (mempool "size")
    time: datetime  # Local time this sample was taken
    MAX_BLOCK_COST_CLVM: uint64  # xxx move to config?


@dataclass(frozen=True)
class FeeMempoolItem:
    height_added: uint32
    fee_per_cost: uint64


class FeeBlockInfo: # See BlockRecord
    """
    Information from Blockchain needed to estimate fees.
    """

    block_height: uint32
    pass


class FeeRate:
    """
    Represents Fee in XCH per CLVM Cost. Performs XCH/mojo conversion
    """

    pass
