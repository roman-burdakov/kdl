# KDL 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0edf700423a54508b146213f8e721a71)](https://app.codacy.com/app/k-descriptor-language/kdl?utm_source=github.com&utm_medium=referral&utm_content=k-descriptor-language/kdl&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.com/k-descriptor-language/kdl.svg?branch=master)](https://travis-ci.com/k-descriptor-language/kdl)
[![codecov](https://codecov.io/gh/k-descriptor-language/kdl/branch/master/graph/badge.svg)](https://codecov.io/gh/k-descriptor-language/kdl)
[![Documentation Status](https://readthedocs.org/projects/kdl/badge/?version=latest)](https://kdl.readthedocs.io/en/latest/?badge=latest)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

K Descriptor Language serves as a domain specific language for authoring and manipulating KNIME workflows.

[Documentation](https://kdl.readthedocs.io/en/latest/?badge=latest)

## Install Package
`python3 setup.py install`

## Run

```bash
❯ kdlc --help
Usage: kdlc [OPTIONS]

Options:
  -o, --output TEXT            The output file, either .knwf or .kdl  [required]
  -i, --input PATH             The input file, either .knwf or .kdl  [required]
  -d, --debug                  Print debug logging to stdout
  -tp, --templates_path PATH   Path to a custom templates catalogue
  --help                       Show this message and exit.
```
