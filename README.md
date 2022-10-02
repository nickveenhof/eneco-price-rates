# Eneco Price Rate Integration for Home Assistant

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
```
