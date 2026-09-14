# pimpcasting (tenderi's fork)

Dota 2 config files for two modes of use on one client: **playing a hero** and **casting / observing**.
Forked from [JJLiebig/pimpcasting](https://github.com/JJLiebig/pimpcasting) (0.7.1, 2020) and rewritten
in September 2026 against the current client. Every command in the cfg files was checked against the
installed game binary; cheat-protected commands and dead aliases were removed.

## Files

| File | Purpose |
|---|---|
| `autoexec.cfg` | Runs at launch. Binds `F12` (playing) / `F11` (casting) / `F10` (netgraph toggle), drops the plain console bind, loads `playing.cfg`. |
| `playing.cfg` | Hero gameplay state: camera, minimap, quickcast, unit control, shop/courier, HUD. Resets **every** convar that `pimpcasting.cfg` touches. |
| `pimpcasting.cfg` | Casting state: slow smooth camera, free zoom, assisted camera on `SHIFT`/`MOUSE4`, hold `SPACE` to follow a hero, broadcaster HUD, rune camera jumps on `k`/`l`. |
| `dotakeys_personal.lst` | Snapshot of the in-game Hotkeys profile ("ARROW"). Abilities, items and spectator keys live here, not in the cfg files. |
| `benchmark.cfg` | Original FPS benchmark script (needs replay 3061101068 downloaded). Untouched. |
| `binds.png` | Original author's recommended spectator hotkeys. The ARROW profile already uses them. |

## Install (Linux / Steam)

The cfg files are symlinked into the game so this repo stays the single source of truth:

```
DCFG="$HOME/.local/share/Steam/steamapps/common/dota 2 beta/game/dota/cfg"
for f in autoexec.cfg playing.cfg pimpcasting.cfg; do ln -sfn "$PWD/$f" "$DCFG/$f"; done
```

`dotakeys_personal.lst` is **not** symlinked. The live copy is
`~/.local/share/Steam/userdata/<steamid>/570/remote/cfg/dotakeys_personal.lst` (Steam Cloud synced).
Copy it here after changing hotkeys in the menu to keep the snapshot current.

Disable or move the Steam overlay screenshot key (default `F12`), otherwise it fires together with the config swap.

## Usage

- `F12` loads `playing.cfg`, `F11` loads `pimpcasting.cfg`. The console prints which one ran.
- `F10` toggles the netgraph in both modes.
- Console is `ALT` + the key at the US-backslash position (`'` on a Nordic layout). The plain key is unbound so it can no longer open while typing in chat.

### The mirror rule

`playing.cfg` and `pimpcasting.cfg` are mirrors. Any convar or bind added to one **must** be reset in the
other, otherwise switching with `F11`/`F12` leaks settings between modes (and Dota persists most convars,
so a leaked value survives a restart).

### Rune camera jumps

`pimpcasting.cfg` binds `k` / `l` to the power rune spots using 7.33+ map coordinates. After a map patch,
stand the camera on the rune, run `dota_camera_get_pos` in the console and paste the new numbers.
The same spots are also stored as saved camera positions 1 and 2 in the client settings.

## Casting with the assisted camera

(From the original readme, still accurate.)

Valve's "Assisted Camera" is a bit like the directed camera in DotaTV and follows heroes around
without you controlling it. Load into a game in DotaTV, press `F11` after the draft, click on a lane,
move to a hero and press `MOUSE4` (`dota_toggle_assisted_camera_operator`). Adjust with `W` `A` `S` `D`;
the middle mouse button does not work while it is on.

Do **not** use it in teamfights or when framing ganks: turn it off and drag with `MOUSE3`.

```
                              Is there a teamfight?
                              /                   \
                             /                     \
                            No                     Yes
                            |                        \
              Is a lot happening regardless?      Turn assisted cam off
                  /                   \             Use Mouse 3 drag
                 No                   Yes
                 |                     |
       Keep assisted cam on    Turn assisted cam off
         Adjust with WASD         Use Mouse 3 drag
```

Do you use WASD to move the camera without assisted cam? Don't. It looks bad. Smooth drag via `MOUSE3`
is by far the most precise camera.

### Tips

- Clicking the minimap without assisted camera: hold `SHIFT` until the movement completes for a smooth transition.
- LAN / on-stage: uncomment `dota_silent_roshan 1` in `pimpcasting.cfg` to mute Roshan and smoke sounds.
- Zoom per mousewheel notch feels wrong: raise `dota_camera_broadcaster_mousewheel_direction_multiplier` and
  `dota_camera_mousewheel_direction_multiplier` (0.0075 is a good second try).
- Minimap icon sizes: `dota_minimap_hero_size` / `dota_minimap_rune_size`.
- Minimap icons scaling with zoom: `dota_minimap_hero_scalar`, `_distance`, `_minimum`; set `dota_minimap_hero_scalar 0` to disable.

## Credits

Original config and casting advice by Jonathan "PimpmuckL" Liebig.
