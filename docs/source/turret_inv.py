# -*- coding: utf-8 -*-
"""Script for creating turret doc inventory file."""

import zlib

if __name__ == "__main__":
    inventory_v2 = '''\
# Sphinx inventory version 2
# Project: turret
# Version: 4.0.1
# The remainder of this file is compressed with zlib.
'''.encode() + zlib.compress('''\
turret.InferenceEngine py:class 1 blob/master/turret/engine.pyx -
turret.layers.LSTMParameterSet py:class 1 blob/master/turret/layers/lstm.py -
turret.logger.Logger py:class 1 blob/master/turret/logger.pyx -
turret.NetworkDefinition py:class 1 blob/master/turret/graph.pyx -
turret.Severity py:class 1 blob/master/turret/logger.pyx -
turret.Tensor py:class 1 blob/master/turret/graph.pyx -
'''.encode())

    with open('turret.inv', mode='wb') as fd:
        fd.write(inventory_v2)
