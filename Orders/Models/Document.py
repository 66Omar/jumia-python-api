from dataclasses import dataclass


@dataclass
class Document:
    document_type: object = None
    mime_type: object = None
    file: object = None
