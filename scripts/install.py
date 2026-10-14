#!/usr/bin/env python3
"""Install the bundled skill without overwriting a different existing copy."""
import argparse, hashlib, os, shutil
from pathlib import Path

def digest(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path, help='Skills parent directory')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / 'skills' / 'pyramid-studio'
    parent = args.destination or Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex'))) / 'skills'
    target = parent.expanduser().resolve() / 'pyramid-studio'
    if not (source / 'SKILL.md').is_file():
        parser.error('Bundled SKILL.md is missing')
    if target.exists():
        if target.is_dir() and digest(source) == digest(target):
            print(f'Already installed: {target}')
            return
        parser.error(f'Destination already exists with different content: {target}. Back it up or choose another destination.')
    if args.dry_run:
        print(f'Would install: {source} -> {target}')
        return
    parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)
    if digest(source) != digest(target):
        raise SystemExit('Installation verification failed')
    print(f'Installed and verified: {target}')
    print('Start a new Codex chat; invoke $pyramid-studio.')

if __name__ == '__main__':
    main()
