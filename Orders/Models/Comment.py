from dataclasses import dataclass


@dataclass
class Comment:
    comment_id: object = None
    username: object = None
    content: object = None
    comment_type: object = None
    is_opened: object = None
    is_answered: object = None
    created_at: object = None
    updated_at: object = None
    comments: object = None
