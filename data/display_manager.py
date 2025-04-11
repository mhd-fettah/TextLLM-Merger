from tqdm import tqdm
import os

class DummyTqdm:
    def __init__(self, total, desc, unit):
        self.total = total
        self.desc = desc
        self.unit = unit
    def update(self, n):
        pass
    def set_description(self, desc):
        self.desc = desc
    def write(self, message):
        print(message)

def init_progress(total_images):
    """
    Initialize and return a tqdm progress bar with a given number of total images.
    If the environment variable DISABLE_TQDM is set, returns a dummy progress object.
    """
    if os.getenv("DISABLE_TQDM", "false").lower() in ["true", "1", "yes"]:
        return DummyTqdm(total=total_images, desc="Starting...", unit="img")
    else:
        return tqdm(total=total_images, desc="Starting...", unit="img")

def update_description(pbar, image_name):
    """
    Update the progress bar's description with the image currently being processed.
    """
    pbar.set_description(f"Processing: {image_name}")

def write_message(pbar, message):
    """
    Write a message to the console without disrupting the progress bar.
    """
    pbar.write(message)

def print_summary(batch_id, total_images, success_count, fail_count, total_time, avg_time):
    """
    Print a nicely formatted summary of the batch processing.
    """
    summary = (
        "\n=== Batch Processing Summary ===\n"
        f"Batch ID: {batch_id}\n"
        f"Total images processed: {total_images}\n"
        f"Successfully processed: {success_count}\n"
        f"Failed processing: {fail_count}\n"
        f"Total time: {total_time:.2f} sec, Average per image: {avg_time:.2f} sec\n"
    )
    print(summary)
