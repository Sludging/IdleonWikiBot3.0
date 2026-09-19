from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class ExoticMarketUpgrade(IdleonModel):
    """One static row from the World 7 Exotic Market table."""

    name: str
    description: str
    cropId: Integer
    effect: Numeric
    # The source consumer branches on this flag when applying ``effect``;
    # its public display name is not stable enough to expose as a formula.
    x4: Integer
    # The source currently stores the market family here (2 for every row),
    # but no player-facing consumer gives this field a more precise meaning.
    x5: Integer
