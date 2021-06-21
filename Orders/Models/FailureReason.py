from dataclasses import dataclass


@dataclass
class FailureReason:
    type: object = None
    name: object = None
