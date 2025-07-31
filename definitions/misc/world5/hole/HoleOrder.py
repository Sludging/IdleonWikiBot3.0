from enum import Enum


class HoleOrder(Enum):
	BuildingOrder = 40
	JusticeCases = 62
	PersonNames = 63
	Amplifiers = 28
	# Measurement System
	MeasurementItemReqs = 50
	MeasurementTypeMapping = 52
	MeasurementDescriptions = 54
	MeasurementFormulas = 55
	# Study System
	StudyNames = 68
	StudyDescriptions = 69
	StudyMultipliers = 70
	# Bell Improvement  
	BellImprovementCosts = 42
	BellImprovementCharges = 60
	# Bell Bonus
	BellBonusTypes = 59
	# Harp System
	HarpStringDescriptions = 45  # Descriptions for the 7 harp strings
	# Gambit System
	GambitConfig = 71
	# Monument System
	MonumentUnlockHours = 30    # Hours required for unlocks
	MonumentUnlockRewards = 31  # Unlock reward descriptions  
	MonumentBonuses = 32        # Monument bonus descriptions
