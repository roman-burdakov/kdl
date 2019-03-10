# kdl-poc

Takes input KNIME workflow called "TestWorkflow.knwf", extracts values from the CSV Reader node and generates new workflow "TestWorkflow_new.knwf" using template file

## Install dependencies
`pip3 install -r requirements.txt`

## Run

`python3 application.py -i TestWorkflow.knwf`


## Test
`python3 -m pytest -s`