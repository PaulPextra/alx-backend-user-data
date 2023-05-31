#!/usr/bin/env python3

"""
SessionAuth module
"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    SessionAuth class.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Method: create_session - creates a Session ID for a user_id.
        """

        if not user_id or type(user_id) != str:
            return
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Method: user_id_for_session_id - returns a User ID based on a Session ID.
        """

        if not session_id or type(session_id) != str:
            return
        return SessionAuth.user_id_by_session_id.get(session_id, None)
