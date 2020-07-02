#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


import logging
import requests

from requests import ConnectionError as RequestConnectionError, Session, Timeout, TooManyRedirects
from requests.adapters import HTTPAdapter
from derl.model.stats import get_stats

_logger = logging.getLogger(__name__)
_stats = get_stats()

_DEFAULT_RETRY = 3
_DEFAULT_TIMEOUT = 10


def request(files, retry=_DEFAULT_RETRY, timeout=_DEFAULT_TIMEOUT):
    if len(files) == 0:
        _logger.debug("No matches for HTTP requests")
        return []

    _logger.debug("Timeout for all HTTP requests is %i seconds", timeout)

    http_adaptor = HTTPAdapter(max_retries=retry)
    session = Session()

    for current_file in files:
        for current_url in current_file.urls:
            try:
                session.mount(current_url.location, http_adaptor)
                _logger.debug("Requesting status code for %s", current_url.location)
                _stats.inc_requests()
                current_url.status_code = requests.get(current_url.location, timeout=timeout).status_code
            except Timeout:
                _logger.debug("Waited for %i seconds, giving up getting %s", timeout, current_url.location)
                current_url.status_code = 0
            except TooManyRedirects:
                _logger.debug("Redirection Tango, danced enough with %s", current_url.location)
                current_url.status_code = 0
            except RequestConnectionError:
                _logger.debug("Connection Error occurred while getting %s", current_url.location)
                current_url.status_code = 0

    return files
