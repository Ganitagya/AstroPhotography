import rawpy
import imageio
import os
import glob
from .config import RAW_PROCESSING_PARAMS

def process_raw(input_path, output_path, params=RAW_PROCESSING_PARAMS):
    with rawpy.imread(input_path) as raw:
        rgb = raw.postprocess(
            use_camera_wb=params['use_camera_wb'],
            no_auto_bright=params['no_auto_bright'],
            output_bps=params['output_bps'],
            gamma=params['gamma'],
            bright=params['bright'],
            user_flip=params['user_flip']
        )
    imageio.imwrite(output_path, rgb)

def batch_process_raw(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    raw_files = glob.glob(os.path.join(input_folder, '*.NEF'))
    for raw_path in raw_files:
        base = os.path.basename(raw_path).replace('.NEF', '_processed.png')
        output_path = os.path.join(output_folder, base)
        process_raw(raw_path, output_path)

