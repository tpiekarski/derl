#
# derl: CLI Utility for searching for dead URLs <https://github.com/tpiekarski/derl>
# ---
# Copyright 2020 Thomas Piekarski <t.piekarski@deloquencia.de>
#


from aiounittest import AsyncTestCase

from derl.dispatcher import request
from derl.model.file import File


def _build_test_files() -> list:
    test_file = File("test-file.txt")
    test_file.append("http://www.python.org/", 14)

    return [test_file]


class DispatcherTest(AsyncTestCase):

    async def test_request(self: "DispatcherTest"):
        files = await request(_build_test_files())

        self.assertEqual(files[0].urls[0].status_code, 200)

    async def test_dispatcher_without_any_files(self: "DispatcherTest"):
        files = await request([])

        self.assertEqual(files, [])

    # Following tests "seem" to work, but they do not! Tests do not wait for coroutines,
    # although AsyncTestCase is used and upper two tests are working. Tried solutions:
    #  - pytest-asyncio - It does not work inside classes at all -> Question for StackOverflow
    #  - IsolatedAsyncioTestCase - Class will be available with Python > 3.8.x
    #  - aiounittest - Seems to work, but only without Mocks
    #
    # -> How to use Mocks and return an Exception ith aiounittest? (Question for StackOverflow)
    #

    # todo: Try to write two _working_ tests for too many redirects and connection errors

    # @patch("aiohttp_retry.RetryClient.get")
    # async def test_too_many_redirects(self: "DispatcherTest", mocked_get: "Mock"):
    #     mocked_get.side_effect = TooManyRedirects

    #     files = await request(_build_test_files())
    #     self.assertEqual(files[0].urls[0].status_code, 0)

    # @patch("aiohttp_retry.RetryClient.get")
    # async def test_connection_error(self: "DispatcherTest", mocked_get: "Mock"):
    #     mocked_get.side_effect = ClientConnectionError

    #     files = await request(_build_test_files())
    #     self.assertEqual(files[0].urls[0].status_code, 0)
