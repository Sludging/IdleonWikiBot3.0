from typing import List

from definitions.misc.world5.hole.Measurement import Measurement, ItemRequirement, MeasurementType
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromMixedArray, replaceUnderscores
from repositories.master.Repository import Repository


class MeasurementRepo(Repository[Measurement]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		
		# Get measurement data from holesInfo array
		itemReqs = data[HoleOrder.MeasurementItemReqs.value]
		typeMapping = data[HoleOrder.MeasurementTypeMapping.value]
		descriptions = data[HoleOrder.MeasurementDescriptions.value]
		formulas = data[HoleOrder.MeasurementFormulas.value]
		
		# Measurement type mappings
		measurementTypeNames = {
			"0": "Gloomie Kills",
			"1": "Crops",
			"2": "Account lv",
			"3": "Tome score",
			"4": "All skill lv",
			"5": "N/A",
			"6": "Deathnote pts",
			"7": "Highest DMG",
			"8": "Slab Items",
			"9": "Studies done",
			"10": "Golem kills"
		}
		
		# Item requirement mappings based on measurement index
		sediments = [0, 2, 5, 7, 9]  # Use HoleWellFill
		notes = [1, 3, 4, 6, 8]      # Use HoleHarpNote
		rupies = [10, 11, 12, 13, 14, 15]  # Use HoleJarR
		
		# Process each measurement
		for i in range(len(itemReqs)):
			# Get item requirement name
			itemReqId = itemReqs[i]
			itemReqName = ""
			
			if i in sediments:
				itemReqName = f"HoleWellFill{int(itemReqId) + 1}"
			elif i in notes:
				itemReqName = f"HoleHarpNote{int(itemReqId) - 10}"
			elif i in rupies:
				itemReqName = f"HoleJarR{int(itemReqId) - 20}"
			else:
				itemReqName = f"Unknown{itemReqId}"
			
			# Get measurement type name
			typeId = typeMapping[i]
			typeName = measurementTypeNames.get(typeId, f"Unknown{typeId}")
			
			# Clean up description (+ remove special character)
			description = replaceUnderscores(descriptions[i])
			description = description.replace("访", "")
			
			# Determine formula type
			formula = replaceUnderscores(formulas[i])
			formulaType = "TOT" if "TOT" in formula else "REGULAR"
			
			measurement = Measurement(
				index=i,
				itemRequirement=ItemRequirement(id=itemReqId, name=itemReqName),
				measurementType=MeasurementType(type=typeId, name=typeName),
				description=description,
				formula=formula,
				formulaType=formulaType
			)
			cls.addList(measurement)
			cls.add(f"{i}", measurement) 
