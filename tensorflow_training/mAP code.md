

# mAP evaluation code 

-  Open the anaconda command prompt(virtual environment), the code should be run in the following virtual environment

```
$ activate virtual environment
activate tf1.12_gpu
```

- Copy the python eval.py file from the legacy folder and paste it where you have your checkpoints and pipeline_config_path saved(folder).

- Run the below code in the virtual environment to get mAP score in both tensorboard and command prompt.

  ```
  $ To get mAP score for entire dataset and each class
  
  python eval.py --logtostderr --checkpoint_dir=model_for_training/ --eval_dir=evaluation/ --pipeline_config_path=model_for_training/ssd_mobilenet_v2_coco.config
  ```



where,

`checkpoint_ dir` = This is the directory where you have your checkpoint meta file which is saved at the end of your training simulation.

``eval_dir`= This the directory where you want your mAP scores to be saved.

`pipeline_config_path=` This is the directory which contains your network configuration file. E.g. ssd_mobilenet_v2_coco.config which you have modified according to your requirement's before training the dataset.

