# brawlcrate-plugins

BrawlCrate loaders (IronPython, BrawlAPI) by Chris Varanese for porting Brawl / Project+ fighters to other games
(made for a Rivals of Aether 2 port of P+ Captain Falcon). Each adds a right-click menu item in BrawlCrate.

If these loaders are useful to you, a ⭐ on the repo helps other modders find them.

| Loader | Right-click on | Menu item | Writes |
|---|---|---|---|
| `Loaders/Rivals Export/export_to_anim.py` | a BRRES with an `AnmChr(NW4R)` folder (e.g. `FitCaptainMotionEtc.pac`'s motion BRRES) | **Export all to anim...** (asks for the fighter's `.mdl0`) | every CHR0 as Maya `.anim`, three sets: `animations_full/` (as in Brawl), `animations_no_trans/` (TransN bone dropped), `animations_no_x/` (TransN Z translation removed); the `ThrowN` bone is renamed `Grab_M` |
| `Loaders/Rivals Export/export_transn_csv.py` | the same BRRES | **Export TransN to CSV...** | `transn_keyframes.csv`: animation, frame, TransN X / Y / Z on every frame where TransN has a keyframe (the movement baked into the animation) |
| `Loaders/Rivals Export/export_bone_list.py` | an MDL0 | **Extract Bones** | `bones.csv`: bone index, name and parent |

Output goes to BrawlCrate's working folder (`./`), normally the folder `BrawlCrate.exe` is in.

## Requirements

- BrawlCrate v0.42 (tested). The loaders use f-strings, so they need BrawlCrate's IronPython 3.
- markymawk's [BrawlCratePlugins](https://github.com/markymawk/BrawlCratePlugins): the loaders import its
  `Lib/mawwwkLib.py` (`getBones`, `transX` / `transY` / `transZ`). Subscribe to it first (same steps as below).

## Install

1. In BrawlCrate: **Tools > Settings > Updater > Manage Subscriptions**, add
   `https://github.com/CVaranese/brawlcrate-plugins`.
2. BrawlCrate downloads the latest release into `BrawlAPI\Loaders\Rivals Export\`. Accept the prompt to enable the
   new loaders (they start disabled otherwise), then restart BrawlCrate: loaders run once at startup.

Manual install: copy `Loaders/Rivals Export/` into `<BrawlCrate folder>\BrawlAPI\Loaders\` and restart.
If you installed older copies by hand (e.g. in `BrawlAPI\Loaders\Animations\`), delete them, or every menu item
shows up twice.

## Update

BrawlCrate follows this repo's **GitHub Releases**, not its commits: it updates when the latest release's tag
changes, and the version it shows is that tag. Each version here is a release (`vX.Y.Z`) listed in
[CHANGELOG.md](CHANGELOG.md).

To hear about new versions without BrawlCrate, star the repo or use **Watch > Custom > Releases** on GitHub.

## History

The loaders started in the author's (private) PM_Character_Exporter repo under `Loaders/Animations/` (committed 2026-10-09, last changed 2026-10-14; written 2026-05 to 2026-06). This repo starts
from those files, unchanged; an older draft of `export_to_anim.py` (from 2026-05-21, built on a copy of mawwwk's
CHR0 Trim Animation script) had nothing the current one lacks and was left out.

## License

GPL-3.0, the same as markymawk's BrawlCratePlugins, whose library these loaders import. See [LICENSE](LICENSE).
