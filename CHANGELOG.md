# Changelog

Each version is a GitHub Release with the same tag; BrawlCrate subscribers update when a new release is published.

## v1.0.1 (2026-10-31)

- Extract Bones: stops after "No bones found." instead of raising an error.
- Export all to anim / Export TransN to CSV: read only a folder named exactly `AnmChr(NW4R)` (it used to accept any
  folder whose name was part of that string).

## v1.0.0 (2026-10-31)

- First release: `Export all to anim...`, `Export TransN to CSV...` and `Extract Bones` in `Loaders/Rivals Export/`,
  unchanged from the copies used for the P+ Captain Falcon port since 2026-06 (tested in BrawlCrate v0.42 there).
