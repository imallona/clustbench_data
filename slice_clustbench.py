import argparse
import urllib.request
import urllib.error
import os
import sys

# This is the 1.1.0 release from 2022
COMMIT = "0812ac3c3d3b9cb458dd9a6eca97db44cbd93339"
BASE_URL = f"https://github.com/gagolews/clustering-data-v1/raw/{COMMIT}"


def download_file(url: str, dest_path: str, chunk_size: int = 8192) -> None:
    """
    Downloads a file from the given URL to the specified destination path using chunks.

    Args:
        url (str): The URL of the file to download.
        dest_path (str): The path where the file will be saved.
        chunk_size (int): The size of each chunk in bytes. Default is 8192 (8 KB).

    Raises:
        ValueError: If the URL or destination path is invalid.
        URLError: If there's an issue with the network or URL.
        HTTPError: If the URL returns an HTTP error.
    """
    if not url or not dest_path:
        raise ValueError("URL and destination path must be provided.")

    try:
        with urllib.request.urlopen(url) as response, open(dest_path, 'wb') as out_file:
            while chunk := response.read(chunk_size):
                out_file.write(chunk)
        print(f"File successfully downloaded to {dest_path}")
    except urllib.error.URLError as e:
        print(f"Failed to download file: {e}")
    except urllib.error.HTTPError as e:
        print(f"HTTP error occurred: {e.code} - {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='clustbench dataset slicer')

    parser.add_argument('--output_dir', type=str,
                        help='output directory to store data files.', default=os.getcwd())
    parser.add_argument('--name', type=str, help='name of this module', default='clustbench')
    parser.add_argument('--dataset_generator', type=str, help='dataset generator name, e.g. graves, mnist etc',
                        required = True)
    parser.add_argument('--dataset_name', type=str,
                        help='dataset name, e.g. for `mnist` either `fashion` or `digits`',
                        required = True)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    # we download data from gagowleski repo. From a pinned commit rather than the master branch,
    # but this is the general schema:
    # https://github.com/gagolews/clustering-data-v1/raw/refs/heads/master/mnist/digits.data.gz

    generator = args.dataset_generator
    name = args.dataset_name
    module_name = args.name

    counts = f'{BASE_URL}/{generator}/{name}.data.gz'
    labels = f'{BASE_URL}/{generator}/{name}.labels0.gz'


    download_file(counts, os.path.join(args.output_dir, f"{module_name}.data.gz"))
    download_file(labels, os.path.join(args.output_dir, f"{module_name}.labels0.gz"))


if __name__ == "__main__":
    main()
