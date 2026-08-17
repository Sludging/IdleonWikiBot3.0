# JavaScript parsing follow-up

WikiBot historically combined JavaScript parsing with export-specific normalization. The Tree-sitter migration preserves those outputs for now, but the behaviors below should be removed in a separate migration with explicit repository and export updates.

## Split delimiters are inferred instead of parsed

The legacy helpers ignore the argument passed to JavaScript `.split()` and choose between a space and semicolon by counting those characters in the source string:

```python
delimiter = " " if value.count(" ") > value.count(";") else ";"
```

This differs from JavaScript for expressions such as `"32504167".split("")`. JavaScript produces individual characters; WikiBot produces `['32504167']`.

`CosmoUpgradeRepo` depends on the WikiBot shape. It selects the first parsed value as an encoded string and indexes individual characters from that string:

```python
enhanceForColour = holeInfo[index][0]
maxEnhance = enhanceForColour[upgradeIndex]
```

Changing to JavaScript-faithful empty-string splitting makes `enhanceForColour` one character and causes `IndexError` for later upgrades. Other affected `HoleInfo` entries include compact character mappings used by Hole repositories. A follow-up should parse actual delimiters and migrate consumers to the resulting arrays.

## Literal arrays are normalized by `strToArray`

The legacy literal-array path removes braces and applies placeholder-specific comma substitutions. Direct AST literal decoding therefore changes exported text.

Known dependents and output changes:

- `ButtonTaskRepo` currently receives descriptions with the `{` substitution marker removed, such as `Level up your DRAGON Statue to at least LV` rather than `Level up your DRAGON Statue to at least LV {`.
- Equipment Set metadata passes through the same normalization. Direct AST decoding changed six sets during the prototype: `GOLD_SET`, `TROLL_SET`, `GODSHARD_SET`, `EMPEROR_SET`, `PREHISTORIC_SET`, and `SECRET_SET`.
- `HoleInfo` contains punctuation and placeholder strings whose comma/braces representation changes when decoded as JavaScript literals instead of with `strToArray`.

A follow-up should define the intended exported text for placeholders, migrate repositories that interpolate those descriptions, and then remove parsing-specific formatting from `strToArray`.

## `EquipmentSetsRepo` passes array fragments

Most helpers receive a CodeReader section containing a function body and `return [...]`. `EquipmentSetsRepo` first uses a repository-local regex to extract the text inside each assigned array, then passes that comma-separated fragment to `getFromMixedArray`.

This forces the parser to support two input contracts:

1. a function section containing a returned array;
2. an array fragment without its outer brackets.

The follow-up should investigate registering or extracting each complete Equipment Set array through CodeReader/Tree-sitter rather than repository-local regex. If complete array nodes can be supplied, `getFromMixedArray` can have one explicit input contract and remove its fragment wrapper.

## Nested arrays were grouped by textual delimiters

The legacy `getFrom4dArray` split source text on bracket substrings. In `StorageOrder`, that accidentally appended a third top-level Max Capacity group to the Storage Chest group. `StorageOrderRepo` then searched for the first entry longer than three fields to separate the groups again, even though the Max Capacity result was unused.

Tree-sitter exposes the source as three distinct arrays: inventory bags, storage chests, and maximum capacities. The migration updated `StorageOrderRepo` to consume the first two arrays directly and removed the compensating scan. Generated Storage Order and Item exports remain unchanged.

This is an example of a legacy parser bug that could be removed immediately because its only consumer could be migrated without changing the public data.

## Migration acceptance

A JavaScript-faithful follow-up should:

1. use actual `.split()` delimiters, including empty strings;
2. decode literal values without syntax-removal side effects;
3. migrate every repository relying on compact strings or stripped placeholders;
4. replace the Equipment Sets fragment extraction if complete AST nodes are available;
5. intentionally review and accept generated JSON and TypeScript changes rather than treating all output differences as regressions;
6. run full generation and focused checks for Cosmo upgrades, Button tasks, Hole data, and all Equipment Sets.
