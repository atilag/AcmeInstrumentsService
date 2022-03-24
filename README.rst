Acme Instruments Service
========================

This is a REST service that will simulate the control electronic instruments used in superconducting based quantum computers.
The simulation is pretty strightforward, and not Quantum at all.

Endpoints
=========

This is the endpoint for loading a program: 

```
POST /load_program
```


The input of the service is a sequence of pulses and values that will map to some simple algebraic operations: Summation, Multiplication and Division.

The format of the input JSON should follow this schema:

```
   "program_code":[
      "Acme_initial_state_pulse",
      10,
      "Acme_pulse_1",
      "Acme_pulse_2",
      120,
      "Acme_pulse_2",
      "Acme_pulse_1",
      "Acme_pulse_1",
      3,
      "Acme_pulse_2",
      "Acme_pulse_2",
      2
   ]
`
```


This is the endpoint for triggering the execution of the program:

```
GET /run_program/<program_id>
```


In case of sucess, the HTTP code will be 200 and the response JSON will be:
```
{
     "program_id": "AcmeProgramId1"
}
```


Workflow
=======
Dute to some hardware imposed constrains, we always need to load the program first, and then trigger the execution.
When we call the /load_program endpoint with the corresponding request body and we will receive a response with a "Program ID".
This "Program ID" needs to be used in a later call to the /run_program endpoint so the service identifies the program to run.

This implies two REST calls:
POST /load_program {...}
GET /run_program/<program_id>
