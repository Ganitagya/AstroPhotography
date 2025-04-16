from moon_stitcher import preprocess
from moon_stitcher.utils import ensure_dir

SECTION_DIRS = ['top', 'bottom', 'left', 'right']
RAW_BASE = 'data/raw'
PROCESSED_BASE = 'data/processed'

def main():
    for section in SECTION_DIRS:
        raw_dir = f'{RAW_BASE}/{section}'
        processed_dir = f'{PROCESSED_BASE}/{section}'
        ensure_dir(processed_dir)
        print(f"Processing section: {section}")
        preprocess.batch_process_raw(raw_dir, processed_dir)

if __name__ == '__main__':
    main()

