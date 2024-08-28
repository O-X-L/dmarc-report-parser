# DMARC Report Parser

[![Lint](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/lint.yml/badge.svg?branch=master)](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/lint.yml)
[![Unit Tests](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/test-unit.yml/badge.svg?branch=master)](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/test-unit.yml)
[![Integration Tests](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/test-integration.yml/badge.svg?branch=master)](https://github.com/O-X-L/dmarc-report-parser/actions/workflows/test-integration.yml)

[Documentation](https://dmarc-report-parser.o-x-l.com/)

## Upstream

**WARNING**: This is a work-in-progress fork of the [parsedmarc project](https://github.com/domainaware/parsedmarc).

This fork aims to refactor the code base of the project to have:

* Less huge functions
* A more Object-Oriented structure
* Unit Testing

<p align="center">
  <img src="https://github.com/domainaware/parsedmarc/raw/master/docs/source/_static/screenshots/dmarc-summary-charts.png?raw=true" alt="A screenshot of DMARC summary charts in Kibana"/>
</p>

----

## Features

- Parses draft and 1.0 standard aggregate/rua reports
- Parses forensic/failure/ruf reports
- Can parse reports from an inbox over IMAP, Microsoft Graph, or Gmail
    API
- Transparently handles gzip or zip compressed reports
- Consistent data structures
- Simple JSON and/or CSV output
- Optionally email the results
- Optionally send the results to Elasticsearch and/or Splunk, for use
    with premade dashboards
- Optionally send reports to Apache Kafka
