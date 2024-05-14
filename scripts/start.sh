#!/bin/bash

export EMAIL="test@email.com"
export PASSWORD="password"
export REPORTS="My Reports.Specific Report"

poetry run python dealogic_report_downloader/main.py