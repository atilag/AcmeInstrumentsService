# `name` is the name of the package as used for `pip install package`
name = "AcmeInstrumentsService"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "IBM Quantum team"
author_email = "juan.gomez.mosquera1@ibm.com"
description = "REST Service for using quantum computer instruemnt controllers"  # One-liner
url = "https://github.com/atilag/AcmeInstrumentsService"  # your project homepage
license = "MIT"  # See https://choosealicense.com
