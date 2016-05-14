# opt_searchtree.py
Creates tables for probabilities and expectations of accessing trees and subtrees to create an opt searchtree

Uses [tabulate](https://bitbucket.org/astanin/python-tabulate) module

Example Usage:

```bash
./opt_searchtree.py

Keys (ex. [1,2,3,4,5]): ["ETH","KIT","MIT","RWTH","TUM"]
Probabilities (ex. [0.2,0.1,0.5,0.1,0.1]): [0.25,0.05,0.35,0.2,0.15]
[i] Everything ok! Generating Tables...

[w]ij:
|   ETH |   KIT |   MIT |   RWTH |   TUM |
|-------+-------+-------+--------+-------|
|  0.25 |  0.3  |  0.65 |   0.85 |  1    |
|  0    |  0.05 |  0.4  |   0.6  |  0.75 |
|  0    |  0    |  0.35 |   0.55 |  0.7  |
|  0    |  0    |  0    |   0.2  |  0.35 |
|  0    |  0    |  0    |   0    |  0.15 |

[i] Roots: 

[ETH to KIT] = ETH
[KIT to MIT] = MIT
[MIT to RWTH] = MIT
[RWTH to TUM] = RWTH
[ETH to MIT] = MIT
[KIT to RWTH] = MIT
[MIT to TUM] = MIT
[ETH to RWTH] = MIT
[KIT to TUM] = MIT
[ETH to TUM] = MIT


[e]ij:
|   ETH |   KIT |   MIT |   RWTH |   TUM |
|-------+-------+-------+--------+-------|
|  0.25 |  0.35 |  1    |   1.4  |  1.85 |
|  0    |  0.05 |  0.45 |   0.85 |  1.3  |
|  0    |  0    |  0.35 |   0.75 |  1.2  |
|  0    |  0    |  0    |   0.2  |  0.5  |
|  0    |  0    |  0    |   0    |  0.15 |
```

Probabilities must add up to 1.0 and must be floating point numbers.
Roots are displayed in case you want to actually draw or create the opt searchtree from these values.
