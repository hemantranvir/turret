#################
Turret Tutorial
#################

The general workflow to build a network and run inference is as follows:

1. Import necessary modules

.. code-block:: python

   import turret
   import numpy as np
   import pycuda.autoinit
   import pycuda.driver as cuda
   import turret.layers as L

1. Create a builder object of :any:`turret.engine.InferenceEngineBuilder` type.

.. code-block:: python

   logger = turret.loggers.ConsoleLogger()
   builder = turret.InferenceEngineBuilder(logger)


2. Create an empty network (of type :any:`turret.graph.NetworkDefinition`) using the builder object created above.

.. code-block:: python

   network = builder.create_network(turret.DataType.FLOAT)


3. Add inputs, logic for inference and outputs to the network.

* ``emb`` is input word embedings vector

* ``max_sequence_length`` is the maximum length of the input ``words``

* In the example below, we are simply gathering the word embedding
  vectors for the corresponding indices supplied by the ``words`` input

.. code-block:: python

   emb = np.random.randn(10,5)
   src = network.add_constant(emb)
   max_sequence_length = 5
   h = network.add_input(
       "words", turret.DataType.INT32,
       turret.Dimensions((
           (1, turret.DimensionType.INDEX),
           (max_sequence_length, turret.DimensionType.INDEX))))
   out = L.gather(src, h, 0)
   network.mark_output("out", out)


4. Set the maximum batch size etc.

.. code-block:: python

   builder.max_batch_size = 1
   builder.max_workspace_size = 1 * (2 ** 30)

5. Build the network to get an :any:`turret.engine.InferenceEngine` object.

.. code-block:: python

   engine = builder.build(network)


Following build log is displayed:

.. code-block:: console

   [INFO] Applying generic optimizations to the graph for inference.
   [INFO] Original: 2 layers
   [INFO] After dead-layer removal: 2 layers
   [INFO] After scale fusion: 2 layers
   [INFO] After vertical fusions: 2 layers
   [INFO] After swap: 2 layers
   [INFO] After final dead-layer removal: 2 layers
   [INFO] After tensor merging: 2 layers
   [INFO] After concat removal: 2 layers
   [INFO] Graph construction and optimization completed in 0.000347243 seconds.
   [INFO] 
   [INFO] --------------- Timing (Unnamed Layer* 1) [Gather](24)
   [INFO] Tactic 0 is the only option, timing skipped
   [INFO] Formats and tactics selection completed in 1.1994 seconds.
   [INFO] After reformat layers: 2 layers
   [INFO] Block size 1073741824
   [INFO] Total Activation Memory: 1073741824
   [INFO] Detected 1 input and 1 output network tensors.
   [INFO] Data initialization and engine generation completed in 0.0299379 seconds.


6. Create a :any:`turret.engine.ExecutionContext` object using the engine object.

.. code-block:: python

   context = turret.ExecutionContext(engine)


7. Create a :any:`turret.buffer.InferenceBuffer` using the context object.

.. code-block:: python

   buf = context.create_buffer()


8. Run Inference

* Create a cuda stream, populate the ``words`` input, call enqueue and synchronize,
  get the results

.. code-block:: python

   stream = cuda.Stream()
   src_words = np.array([[[1,2,3,4,5]]]).astype(np.int32)
   buf.put("words", src_words)
   context.enqueue(buf, stream)
   stream.synchronize()
   out = buf.get("out")


The output is stored in ``out`` numpy array and contains the word embedding vectors 
for the supplied indices.


