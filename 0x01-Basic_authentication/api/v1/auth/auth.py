#!/usr/bin/env python3
"""
3. Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public Method: require_auth
        """
        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        for e in excluded_paths:
            if path == e:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Public Method: authorization_header
        """
        if request:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public Method: curent_user
        """
        return None