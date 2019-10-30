# -*- coding: utf-8 -*-
"""Script for creating torch doc inventory file."""

import zlib

if __name__ == "__main__":
    inventory_v2 = '''\
# Sphinx inventory version 2
# Project: torch
# Version: 1.1.0
# The remainder of this file is compressed with zlib.
'''.encode() + zlib.compress('''\
torch.Tensor py:class 1 tensors.html -
'''.encode())

    with open('torch.inv', mode='wb') as fd:
        fd.write(inventory_v2)
