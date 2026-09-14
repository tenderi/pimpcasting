# Dygma Defy layers for Dota 2

Four Bazecor layers, all driven with the **left hand only** so the right hand never leaves the mouse.
The layers emit exactly the keys the in-game Hotkeys profile ("ARROW", `../dotakeys_personal.lst`)
already expects, so no hotkey had to change in Dota - the right half of the keyboard just became
unnecessary. Right-hand keys are transparent (fall through to L1 for typing in chat).

| File | Layer | Purpose |
|---|---|---|
| `layer5-dota.json` | L5 "Dota" | Hero play |
| `layer6-dotafn.json` | L6 "DotaFn" | Rare play actions, held via the outer-lower thumb key |
| `layer7-cast.json` | L7 "Cast" | Spectating / casting |
| `layer8-castfn.json` | L8 "CastFn" | Rare casting actions, held via the outer-lower thumb key |

`gen_layers.py` generates the files; edit the dictionaries there rather than the JSON.
`original-dota-export.json` is the pre-redesign export of the Dota layer (palette and underglow are taken from it).

## Import

In Bazecor: Layout Editor -> select the target layer (L5 first) -> layer menu -> **Import** -> pick the
file. The import renames the layer and replaces its keys and colours. Repeat for L6, L7, L8, then
**Save** to the keyboard. The palette is not imported; the files use the palette already on the neuron.
Getting into L5 from L1 is whatever key you already use; leaving is `Fn + ESC` or the right thumb key.

## L5 Dota - hero play

```
ESC    1      2      3      4      5      F4(shop)
TAB    Q      W      E      R      T      F3(courier deliver)
CTRL   A      S      D      F      G      F2(courier select)
SHIFT  P      J      H      V      Y
       scan   glyph  hold   movedir quickbuy

thumb upper (outer -> inner):  ENTER   Z      X      C        chat, items 4-6
thumb lower (outer -> inner):  Fn      PGDN   ALT    SPACE    Fn, voice PTT, alt, camera
```

Colours: blue abilities, green items, cyan TP, red attack/hold/move-direction, amber select/control
groups, magenta scan/glyph, white shop/courier/quickbuy, sky camera/chat/voice, purple layer keys.
Modifiers and the right hand stay dark. Underglow tells the active layer apart: amber = Dota,
sky = Cast, purple = an Fn layer is held. Fn layers light only the keys that do something.

What changed against the old layer:
- `H` hold, `J` glyph, `P` scan moved onto the bottom row (they were right-hand only).
- The big inner thumb key is `SPACE` (tap = recent event, hold = camera lock); `V` move-direction
  went to its normal bottom-row spot. The duplicate `SPACE` became `ENTER` so chat can be opened left-handed.
- Voice push-to-talk is a thumb key (`PGDN`, the profile's Voice key).
- Dead `F16-F18`/`F24` placeholders are gone; the inner column is a shop/courier column.

## L6 DotaFn - hold the outer-lower thumb key

```
LOCK L1  6     7     8      9     0     F8(sticky buy)
`        O     U     UP     F10   M     F11(cast cfg)
LOCK L7  ·     LEFT  DOWN   RIGHT F7    F12(play cfg)
·        ·     ·     I      ·     ·
scoreboard / learn abilities / learn stats / camera ESDF / netgraph / move / inspect / scout

thumb upper:  ALT+\ (console)   ·   ·   ·
thumb lower:  Fn    PGUP(party voice)   ·   .(pause)
```

`Fn + 1-5` = control groups 6-10. `Fn + CTRL` locks to the Cast layer, `Fn + ESC` back to L1.

## L7 Cast - spectating

```
ESC    1      2      3      4      5      F4(FOW both)
TAB    Q      W      E      R      T      F3(FOW dire)
CTRL   A      S      D      F      G      F2(FOW radiant)
SHIFT  K      L      Z      -      =
       rune↑  rune↓  LH     slower faster (replay)

thumb upper:  ENTER   F5(items)  F6(gold)  F7(xp)
thumb lower:  Fn      F8(win%)   ALT       SPACE(follow hero)
```

`1` = hero select, `2-5` = focus player, `WASD` = camera, `Q E R T F Z` = stat dropdowns,
`SHIFT` held = assisted camera (from `pimpcasting.cfg`), `k`/`l` = rune camera jumps.

## L8 CastFn - hold the outer-lower thumb key

```
LOCK L1  6     7     8      9     0     F9(broadcaster menu)
`        Y     U     I      O     F10   F11(cast cfg)
LOCK L5  ·     ·     ·      ·     ·     F12(play cfg)
scoreboard / networth / gpm / buyback / fantasy / netgraph

thumb upper:  ALT+\ (console)   ·   ·   ·
thumb lower:  Fn    ·   ·   .(pause)
```

`Fn + 1-5` = focus players 6-10. `Fn + CTRL` locks back to the Dota layer.

## Key index reference

Bazecor keymap index = `16 * row + col`; left hand is cols 0-6 (row 3: 0-5), thumb row 4.
Left thumb: upper arc `64 65 66 67`, lower arc `71 70 69 68`, outer to inner; 68 is the big key.
Codes: Layer Shift N = `17449+N`, Layer Lock N = `17491+N`, `Ctrl +256`, `Alt +512`, `Shift +2048`,
No Key `0`, Transparent `65535`.
