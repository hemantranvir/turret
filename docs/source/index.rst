##################################
Welcome to Turret's documentation!
##################################

Turret is a Pythonic wrapper for TensorRT.

Turret has been developed to solve the inconvenience of TensorRT's Python API and to
access functions which cannot be accessed by the Python API.  

Turret provides high level API for accessing commonly used deep learning layers
and objects to create and use the inference engine.


.. toctree::
   :caption: User Guide
   :maxdepth: 4

   guide/install.rst
   guide/tutorial.rst
   guide/samples.rst
   guide/tests.rst


The API reference contains detailed descriptions of the different end-user
classes, functions, methods, etc. you will need to work with Turret.

.. note::

  This API reference only contains *end-user* documentation. If you are
  looking for Turret's internals, you will find more detailed
  comments in the source code.

.. toctree::
   :caption: API Reference
   :maxdepth: 4

   apis/core/index.rst
   apis/layers/layers.rst
   apis/int8/int8.rst
   apis/loggers/loggers.rst
   apis/caffe/caffe.rst
   apis/plugin/plugin.rst

******************
Indices and tables
******************
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
