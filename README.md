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

viaduct.query("SELECT 43;", format=pandas)
```

## Config

```yaml
databases:
  black:
    protocol: postgresql
    host: localhost
    port: 5432
    username: postgres
    password: _env:BLACK_DB_PW
filesystems:
  local:
    protocol: localfs
    global_writes: True
  s3_company_bucket:
    protocol: s3
    bucket: company-bucket
```

## Extensions we've made to omniducts

- [X] With multi-file-config registrar
- [X] Support for env var extraction
- [ ] Add support for exasol
- [ ] Add failover support
