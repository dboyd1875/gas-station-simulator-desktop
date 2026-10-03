"""Gas Station Simulator Desktop — Local Windows and macOS helper for Gas Station Simulator data paths, config and export caches, and export folders."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='gas_station_simulator_desktop',
        description='Local Windows and macOS helper for Gas Station Simulator data paths, config and export caches, and export folders.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Gas Station Simulator Desktop')
    print('Find the Gas Station Simulator folder fast and keep a local spare.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
