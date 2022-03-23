"""
Provides a base test class for other test classes to inherit from.

Includes the numpy testing functions as methods.
"""
import unittest
import pytest
import json
from fastapi.testclient import TestClient
from AcmeInstrumentsService.main import app


class TestRunProgram(unittest.TestCase):
    """
    Superclass for test cases
    """

    def __init__(self, *args, **kwargs):
        """Instance initialisation."""
        # First do the __init__ associated with parent class
        super().__init__(*args, **kwargs)
        self.client = TestClient(app)

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        r"""
        Pass-through for accessing pytest.capsys fixture with class methods.

        Returns
        -------
        capture : pytest.CaptureFixture[str]

        Example
        -------
        To use this fixture with your own subclass of ``BaseTestCase``::

            class TestVerbose(BaseTestCase):
                def test_output(self):
                    print("hello")
                    captured = self.capsys.readouterr()
                    self.assert_string_equal(captured.out, "hello\n")

        Note
        ----
        capsys will capture all messages sent to stdout and stderr since the
        last call to capsys (or since execution began on the test). To test the
        output of a particular command, you may want to do a capture before the
        command to clear stdout/stderr before running the command and then
        capturing its output.

        See Also
        --------
        - https://docs.pytest.org/en/stable/reference.html#capsys
        - https://docs.pytest.org/en/stable/capture.html
        """
        self.capsys = capsys

    def recapsys(self, *captures):
        r"""
        Capture stdout and stderr, then write them back to stdout and stderr.

        Capture is done using the :func:`pytest.capsys` fixture. Used on its
        own, :func:`~pytest.capsys` captures outputs to stdout and stderr,
        which prevents the output from appearing in the usual way when an
        error occurs during testing.

        By chaining series of calls to ``capsys`` and ``recapsys`` around
        commands whose outputs must be inspected, all output directed to stdout
        and stderr will end up there and appear in the "Captured stdout call"
        block in the event of a test failure, as well as being captured here
        for the test.

        Parameters
        ----------
        *captures : pytest.CaptureResult, optional
            A series of extra captures to output. For each `capture` in
            `captures`, `capture.out` and `capture.err` are written to stdout
            and stderr, respectively.

        Returns
        -------
        capture : NamedTuple
            `capture.out` and `capture.err` contain all the outputs to stdout
            and stderr since the previous capture with :func:`~pytest.capsys`.

        Example
        -------
        To use this fixture with your own subclass of ``BaseTestCase``::

            class TestVerbose(BaseTestCase):
                def test_hello_world(self):
                    print("previous message here")
                    message = "Hello world!"
                    capture_pre = self.capsys.readouterr()  # Clear stdout
                    print(message)
                    capture_post = self.recapsys(capture_pre)  # Capture & output
                    self.assert_string_equal(capture_post.out, message + "\n")
        """
        capture_now = self.capsys.readouterr()
        for capture in captures + (capture_now,):
            sys.stdout.write(capture.out)
            sys.stderr.write(capture.err)
        return capture_now

    def test_run_program_returns_195(self):

        # We first load the program
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse", 10, "Acme_pulse_1", "Acme_pulse_2", 120, "Acme_pulse_2", "Acme_pulse_1", "Acme_pulse_1", 3, "Acme_pulse_2", "Acme_pulse_2", 2] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 200
        program_id = response.json()["program_id"]
        assert "AcmeProgramId" in program_id

        # And then we run it
        response = self.client.get(f"/run_program/{program_id}")

        assert response.status_code == 200
        assert json.loads(response.content)["result"] == 195

    def test_run_an_invalid_program(self):
        assert False
