#!/usr/bin/env python3
"""Pack a Knytt Stories world folder into a .knytt.bin archive.

The .knytt.bin format is a flat archive:

    header:        "NF" + <world folder name> + 0x00 + uint32(len of that name)
    per file:      "NF" + <relative path, '\\' separators> + 0x00 + uint32(size) + data

Editor scratch files (*.temp, *.bkup) are excluded, matching what KSManager
ships. Files are emitted in case-insensitive path order so output is stable.

Usage:
    python tools/pack_knytt.py "Worlds/Masaru-Level" "release/Masaru.knytt.bin"
"""
import os
import struct
import sys

EXCLUDE_EXT = {".temp", ".bkup"}


def pack(world_dir: str, out_path: str) -> None:
    world_dir = os.path.normpath(world_dir)
    folder_name = os.path.basename(world_dir)

    files = []
    for dirpath, _dirs, names in os.walk(world_dir):
        for name in names:
            if os.path.splitext(name)[1].lower() in EXCLUDE_EXT:
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, world_dir).replace(os.sep, "\\")
            files.append((rel, full))
    files.sort(key=lambda f: f[0].lower())

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "wb") as out:
        # header
        out.write(b"NF" + folder_name.encode("ascii") + b"\x00")
        out.write(struct.pack("<I", len(folder_name)))
        # files
        for rel, full in files:
            with open(full, "rb") as fh:
                data = fh.read()
            out.write(b"NF" + rel.encode("ascii") + b"\x00")
            out.write(struct.pack("<I", len(data)))
            out.write(data)

    print(f"Packed {len(files)} files from '{world_dir}' -> '{out_path}' "
          f"({os.path.getsize(out_path)} bytes)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"usage: {sys.argv[0]} <world-folder> <output.knytt.bin>")
    pack(sys.argv[1], sys.argv[2])
