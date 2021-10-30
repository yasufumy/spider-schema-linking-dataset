# Spider Schema Linking Dataset

This repository provides the schema linking annotation on [Spider](https://github.com/taoyds/spider).  
It is released along with our paper: An Investigation between Schema Linking and Text-to-SQL Performance.  
By using this dataset,  you can evaluate the performance of schema linking.

## Installation

```bash
git clone https://github.com/yasufumy/spider-schema-linking-dataset
cd spider-schema-linking-dataset
pipenv install
```

## Usage

```bash
cd spider-schema-linking-dataset
pipenv run evaluate --gold data/schema-linking/dev.txt --pred /path/to/your/output
```

## Citation

```
@misc{taniguchi2021investigation,
      title={An Investigation Between Schema Linking and Text-to-SQL Performance}, 
      author={Yasufumi Taniguchi and Hiroki Nakayama and Kubo Takahiro and Jun Suzuki},
      year={2021},
      eprint={2102.01847},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
