from pydantic import BaseModel, ConfigDict, Field

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str | None = None
    username: str | None = None
    language_code: str | None = None

class Chat(BaseModel):
    id: int
    first_name: str | None = None
    username: str | None = None
    type: str

class Message(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    message_id: int
    from_user: User = Field(alias="from")
    chat: Chat
    date: int
    text: str | None = None

class WebhookBody(BaseModel):
    update_id: int
    message: Message | None = None
