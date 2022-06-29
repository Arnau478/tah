#!/usr/bin/env python3

import sys
import os
import shutil

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <pkg_name>")
        exit(1)
    
    pkg_name = sys.argv[1]

    if not os.path.exists("/tmp/tah/pkg"): os.makedirs("/tmp/tah/pkg")
    os.chdir("/tmp/tah/pkg")
    os.system(f"git clone https://aur.archlinux.org/{pkg_name}.git")
    os.chdir(f"/tmp/tah/pkg/{pkg_name}")
    os.system(f"makepkg -si {pkg_name}")
    shutil.rmtree(f"/tmp/tah/pkg/{pkg_name}")

if __name__ == "__main__":
    main()
