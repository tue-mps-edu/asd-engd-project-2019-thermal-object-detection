"""egohands_models.py
"""


SUPPORTED_MODELS = {
    'ssd_mobilenet_v1_egohands': {
        'config_path': 'data/ssd_mobilenet_v1_egohands.config',
        'checkpoint_path': 'data/ssd_mobilenet_v1_egohands/model.ckpt-20000',
    },
}


def get_egohands_model(model_name):
    assert model_name in SUPPORTED_MODELS
    return (SUPPORTED_MODELS[model_name]['config_path'],
            SUPPORTED_MODELS[model_name]['checkpoint_path'])
