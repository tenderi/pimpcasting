# Cheatsheet

## Switching modes

| Key | Does |
|---|---|
| `F12` | `exec playing.cfg` - hero play settings |
| `F11` | `exec pimpcasting.cfg` - casting settings |
| `F10` | toggle netgraph |
| `F1` (keyboard: `Fn + ENTER`) | console |
| `Fn + ESC` | keyboard: back to L1 (typing) |

`Fn` = outer-lower thumb key (hold). The right half types normally in every layer, except the right
thumb cluster which holds the out-of-combat keys:

```
upper (inner -> outer):  F10   F11   F12   F9 broadcaster menu
lower (outer -> inner):  ->L1  Dota<->Cast  . pause  (typing)
```

## L5 Dota - hero play

```
ESC    1      2      3      4      5      F4 shop
TAB    Q      W      E      R      T      F3 courier deliver
CTRL   A      S      D      F      G      F2 courier select
SHIFT  P      J      H      V      Y
       scan   glyph  hold   movdir quickbuy

thumb upper:  ENTER  Z  X  C            chat, items 4-6
thumb lower:  Fn  PGDN  ALT  SPACE      Fn, voice PTT, alt, camera
```

- Abilities `Q W E R F G` (quickcast, `ALT+` = autocast). Items `A S D` + thumb `Z X C`. TP `5`. Neutral item `MOUSE5`.
- `T` attack, `H` hold, `V` move-direction, `B` (right hand) filter enemy.
- `1` hero, `2` all others, `3` all, `4` group 4, `TAB` cycle groups. `CTRL + n` assigns a group.
- `SPACE` tap = recent event, hold = lock camera on hero.
- `ENTER` team chat, `SHIFT+ENTER` all chat, `MOUSE4` chat wheel, `PGDN` (thumb) voice.
- Shop: `F4` open, `Y` quickbuy, in the shop `1-0` are slots and `Q W E R A S D F G H Z X C V` tabs.

### Fn held

```
->L1   6      7      8      9      0      F8 sticky buy
`      O      U      UP     ·      M      ·
·      ·      LEFT   DOWN   RIGHT  F7     ·
·      ·      ·      I      ·      ·

thumb upper:  F1 console
thumb lower:  Fn  PGUP party voice  ·  ·
```

`Fn+1-5` groups 6-10 / `Fn+Q` learn abilities / `Fn+W` learn stats / `Fn+T` move / `Fn+H` inspect / `Fn+G` scout / `Fn+TAB` scoreboard.

## L7 Cast - spectating

```
ESC    1      2      3      4      5      F4 FOW both
·      Q      W      E      R      T      F3 FOW dire
CTRL   A      S      D      F      ·      F2 FOW radiant
SHIFT  K      L      Z      -      =
       rune^  runev  LH     slower faster

thumb upper:  ENTER  F5 items  F6 gold  F7 xp
thumb lower:  Fn  F8 win%  ALT  SPACE follow hero
```

- `W A S D` camera, `MOUSE3` drag. `1` hero select, `2-5` focus player.
- `SHIFT` hold = assisted camera, `MOUSE4` toggles it. Turn it off for teamfights.
- Stat dropdown: `Q` KDA, `E` level, `R` XPM, `T` gold, `F` facet, `Z` last hits.
- `K` / `L` jump the camera to the top / bottom power rune.

### Fn held

```
->L1   6      7      8      9      0      ·
`      Y      U      I      O      ·      ·

thumb upper:  F1 console
thumb lower:  Fn  ·  ·  ·
```

`Fn+1-5` focus players 6-10 / `Fn+Q` net worth / `Fn+W` GPM / `Fn+E` buyback / `Fn+R` fantasy / `Fn+TAB` scoreboard.

## Maintenance

- Hotkeys changed in the menu: copy `~/.local/share/Steam/userdata/24132032/570/remote/cfg/dotakeys_personal.lst` here.
- Rune coordinates after a map patch: `dota_camera_get_pos` in the console, paste into `pimpcasting.cfg`.
- Layer tweaks: edit `bazecor/gen_layers.py`, run it, re-import the layer in Bazecor.
- Any convar added to one cfg must be reset in the other.
