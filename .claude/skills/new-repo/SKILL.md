---
name: new-repo
description: Create a new Repository and Model for extracting game data from the Idleon codefile. Guides through data analysis, model definition, repo implementation, section registration, and AllRepos registration.
---

# New Repository Skill

You are creating a new Repository + Model pair to extract game data from the Idleon codefile. Follow this process carefully.

## Step 1: Identify the Data Source

Ask the user what game feature they want to extract data for. Then:

1. **Find the code section** — Search the formatted codefile (`codefiles/idleon1.09.txt`) for the relevant function. Game data is stored in functions like `FeatureName = function ()` that return arrays of `.split()` strings or nested arrays.

2. **Check if a section is already registered** — Read `helpers/CodeReader.py` and look for an existing `addSection()` call that covers this data. If not found, you'll need to add one.

3. **Analyze the raw data format** — Read the relevant section from the codefile to understand:
   - Is it `.split(" ")` arrays? → use `getFromSplitArray()`
   - Is it mixed `.split()` and `[...]` arrays? → use `getFromMixedArray()`
   - Is it `],[` separated 2D arrays? → use `getFromArrayArray()`
   - What indices map to what data?

4. **Find UI/game code** — Search the codefile for how the game uses these data indices. This helps name fields properly. Look for references to the function name or array variable.

## Step 2: Create the Model

Create the model file in the appropriate `definitions/` subdirectory.

### Directory Convention
- `definitions/misc/world1/` through `definitions/misc/world7/` for world-specific features
- `definitions/misc/world5/hole/` for Hole features
- Subdirectories for grouped features (e.g., `definitions/misc/world7/spelunking/`)

### Model Template

```python
from typing import List, Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class FeatureName(IdleonModel):
    index: Integer
    name: str
    description: str
    someValue: Numeric
    someFlag: Integer
    # Name unknown fields x1, x2 etc. — rename when purpose is discovered
    x1: Integer
```

### Field Type Rules
- **`Integer`** for all integer fields (handles string-to-int conversion from parsed data)
- **`Numeric`** (`Union[Integer, float]`) for fields that could be int or float
- **`str`** for text fields
- **`Boolean`** for boolean fields (handles "1"/"0" conversion)
- **`Optional[Type]`** for fields that may not exist in all entries
- **`List[SubModel]`** for nested/related data (define sub-models in the same file)
- Always include an `index: Integer` field

### When to use `fromList()`
If the data is a flat array where field order matches model field order, the model needs NO custom code — `IdleonModel.fromList()` handles it automatically by zipping field names with the data list. This is the preferred approach for `.split()` data.

Example — `SpelunkingUpgrade` has fields in the same order as the split data, so the repo just calls `SpelunkingUpgrade.fromList(line)`.

### When NOT to use `fromList()`
If data comes from multiple arrays at different indices, or needs transformation, construct the model explicitly with keyword arguments in the repo's `generateRepo()`.

## Step 3: Create the Repository

Create the repo file in the matching `repositories/` subdirectory.

### Repository Template — Simple (fromList)

```python
from typing import List

from definitions.category.FeatureName import FeatureName
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class FeatureNameRepo(Repository[FeatureName]):
    @classmethod
    def getCategory(cls) -> str:
        return "Worlds/N"  # Determines export path: exported/repo/Worlds/N/

    @classmethod
    def getSections(cls) -> List[str]:
        return ["SectionName"]  # Must match a registered section in CodeReader

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        for line in data:
            cls.addList(FeatureName.fromList(line))
            cls.add(line[0], FeatureName.fromList(line))
```

### Repository Template — Indexed Arrays

When data is spread across multiple sub-arrays at known indices:

