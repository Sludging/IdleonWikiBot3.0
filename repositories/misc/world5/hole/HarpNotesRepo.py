from typing import List

from definitions.misc.world5.hole.HarpNote import HarpNote
from repositories.master.Repository import Repository


class HarpNotesRepo(Repository[HarpNote]):
	"""
	Repository for extracting Harp Notes data
	"""
	
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"
	
	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]
	
	@classmethod
	def generateRepo(cls) -> None:
		# Note names from the wiki (hardcoded)
		noteNames = [
			"Crotchet Note",
			"Natural Note", 
			"Bass Note",
			"Treble Note",
			"Eighth Note",
			"Quaver Note",
			"Sharp Note",
			"(F)Clef Note",
			"(G)Clef Note",
			"Sixteenth Note"
		]
		
		# Extract note configuration data
		for i in range(10):
			harpNote = HarpNote(
				noteId=i,
				noteName=noteNames[i]
			)
			
			cls.addList(harpNote)
			cls.add(harpNote.noteId, harpNote)
            