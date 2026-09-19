from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class RoyalResource(IdleonModel):
    """Static Royal Guardian resource-node placement and capacity data.

    RoyalResources is a flat table of twenty node slots per world.  The source
    index is the node identifier used by the RoyalMaps/RoyalG arrays; ``order``
    is the slot within that world's twenty-node block.
    """

    resourceId: Integer
    world: Integer
    order: Integer
    x: Integer
    y: Integer
    capacity: Integer
    nodeType: Integer
