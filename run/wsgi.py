#!/usr/bin/env python3
# WSGI: Web service gateway interface


from core import omnibus


if __name__ == "__main__":
    omnibus.run(host="127.0.0.1", port=5000, debug=True)