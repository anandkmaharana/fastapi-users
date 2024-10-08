from typing import Generic, List, Optional, Protocol, TypeVar

ID = TypeVar("ID")


class UserProtocol(Protocol[ID]):
    """User protocol that ORM model should follow."""

    id: ID
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    is_evaluator: bool


class OAuthAccountProtocol(Protocol[ID]):
    """OAuth account protocol that ORM model should follow."""

    id: ID
    oauth_name: str
    access_token: str
    expires_at: Optional[int]
    refresh_token: Optional[str]
    account_id: str
    account_email: str


UP = TypeVar("UP", bound=UserProtocol)
OAP = TypeVar("OAP", bound=OAuthAccountProtocol)


class UserOAuthProtocol(UserProtocol[ID], Generic[ID, OAP]):
    """User protocol including a list of OAuth accounts."""

    id: ID
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    is_evaluator: bool
    oauth_accounts: List[OAP]


UOAP = TypeVar("UOAP", bound=UserOAuthProtocol)
