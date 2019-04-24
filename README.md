<h1 align='center'>
    Viaducts
</h1>
<h4 align='center'>
    Database connection via [Ducts](https://github.com/airbnb/omniduct/blob/master/omniduct/duct.py#L25).
</h4>

## Install

Dependency

```
pip install git+git://github.com/foxyblue/omniduct.git@b8eae6493ff504f77894cc6ef6c4e09f3b2737bd
pip install pyexasol revlibs-dicts
```

## Usage

```python
from viaducts import Viaducts

viaducts = Viaducts()

exasol = viaducts['exasol']
exasol.query("SELECT 43;", format='pandas')
```

### Example Config

```yaml
databases:
  black:
    protocol: postgresql
    host: localhost
    port: 5432
    username: postgres
    password: _env:BLACK_DB_PW
  exasol:
    protocol: exasol
    host:
      - 'localhost:8563'
    username: _env:EXASOL_USER
    password: _env:EXASOL_PASSWORD
    schema: _env:EXASOL_SCHEMA

filesystems:
  local:
    protocol: localfs
    global_writes: True
  s3_company_bucket:
    protocol: s3
    bucket: company-bucket
```

## Extensions we've need to omniducts

- [X] Support for env var extraction
- [X] With multi-file-config
- [X] Add support for exasol ([Open in PR](https://github.com/airbnb/omniduct/pull/99))
- [X] Add failover support. Already supported by omniducts.
