# Sushi Station unlock bonuses — game 1.19

This producer supplies the static values read by the delivered game's
`SushiStuff("RoG_BonusQTY", index, 0)` branch.

## Accepted source and baseline

- Game version: `1.19` (`Summer_Event`)
- Parsed source: `codefiles/idleon1.19.txt`
- Source revision: `f5953a3b` (`add 1.19 codefile`)
- Static source function: `scripts.CustomLists` → `Research = function ()`, row `37`
- Formula source: `_customBlock_SushiStuff`, `RoG_BonusQTY` branch
- Accepted save SHA-256: `627b1eda758bab2749802b5ee373a2b7da3e6b2e3505647b0affe5c0686323c7`
- Accepted live-result manifest SHA-256: `fcdd321877cab4a0e7f36abf36142fa7cfa755bfe35118e61b609a0892ebf345`

`Research[37]` is static game data. It is not the player's saved
`Research` field.

## Produced data

`SushiUnlockBonusRepo` exports every value in the 59-entry static row, keyed
and listed by the internal zero-based index.

The generated producer files are:

- `exported/repo/Worlds/7/SushiUnlockBonusRepo.json`
- `exported/list/Worlds/7/SushiUnlockBonusRepo.json`
- `exported/ts/data/SushiUnlockBonusRepo.ts`
- `exported/ts/model/sushiUnlockBonusModel.ts`

The formula is recorded at `codefiles/idleon1.19.txt:240725`; the static
`Research` function begins at `codefiles/idleon1.19.txt:302522`.

The requested caller indices are:

| Internal index | Static unlock-bonus value |
| ---: | ---: |
| 23 | 1 |
| 26 | 25 |
| 41 | 100 |
| 44 | 50 |
| 50 | 10 |
| 51 | 10 |

Generated consumers should use the internal index directly. This delivery
does not assert a mapping from an internal index to a player-facing Sushi tier.

## Limitations

- This producer supplies static `Research[37]` values only.
- It does not parse saved `Sushi[5]` or implement `UniqueSushi()`.
- It does not implement the unlock gate (`UniqueSushi() > index`) or the
  caller-index `99` bypass; those remain consumer-domain behavior.
- It does not provide root-specific live extraction evidence. The consumer
  must validate the formula, save gate, caller indices, and all supplied values
  against the accepted baseline before enabling the correctness case.
- Wiki descriptions are terminology context, not evidence for internal index
  mappings.
