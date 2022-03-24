"""
Provides a base test class for other test classes to inherit from.

Includes the numpy testing functions as methods.
"""
import unittest
import pytest
import json
from fastapi.testclient import TestClient
from AcmeInstrumentsService.program.load.load_program import load_program
from AcmeInstrumentsService.program.run.run_program import run_program
from AcmeInstrumentsService.main import app


class TestLoadProgram(unittest.TestCase):
    """
    Superclass for test cases
    """

    def __init__(self, *args, **kwargs):
        """Instance initialisation."""
        # First do the __init__ associated with parent class
        super().__init__(*args, **kwargs)
        self.client = TestClient(app)

    def test_load_program_returns_ok(self):
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse", 10, "Acme_pulse_1", "Acme_pulse_2", 120, "Acme_pulse_2", "Acme_pulse_1", "Acme_pulse_1", 3, "Acme_pulse_2", "Acme_pulse_2", 2] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)
        import pdb

        pdb.set_trace()

        assert response.status_code == 200
        assert "AcmeProgramId" in response.json()["program_id"]

    def test_load_pulse_sequence_doesnt_exist(self):
        # We first load the program
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse", 10, "Acme_pulse_1", "Acme_pulse_1", "Acme_pulse_2", 2] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 452

    def test_load_malformed_sequence_in_program(self):
        # We first load the program
        pulse_sequence = '{ "program_code": ["Acme_initial_state_pulse"] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 454

    def test_load_empty_program(self):
        # We first load the program
        pulse_sequence = '{ "program_code": [] }'
        json_pulses = json.loads(pulse_sequence)
        response = self.client.post("/load_program", json=json_pulses)

        assert response.status_code == 454