```python
@classmethod
def generateRepo(cls) -> None:
    data = getFromSplitArray(cls.getSection())

    names = data[0]       # First sub-array has names
    values = data[3]      # Fourth sub-array has values
    descriptions = data[7]  # etc.

    for index, name in enumerate(names):
        toAdd = FeatureName(
            index=index,
            name=name,
            value=values[index],
            description=descriptions[index],
        )
        cls.addList(toAdd)
        cls.add(toAdd.name, toAdd)
```

### Repository Template — With Dependencies

When this repo needs data from another repo:

```python
from repositories.other.OtherRepo import OtherRepo

class FeatureNameRepo(Repository[FeatureName]):
    # ... getCategory, getSections ...

    @classmethod
    def initDependencies(cls, log=True):
        OtherRepo.initialise(cls.codeReader, log)

    @classmethod
    def generateRepo(cls) -> None:
        data = getFromSplitArray(cls.getSection())
        otherItems = OtherRepo.itemsList()
        # ... use otherItems in construction ...
```

### Category Conventions
- `"Item"` — item-related repos
- `"Enemy"` — enemy-related repos
- `"Npc"` — NPC/quest repos
- `"Worlds/1"` through `"Worlds/7"` — world-specific features
- `"Worlds/5/Hole"` — Hole features
- `"Misc"` — general game features (achievements, gem shop, etc.)
- `"Dungeon"` — dungeon features
- `"Talents"` — talent trees

### Key Patterns
- Always call BOTH `cls.addList(item)` AND `cls.add(key, item)` for each entry
- Keys for `cls.add()` are typically the name/display string, or index as string
- Use `replaceUnderscores()` on display strings (converts `_` to spaces)
- Comment the index mapping when data comes from indexed arrays (e.g., `# data[6] = tunnel names`)

## Step 4: Register the Section (if needed)

If the data comes from a function not yet registered in `helpers/CodeReader.py`:

1. Open `helpers/CodeReader.py`
2. Find the appropriate world/category comment block in `readSections()`
3. Add: `self.codeReader.addSection("FunctionName = function ()", "SectionName")`

The pattern is: `addSection(start_of_function_signature, section_name)`

## Step 5: Register in AllRepos

### Single Repo
Add the import and class to `AllRepos.py`:

```python
from repositories.category.FeatureNameRepo import FeatureNameRepo

AllRepos = [..., FeatureNameRepo]
```

### Grouped Repos (multiple related repos)
Create a master file (e.g., `repositories/misc/world7/Spelunking.py`):

```python
from repositories.misc.world7.spelunking.UpgradeRepo import UpgradeRepo
from repositories.misc.world7.spelunking.ElixirRepo import ElixirRepo

FeatureRepos = [UpgradeRepo, ElixirRepo]
```

Then in `AllRepos.py`:
```python
from repositories.misc.world7.Spelunking import FeatureRepos
AllRepos = [*FeatureRepos, ...]
```

**Important**: Repos with dependencies must come AFTER their dependencies in AllRepos, OR use `initDependencies()` to ensure the dependency is initialized first. Using `initDependencies()` is preferred as it's explicit.

## Step 6: Test

Run `python -m main` from the project root and verify:
- Console shows `Generated FeatureNameRepo's repo with N Items` (green)
- No red error messages for your repo
- Check `exported/repo/{Category}/FeatureNameRepo.json` looks correct
- Check `exported/list/{Category}/FeatureNameRepo.json` if using list storage

## Helper Function Reference

| Function | Input Format | Returns |
|---|---|---|
| `getFromSplitArray(section)` | `"a b c".split(" ")` repeated | `List[List[str]]` — list of split arrays |
| `getFromMixedArray(section)` | Mix of `.split()` and `[...]` | `List[List[str]]` |
| `getFromArrayArray(section)` | `[[...],[...]]` | `List[List[str]]` |
| `getFromSplit(section)` | Single `.split()` | `List[str]` |
| `replaceUnderscores(val)` | `"Hello_World"` | `"Hello World"` |
| `formatStr(val, remove, replaceUnderscores)` | Raw string | Cleaned string |
