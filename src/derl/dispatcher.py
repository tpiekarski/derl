#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


import logging

from requests import ConnectionError as RequestConnectionError, Session, Timeout, TooManyRedirects
from requests.adapters import HTTPAdapter
from derl.tracker import get_tracker
from derl import __version__


_logger = logging.getLogger(__name__)
_tracker = get_tracker()

_DEFAULT_RETRY = 5
_DEFAULT_TIMEOUT = 10
_DEFAULT_USER_AGENT = "derl/{0}".format(__version__)
_DEFAULT_ADDITIONAL_HEADER = {"user-agent": _DEFAULT_USER_AGENT}


def _get_status_code(location: str, session: Session, timeout: int) -> int:
    _tracker.stats.inc_requests()
    status_code = 0

    try:
        _logger.debug("Requesting status code for %s", location)
        status_code = session.get(location, timeout=timeout, headers=_DEFAULT_ADDITIONAL_HEADER).status_code
    except Timeout:
        _logger.debug("Waited for %i seconds, giving up getting %s", timeout, location)
    except TooManyRedirects:
        _logger.debug("Redirection Tango, danced enough with %s", location)
    except RequestConnectionError:
        _logger.debug("Connection Error occurred while getting %s", location)

    return status_code


def request(files: list, retry: int = _DEFAULT_RETRY, timeout: int = _DEFAULT_TIMEOUT) -> list:

    if len(files) == 0:
        _logger.debug("No matches for HTTP(S) requests")
        return []

    _logger.debug("Timeout for all HTTP(S) requests is %i seconds", timeout)

    with Session() as session:
        adaptor = HTTPAdapter(max_retries=retry)

        session.mount("http://", adaptor)
        session.mount("https://", adaptor)

        for current_file in files:
            for current_url in current_file.urls:
                current_url.status_code = _get_status_code(current_url.location, session, timeout)

        return files
