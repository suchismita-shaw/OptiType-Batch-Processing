

# OptiType Batch Processing

This repository contains a simple Bash script to run OptiType on multiple paired-end FASTQ samples automatically.

## Requirements
- OptiType installed
- Python 3
- FASTQ files in gzip format

## Input Files
Place your paired-end FASTQ files inside the `SRA_Input` folder.  
Each sample should be named like this:
SAMPLE_1.fastq.gz
SAMPLE_2.fastq.gz


Example samples:

ERR035536

SRR064286

SRR292246

SRR292249


Output

Results will be saved in the SRA_Output folder, one subfolder per sample.

Example Output Folder

SRA_Output/

├── ERR035536/

├── SRR064286/

├── SRR292246/

└── SRR292249/

Each folder will contain the OptiType result files (result.tsv)
