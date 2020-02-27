

**mAP evaluation code** 

`` Use this in the anaconda command prompt(virtual environment)

`` Copy the python eval.py file from the legacy folder and paste it where you have your checkpoints and pipeline_config_path saved(folder).



python eval.py --logtostderr --checkpoint_dir=model_for_training/ --eval_dir=evaluation/ --pipeline_config_path=model_for_training/ssd_mobilenet_v2_coco.config



`checkpoint` dir = your trained model checkpoint location

`eval` dir= where you want evaluation output results

`pipeline_config_path=` your trained model config file location and network used

