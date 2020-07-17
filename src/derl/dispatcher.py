#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#

import asyncio
import logging

from aiohttp import ClientTimeout
from aiohttp.client_exceptions import ClientConnectionError, TooManyRedirects
from aiohttp_retry import RetryClient

from derl import __version__
from derl.tracker import get_tracker

_logger = logging.getLogger(__name__)
_tracker = get_tracker()

_DEFAULT_RETRY = 5
_DEFAULT_TIMEOUT = 10
_DEFAULT_USER_AGENT = "derl/{0}".format(__version__)
_DEFAULT_ADDITIONAL_HEADER = {"user-agent": _DEFAULT_USER_AGENT}


async def _get_status_code(location: str, client: RetryClient, retry: int) -> int:
    _tracker.stats.inc_requests()
    status_code = 0

    try:
        _logger.debug("Requesting status code for %s", location)
        async with client.get(location, retry_attempts=retry) as response:
            status_code = response.status
    except TooManyRedirects:
        _logger.debug("Redirection Tango, danced enough with %s", location)
    except ClientConnectionError:
        _logger.debug("Connection Error occurred while getting %s", location)

    return status_code


async def _request(files: list, retry: int = _DEFAULT_RETRY, timeout: int = _DEFAULT_TIMEOUT) -> list:
    if len(files) == 0:
        _logger.debug("No matches for HTTP(S) requests")
        return []

    _logger.debug("Timeout for all HTTP(S) requests is %i seconds", timeout)

    client_timeout = ClientTimeout(total=timeout)

    async with RetryClient(headers=_DEFAULT_ADDITIONAL_HEADER, timeout=client_timeout) as client:
        for current_file in files:
            for current_url in current_file.urls:
                current_url.status_code = await _get_status_code(current_url.location, client, retry)

        return files


def run_loop(files: list, retry: int, timeout: int) -> list:
    _logger.info("Starting async dispatcher...")

    event_loop = asyncio.get_event_loop()
    files = event_loop.run_until_complete(_request(files, retry, timeout))

    return files
