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

    def test_run_program_not_found(self):
        # We first load the program
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse", 10, "Acme_pulse_1", "Acme_pulse_2", 120, "Acme_pulse_2", "Acme_pulse_1", "Acme_pulse_1", 3, "Acme_pulse_2", "Acme_pulse_2", 2] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 200

        # And then we run it
        response = self.client.get(f"/run_program/bad_ID")

        assert response.status_code == 455

    def test_run_division_by_zero(self):
        # We first load the program
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse", 10, "Acme_pulse_1", "Acme_pulse_2", 120, "Acme_pulse_2", "Acme_pulse_1", "Acme_pulse_1", 3, "Acme_pulse_2", "Acme_pulse_2", 0] }'  # Notice the 0 in the pulse sequence that corresponds to Division
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 200
        program_id = response.json()["program_id"]
        assert "AcmeProgramId" in program_id

        # And then we run it
        response = self.client.get(f"/run_program/{program_id}")

        assert response.status_code == 456
