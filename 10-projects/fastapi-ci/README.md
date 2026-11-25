### Do the following before creating your first api

- Create a virtual environment then install fastApi and pytest package

```bash
source .venv/bin/activate
python3 -m pip install "fastapi[standard]"

## packages to run tests
python3 -m pip install httpx
python3 -m pip install pytest
```

- run the server using fastapi command in the venv

```bash
fastapi dev file.py #for dev api
fastapi run file.py #for production api
```

run test file

```bash
python3 -m pytest -v tests/file.py
```
