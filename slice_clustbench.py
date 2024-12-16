import argparse
import os
import wget
import sys

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
    
    # clone source
    # rather, download
    # https://github.com/gagolews/clustering-data-v1/raw/refs/heads/master/mnist/digits.data.gz

    generator = args.dataset_generator    
    name = args.dataset_name

    counts = f'https://github.com/gagolews/clustering-data-v1/raw/refs/heads/master/{generator}/{name}.data.gz'
    labels = f'https://github.com/gagolews/clustering-data-v1/raw/refs/heads/master/{generator}/{name}.labels0.gz'
    
    wget.download(counts, os.path.join(args.output_dir, f"{generator}_{name}.data.gz"))
    wget.download(labels, os.path.join(args.output_dir, f"{generator}_{name}.labels0.gz"))


if __name__ == "__main__":
    main()
