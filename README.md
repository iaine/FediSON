## FediSON

A simple Python experiment to create a ChucK file and run it. 

This is being to sonify a model of the Fediverse and an experiment
in sonification. 

## Author

Iain Emsley

## Requirements

* ChucK

* Python

## Build

Install ChucK 

git clone

## Usage

```
import sys
from agent import createAgent

data_files = sys.argv[2]

ca = createAgent()

if not data_files:
    print("Usage: python agent.py <filename>")
    sys.exit(0)
    
with open(data_files, 'r') as df:
    data = df.readlines()

ca.create_agents(data_files)
```

## Contributions

Bug fixes and requests should go into the issue queue on Github.

If you want to contribute code, please fork and send a pull request.
