#!/usr/bin/env python3
"""
6. Basic auth
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    BasicAuth class.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Method: extract_base64_authorization_header.
        """

        if not authorization_header or type(authorization_header) != str or not authorization_header.startswith("Basic "):
            return
        return "".join(authorization_header.split(" ")[1:])
