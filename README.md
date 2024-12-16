Structures Gagolewski's `clustering-data-v1` in an omnibenchmark-friendly way, being dataset defined by the data-specific parameters

As args it requires the dataset generator (e.g. mnist) and the dataset name (e.g. fashion)

```
python slice_clustbench.py --dataset_generator mnist --dataset_name fashion
```

It downloads both data and labels with filenames following the encoding: 

- for counts: `os.path.join(args.output_dir, f"{generator}_{name}.data.gz")`
- for labels: `os.path.join(args.output_dir, f"{generator}_{name}.labels0.gz")`
