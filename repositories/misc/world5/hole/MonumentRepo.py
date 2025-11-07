from typing import List

from definitions.misc.world5.hole.Monument import Monument, MonumentUnlock, MonumentBonus
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class MonumentRepo(Repository[Monument]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get monument data from holesInfo array (indices 30, 31, 32)
		unlock_hours = data[HoleOrder.MonumentUnlockHours.value]
		unlock_rewards = data[HoleOrder.MonumentUnlockRewards.value] 
		bonus_descriptions = data[HoleOrder.MonumentBonuses.value]
		bonus_multipliers = data[HoleOrder.MonumentBonusMultipliers.value]
		
		# Monument names in order
		monument_names = ["Bravery", "Justice", "Wisdom"]
		
		# Each monument has 8 unlocks and 10 bonuses
		# Data is organized sequentially: first N for bravery, next N for justice, last N for wisdom
		unlocks_per_monument = 8
		bonuses_per_monument = 10
		
		# Process each monument
		for monument_index, monument_name in enumerate(monument_names):
			# Calculate data slice indices for this monument
			unlock_start_idx = monument_index * unlocks_per_monument
			unlock_end_idx = unlock_start_idx + unlocks_per_monument
			
			bonus_start_idx = monument_index * bonuses_per_monument  
			bonus_end_idx = bonus_start_idx + bonuses_per_monument
			
			# Extract data slices for this monument
			# Hours are shared across all monuments (same 8 values for each)
			monument_unlock_hours = unlock_hours[:unlocks_per_monument] if unlock_hours else []
			monument_unlock_rewards = unlock_rewards[unlock_start_idx:unlock_end_idx] if unlock_rewards else []
			monument_bonus_descriptions = bonus_descriptions[bonus_start_idx:bonus_end_idx] if bonus_descriptions else []
			monument_bonus_multipliers = bonus_multipliers[bonus_start_idx:bonus_end_idx] if bonus_multipliers else []

			# Create unlocks (8 per monument)
			unlocks = []
			for i in range(8):
				unlock = MonumentUnlock(
					index=i,
					description=replaceUnderscores(monument_unlock_rewards[i]) if i < len(monument_unlock_rewards) else "",
					hours_required=float(monument_unlock_hours[i]) if i < len(monument_unlock_hours) and monument_unlock_hours[i] else 0
				)
				unlocks.append(unlock)
			
			# Create bonuses (10 per monument)  
			bonuses = []
			for i in range(10):
				bonus = MonumentBonus(
					index=i,
					description=replaceUnderscores(monument_bonus_descriptions[i]) if i < len(monument_bonus_descriptions) else "",
					multiplier=float(monument_bonus_multipliers[i]) if i < len(monument_bonus_multipliers) and monument_bonus_multipliers[i] else 0
				)
				bonuses.append(bonus)
			
			# Create monument object
			monument = Monument(
				index=monument_index,
				name=monument_name,
				unlocks=unlocks,
				bonuses=bonuses
			)
			
			# Add to repository
			cls.addList(monument)
			cls.add(monument_name.lower(), monument) 
