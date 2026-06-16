import re
from queue import Queue
from typing import List, Set

from definitions.itemdef.Recipe import Recipe, Component, DetRecipeComponent, DetailedRecipe
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import getFrom4dArray, getFromSplitArray
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class RecipeRepo(Repository[Recipe]):
	"""
	Depends on: ItemDetailRepo
	"""
	anvilItemNames: List[List[str]]

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["AnvilItems", "Recipes", "RecipeLevel"]

	@classmethod
	def generateRepo(cls) -> None:
		reItems = r'"([a-zA-Z0-_ ]*)"\.'
		anvItemNameData = cls.getSection(0)
		cls.anvilItemNames = [x.split(" ") for x in re.findall(reItems, anvItemNameData)]

		craftNames = getFromSplitArray(cls.getSection(0))
		cls.anvilItemNames = craftNames
		componentData = getFrom4dArray(cls.getSection(1))
		levelData = getFrom4dArray(cls.getSection(2))[0]
		for i, (tabName, tabComps, tabLevel) in enumerate(zip(craftNames, componentData, levelData)):
			for j, (name, comps, level) in enumerate(zip(tabName, tabComps, tabLevel)):
				recipe = [Component(item = q, quantity = v) for q, v in comps]
				toAdd = Recipe(
					intID = name,
					recipe = recipe,
					levelReqToCraft = level[0],
					expGiven = level[1],
					no = j + 1,
					tab = i + 1
				)
				cls.add(cls.anvilItemNames[i][j], toAdd)

		for _, v in cls.items():
			cls.generateDetailedRecipe(v)
			cls.generateDetTotals(v)

	@classmethod
	def getItemAtIndex(cls, tab: int, index: int) -> str:
		return cls.anvilItemNames[tab][index]

	@classmethod
	def getFromComponent(cls, comp: Component) -> str:
		tab = int(comp.item[-1]) - 1
		index = comp.quantity
		return cls.getItemAtIndex(tab, index)

	@classmethod
	def getFromItemStr(cls, item: str, quantity: Integer) -> str:
		tab = int(item[-1]) - 1
		index = quantity
		return cls.getItemAtIndex(tab, index)

	@classmethod
	def generateDetailedRecipe(cls, recipe: Recipe):
		if recipe.detailedRecipe:
			return
		currentRecipe = []
		for component in recipe.recipe:
			currentRecipe.append(DetRecipeComponent(
				indent = 0,
				item = component.item,
				quantity = component.quantity
			))
			cRecipe = cls.get(component.item)
			if cRecipe is None or cRecipe.intID == "FillerMaterial":
				continue
			if cRecipe.detailedRecipe is None:
				cls.generateDetailedRecipe(cRecipe)
			assert cRecipe.detailedRecipe is not None
			for part in cRecipe.detailedRecipe.detRecipe:
				currentRecipe.append(DetRecipeComponent(
					indent = part.indent + 1,
					item = part.item,
					quantity = component.quantity * part.quantity
				))
		recipe.detailedRecipe = DetailedRecipe(detRecipe = currentRecipe)

	@classmethod
	def generateDetTotals(cls, recipe: Recipe):
		total = {}
		queue = Queue()
		for component in recipe.recipe:
			queue.put(component)

		while not queue.empty():
			cComponent = queue.get()
			cRecipe = cls.get(cComponent.item)
			if cRecipe is None or cRecipe.intID == "FillerMaterial":
				total[cComponent.item] = total.get(cComponent.item, 0) + cComponent.quantity
			else:
				for subComponent in cRecipe.recipe:
					queue.put(Component(
						item = subComponent.item,
						quantity = subComponent.quantity * cComponent.quantity
					))

		recipeTotals = [Component(item = i, quantity = q) for i, q in total.items()]
		recipe.detailedRecipe.detRecipeTotals = recipeTotals.copy()
		cls.calculateSellPrice(recipe)

	@classmethod
	def calculateSellPrice(cls, recipe: Recipe):
		sellPrice = 0
		for component in recipe.detailedRecipe.detRecipeTotals:
			if not ItemDetailRepo.contains(component.item):
				continue
			sellPrice += ItemDetailRepo.get(component.item).sellPrice * component.quantity
		recipe.sellPrice = sellPrice

