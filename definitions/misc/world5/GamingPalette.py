from definitions.master.IdleonModel import IdleonModel


class GamingPalette(IdleonModel):
	red: int
	green: int
	blue: int
	name: str
	bonusValue: int
	usesDecay: int
	levelUpBase: int
	levelUpExponent: float
	unlockChanceBase: int
	x9: int
	bonus: str
