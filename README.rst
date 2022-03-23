Acme Instruments Service
========================

This is a REST service that will simulate the control electronic instruments used in superconducting based quantum computers.
The simulation is pretty strightforward, and not Quantum at all.

The input of the service is a sequence of pulses and values that will map to some simple algebraic operations: Summation, Multiplication and Division.

The format of the input JSON should follow this schema:

{


}


The output of will have this JSON format:
 
 {


 }


Endpoints
=========

This is the endpoint for loading a program: 

/load_program


This is the endpoint for triggering the execution of the program:

/run_program

Workflow
=======
Dute to some hardware imposed constrains, we always need to load the program first, and then trigger the execution.
When we call the /load_program endpoint with the corresponding request body and we will receive a response with a "Program ID".
This "Program ID" needs to be used in a later call to the /run_program endpoint so the service identifies the program to run.

This implies two POST calls:
POST /load_program { }
POST /run_program { }
