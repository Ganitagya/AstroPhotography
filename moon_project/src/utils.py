import os

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_images(directory, ext='.png'):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(ext)]


