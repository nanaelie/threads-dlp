from dataclasses import dataclass


@dataclass(frozen=True)
class Media:
    post_id: str
    url: str
    referer: str
