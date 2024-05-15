# Dealogic report downloader

## Prerequisite

Install python & [poetry](https://python-poetry.org/), needed for docs diagrams:

```
curl -sSL https://install.python-poetry.org | python3 -

poetry install
```

Now download browser binaries and their dependencies:

```
poetry shell
playwright install
```

## Usage

First step is to retrieve `access_token` for provided credentials:

```
export EMAIL="test@test.com"
export PASSWORD="test"

./scripts/get_auth_token.sh
```

Then we can make request for specific report data, swagger docs for API are available at: \
https://api.reporting.cortex.dealogic.com/index.html

```
export ACCESS_TOKEN="access-token"
export REPORT_ID="id-of-report"

./scripts/get_report_data.sh
```
