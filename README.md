# Eneco Price Rate Integration for Home Assistant
[![Python package](https://github.com/lovebug356/eneco-price-rates/actions/workflows/pythonpackage.yaml/badge.svg)](https://github.com/lovebug356/eneco-price-rates/actions/workflows/pythonpackage.yaml)

## About

This repo contains a custom component for [Home Assistant](https://www.home-assistant.io) that integrates the [Eneco Price Rates](https://eneco.be/nl/elektriciteit-gas/tariefkaarten) for Belgium.

## Running Tests

To run the test suite create a virtualenv (I recommend checking out [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for this) and install the test requirements.

```bash
$ pip install -r requirements.test.txt
```

After the test dependencies are installed you can simply invoke `pytest` to run
the test suite.

```bash
$ pytest
...
---------- coverage: platform linux, python 3.10.6-final-0 -----------
Name                                               Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------------
custom_components/__init__.py                          0      0   100%
custom_components/eneco_price_rates/__init__.py        8      2    75%   14-16
custom_components/eneco_price_rates/eneco_pdf.py      15      0   100%
custom_components/eneco_price_rates/eneco_web.py      22      3    86%   19-21
custom_components/eneco_price_rates/sensor.py         40     40     0%   2-87
custom_components/eneco_price_rates/types.py          21      0   100%
--------------------------------------------------------------------------------
TOTAL                                                106     45    58%


Results (2.01s):
```
