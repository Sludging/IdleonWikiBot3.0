# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

IdleonWikiBot3.0 is a Python data extraction tool for the idle game "Idleon". It parses the game's JavaScript code file (N.js), extracts structured game data via regex-based section extraction, validates it through Pydantic models, and exports to JSON and TypeScript for the IdleonEfficiency website. (available locally at ../IdleonEfficiency)

## Commands

```bash
# Pre-parse game code (after placing N.js in root, update ver in pre_parsing.py)
python pre_parsing.py          # Formats N.js → codefiles/idleon{ver}.txt (requires npx prettier)

# Run all repositories and export data
python -m main                 # Outputs to exported/repo/, exported/list/, exported/ts/

# Install dependencies
pip install -r requirements.txt
```

There are no test or lint commands configured.

## Architecture

### Data Flow

`N.js` → `pre_parsing.py` (cleanup + prettier) → `codefiles/idleon{ver}.txt` → `IdleonReader` (regex section extraction) → `Repository.generateRepo()` (parse sections into models) → JSON + TypeScript exports in `exported/`

### Core Abstractions

- **`IdleonModel`** (`definitions/master/IdleonModel.py`): Pydantic v1 BaseModel with TypeScript interface generation, comparison utilities, and wiki export support. All game data models inherit from this.

- **`Repository[T]`** (`repositories/master/Repository.py`): Generic base class for all repositories. Uses class-level state (not instances). Key methods: `getSections()` returns regex keys, `getCategory()` returns export folder, `generateRepo()` contains parsing logic, `initDependencies()` initializes prerequisite repos.

- **`CodeReader`** (`helpers/CodeReader.py`): Extracts named code sections from the formatted game file using regex patterns. `IdleonReader` subclass registers all ~100 section patterns and calls `readCode()` to extract them in one pass.

### Model-Repository Pattern

Every game data type follows the same pattern:
1. A **Model** in `definitions/` — Pydantic class defining the data structure
2. A **Repository** in `repositories/` — Parses code sections and builds model instances
3. Registration in `AllRepos.py` — list that `main.py` iterates to initialize all repos

Repositories use `add(key, model)` for dict-based storage and `addList(model)` for list-based storage. Export produces both `exported/repo/` (dict) and `exported/list/` (list) JSON files, plus TypeScript in `exported/ts/`.

### Adding a New Repository

Use the `/new-repo` skill for guided repository creation with examples and best practices.

### Key Helpers

- `helpers/HelperFunctions.py`: String/array parsing (`getFromSplit`, `strToArray`, `formatStr`, `replaceUnderscores`)
- `helpers/Constants.py`: Game constants (world names, skill names, map lookups)
- `helpers/JsonEncoder.py`: `CompactJSONEncoder` for readable JSON output

## Dependencies

Python 3 with Pydantic v1 (`pydantic==1.10.19`). Also requires Node.js/npx for prettier (used in pre-parsing step).
