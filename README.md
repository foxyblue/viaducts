<h1 align='center'>
    Viaducts
</h1>
<h4 align='center'>
    Database connection via ducts.
</h4>

## Usage

```python
from viaducts import Viaducts

viaducts = Viaducts()
viaduct = viaducts['postgres']

viaduct.query("SELECT version();")
```

## Omniducts extensions

- [X] With multi-file-config registrar
- [X] Support for env var extraction
- Add support for exasol
- Add failover support
