# Model training checkpoints 

This file gives the reference/expected output structure for this folder after train.py has been executed from tensorflow_training [README.md](../).

```
tensorflow_training
 ├── model_training_checkpoints
 │ ├── events.out.(filename)
 │ ├── graph.pbtxt
 │ ├── checkpoint
 │ ├── model.ckpt.data-00000-of-00001
 │ ├── model.ckpt.index
 │ ├── model.ckpt.meta
 │ ├── ...
 │ ├── (multiple intermediate model checkpoint files)
 │ ├── ...
 │ ├── model.ckpt-(Total number of steps).data-00000-of-00001
 │ ├── model.ckpt-(Total number of steps).index
 │ ├── model.ckpt-(Total number of steps).meta
 │ ├── pipeline.config
```