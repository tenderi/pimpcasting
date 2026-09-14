#!/usr/bin/env python3
"""Generate Bazecor layer files for the Dygma Defy: Dota (play), DotaFn, Cast, CastFn.

Keymap index = 16*row + col. Left hand = cols 0-7, right hand = cols 8-15, row 4 = thumb clusters.
Left thumb, outer -> inner: upper arc 64 65 66 67, lower arc 71 70 69 68 (68 is the big inner key).
Layer indices: 4 Dota, 5 DotaFn, 6 Cast, 7 CastFn (Bazecor shows them 1-based: L5..L8).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = json.loads((HERE / "original-dota-export.json").read_text())

# Bazecor re-parses a key from keyCode when extraLabel is an object, so labels are display-only here.
TRANS = {"keyCode": 65535, "label": "TRANS", "extraLabel": {}}
NOKEY = {"keyCode": 0, "label": "NO KEY", "extraLabel": {}}

CTRL, ALT, SHIFT = 256, 512, 2048
HID = {
    "A": 4, "B": 5, "C": 6, "D": 7, "E": 8, "F": 9, "G": 10, "H": 11, "I": 12, "J": 13, "K": 14, "L": 15,
    "M": 16, "N": 17, "O": 18, "P": 19, "Q": 20, "R": 21, "S": 22, "T": 23, "U": 24, "V": 25, "W": 26,
    "X": 27, "Y": 28, "Z": 29, "1": 30, "2": 31, "3": 32, "4": 33, "5": 34, "6": 35, "7": 36, "8": 37,
    "9": 38, "0": 39, "ENTER": 40, "ESC": 41, "TAB": 43, "SPACE": 44, "-": 45, "=": 46, "\\": 49,
    "`": 53, ".": 55, "F1": 58, "F2": 59, "F3": 60, "F4": 61, "F5": 62, "F6": 63, "F7": 64, "F8": 65,
    "F9": 66, "F10": 67, "F11": 68, "F12": 69, "PGUP": 75, "PGDN": 78, "RIGHT": 79, "LEFT": 80,
    "DOWN": 81, "UP": 82, "LCTRL": 224, "LSHIFT": 225, "LALT": 226,
}

def key(name):
    if name == "TRANS":
        return dict(TRANS)
    if name == "NOKEY":
        return dict(NOKEY)
    if name.startswith("LOCK L"):      # LOCK L1 .. L10
        return {"keyCode": 17491 + int(name[6:]), "label": name, "extraLabel": {}}
    if name.startswith("SHIFT L"):     # SHIFT L1 .. L10 (hold)
        return {"keyCode": 17449 + int(name[7:]), "label": name, "extraLabel": {}}
    if name.startswith("ALT+"):
        return {"keyCode": HID[name[4:]] + ALT, "label": name, "extraLabel": {}}
    return {"keyCode": HID[name], "label": name, "extraLabel": {}}

# Palette indices from the existing Dota.json palette
AMBER, GREEN, WHITE, LIME, CYAN, BLUE, MAGENTA, SKY, PURPLE, LILAC, RED, OFF = 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 15

def layer(name, left, colors, glow, right=None):
    """left/right: {index: keyname}. Unset keys are transparent. glow = underglow + neuron colour."""
    keymap = [dict(TRANS) for _ in range(80)]
    colormap = [OFF] * 80 + [glow] * (len(BASE["colormap"]) - 80)
    for idx, k in {**left, **(right or {})}.items():
        keymap[idx] = key(k)
    for idx, c in colors.items():
        colormap[idx] = c
    return {
        "device": BASE["device"],
        "language": "en-US",
        "layerNames": [],
        "layerName": name,
        "keymap": keymap,
        "colormap": colormap,
        "palette": BASE["palette"],
    }

#################################################################################################
# Layer 5 "Dota" - hero play, left hand only. Emits the keys the ARROW hotkey profile expects.
#################################################################################################
dota_left = {
    0: "ESC",   1: "1", 2: "2", 3: "3", 4: "4", 5: "5",            6: "F4",     # shop
    16: "TAB",  17: "Q", 18: "W", 19: "E", 20: "R", 21: "T",       22: "F3",    # courier deliver
    32: "LCTRL", 33: "A", 34: "S", 35: "D", 36: "F", 37: "G",     38: "F2",    # courier select
    48: "LSHIFT", 49: "P", 50: "J", 51: "H", 52: "V", 53: "Y",                 # scan glyph hold movedir quickbuy
    64: "ENTER", 65: "Z", 66: "X", 67: "C",                                    # chat, items 4-6
    71: "SHIFT L6", 70: "PGDN", 69: "LALT", 68: "SPACE",                       # Fn, voice, alt, camera
}
# Right thumb (76-79 upper inner->outer, 72-75 lower outer->inner; 75 stays transparent for typing)
RIGHT_COMMON = {76: "F10", 77: "F11", 78: "F12", 79: "F9", 72: "LOCK L1", 74: "."}
RIGHT_COLORS = {76: SKY, 77: SKY, 78: SKY, 79: SKY, 72: PURPLE, 73: PURPLE, 74: MAGENTA}
MODS = {0: LILAC, 32: LILAC, 48: LILAC, 69: LILAC}                          # esc, ctrl, shift, alt

dota_right = {**RIGHT_COMMON, 73: "LOCK L7"}
dota_colors = {
    17: BLUE, 18: BLUE, 19: BLUE, 20: BLUE, 36: BLUE, 37: BLUE,            # abilities
    33: GREEN, 34: GREEN, 35: GREEN, 65: GREEN, 66: GREEN, 67: GREEN,      # items
    5: CYAN,                                                               # TP
    21: RED, 51: RED, 52: RED,                                             # attack, hold, move direction
    1: AMBER, 2: AMBER, 3: AMBER, 4: AMBER, 16: AMBER,                     # select / control groups
    49: MAGENTA, 50: MAGENTA,                                              # scan, glyph
    6: WHITE, 22: WHITE, 38: WHITE, 53: WHITE,                             # shop, courier, quickbuy
    68: SKY, 64: SKY, 70: SKY,                                             # camera, chat, voice
    71: PURPLE, **MODS, **RIGHT_COLORS,                                    # layer keys, mods, right thumb
}

#################################################################################################
# Layer 6 "DotaFn" - held via thumb 71 on top of Dota. Only overrides are defined.
#################################################################################################
dotafn_left = {
    0: "LOCK L1", 1: "6", 2: "7", 3: "8", 4: "9", 5: "0",         6: "F8",     # leave, groups 6-10, sticky buy
    16: "`", 17: "O", 18: "U", 19: "UP", 21: "M",                              # scoreboard, learn, stats, cam, move
    34: "LEFT", 35: "DOWN", 36: "RIGHT", 37: "F7",                             # cam, scout
    51: "I",                                                                   # inspect hero
    64: "F1", 70: "PGUP",                                                      # console, party voice
}
dotafn_colors = {
    1: AMBER, 2: AMBER, 3: AMBER, 4: AMBER, 5: AMBER,                      # groups 6-10
    19: WHITE, 34: WHITE, 35: WHITE, 36: WHITE,                            # camera
    17: BLUE, 18: BLUE, 51: BLUE,                                          # learn abilities / stats, inspect
    21: RED, 37: RED,                                                      # move, scout
    6: WHITE, 16: SKY,                                                     # sticky buy, scoreboard
    64: SKY, 70: SKY,                                                      # console, party voice
    0: PURPLE, 71: PURPLE,                                                 # layer keys
}

#################################################################################################
# Layer 7 "Cast" - spectating. Spectator hotkeys from the ARROW profile + pimpcasting.cfg binds.
#################################################################################################
cast_left = {
    0: "ESC",   1: "1", 2: "2", 3: "3", 4: "4", 5: "5",            6: "F4",     # hero select, players 2-5, FOW both
    17: "Q", 18: "W", 19: "E", 20: "R", 21: "T",                  22: "F3",    # KDA, cam up, level, xpm, gold, FOW dire
    32: "LCTRL", 33: "A", 34: "S", 35: "D", 36: "F",              38: "F2",    # cam left/down/right, facet, FOW radiant
    48: "LSHIFT", 49: "K", 50: "L", 51: "Z", 52: "-", 53: "=",                 # assisted cam, rune top/bot, LH, replay speed
    64: "ENTER", 65: "F5", 66: "F6", 67: "F7",                                 # chat, item stats, gold graph, xp graph
    71: "SHIFT L8", 70: "F8", 69: "LALT", 68: "SPACE",                         # Fn, win chance, alt, follow hero
}
cast_right = {**RIGHT_COMMON, 73: "LOCK L5"}
cast_colors = {
    18: WHITE, 33: WHITE, 34: WHITE, 35: WHITE, 68: WHITE,                 # camera
    1: AMBER, 2: AMBER, 3: AMBER, 4: AMBER, 5: AMBER,                      # hero / player focus
    6: MAGENTA, 22: MAGENTA, 38: MAGENTA,                                  # FOW
    17: BLUE, 19: BLUE, 20: BLUE, 21: BLUE, 36: BLUE, 51: BLUE,            # stat dropdowns
    65: CYAN, 66: CYAN, 67: CYAN, 70: CYAN,                                # graphs
    49: GREEN, 50: GREEN, 52: LIME, 53: LIME,                              # rune jumps, replay speed
    48: RED, 64: SKY,                                                      # assisted camera, chat
    71: PURPLE, **MODS, **RIGHT_COLORS,                                    # layer keys, mods, right thumb
}

#################################################################################################
# Layer 8 "CastFn" - held via thumb 71 on top of Cast.
#################################################################################################
castfn_left = {
    0: "LOCK L1", 1: "6", 2: "7", 3: "8", 4: "9", 5: "0",                      # leave, players 6-10
    16: "`", 17: "Y", 18: "U", 19: "I", 20: "O",                               # scoreboard, networth, gpm, buyback, fantasy
    64: "F1",                                                                  # console
}
castfn_colors = {
    1: AMBER, 2: AMBER, 3: AMBER, 4: AMBER, 5: AMBER,                      # players 6-10
    17: BLUE, 18: BLUE, 19: BLUE, 20: BLUE,                                # stat dropdowns
    6: MAGENTA, 16: SKY, 21: SKY, 22: SKY, 38: SKY,                        # broadcaster menu, scoreboard, netgraph, cfgs
    64: SKY, 68: MAGENTA,                                                  # console, pause
    0: PURPLE, 32: PURPLE, 71: PURPLE,                                     # layer keys
}

LAYERS = [
    ("layer5-dota.json",   layer("Dota",   dota_left,   dota_colors,   AMBER,  dota_right)),
    ("layer6-dotafn.json", layer("DotaFn", dotafn_left, dotafn_colors, PURPLE)),
    ("layer7-cast.json",   layer("Cast",   cast_left,   cast_colors,   SKY,    cast_right)),
    ("layer8-castfn.json", layer("CastFn", castfn_left, castfn_colors, PURPLE)),
]

if __name__ == "__main__":
    for fn, data in LAYERS:
        (HERE / fn).write_text(json.dumps(data, indent=2) + "\n")
        print("wrote", fn)
