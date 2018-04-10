# Street Address Parser

This is a command line utility using Python standard libraries to parse street addresses in the
country schemes DE, ES, FR, and US.

# Prerequisites
* A working Python installation, minimum version 3.6.
* Add your Python command line interpreter to the PATH

## Usage
Example for parsing an address (simple address profile) - open a command line prompt, change to the
project directory and execute:
```
$ python street_address_parser.py "foobar 23"
{"foobar", "23"}
```

## Help
From the project directory, you can get command line help by running this:
```
$ python street_address_parser.py --help
```

## Test Execution
Open a command line prompt, change to the project directory and run the following command:
```
$ python -m unittest discover
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

# Implementation Notes
## Assumptions
* Addresses don't contain funny unicode characters. I only considered the test cases provided in
the coding challenge.
* Functional correctness is primary for this task, performance is secondary. If performance would
be primary (e.g., for quickly parsing large numbers of addresses), I would reconsider the use of
regular expressions and possibly also the use of Python.

## Home-made vs off-the-shelf solutions
I first tried several open-source libraries (Python) for address parsing, but they all failed one
or more of the addresses. The most promising one was https://github.com/datamade/usaddress, but it
failed parse ES addresses correctly. Apart from that, the library looks really good and they even
offer a API for bulk processing (https://parserator.datamade.us/api-docs).
With these insights, I opted for a home-made solution. However, if I were to require a fully fledged
parser for all sorts of address formats as utility for professional use, I would try not to build
this myself and rather focus my efforts on the core business functionality.
