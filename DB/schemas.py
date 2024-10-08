from pydantic import BaseModel
from typing import List, Optional
from datetime import time

# UserTable 스키마
class UserTableBase(BaseModel):
    userid: str
    name: Optional[str] = '0.0'
    profileimage: Optional[str] = None

class UserTableCreate(BaseModel):
    userid: str

class UserTableUpdate(BaseModel):
    name: Optional[str] = None
    profileimage: Optional[str] = None

class UserTableInDB(UserTableBase):
    pass

class UserTableOut(UserTableInDB):
    pass

# AITable 스키마
class AITableBase(BaseModel):
    id: str
    name: Optional[str] = None
    creator: Optional[str] = None
    category: Optional[str] = None
    introductions: Optional[str] = None
    usage: Optional[int] = 0
    total_usage: Optional[int] = 0
    ratio: Optional[float] = 0.1
    collect: Optional[float] = 0

    class Config:
        from_attributes = True

class AITableCreate(BaseModel):
    name: Optional[str] = None
    creator: Optional[str] = None
    category: Optional[str] = None
    introductions: Optional[str] = None
    contents: Optional[str] = None
    logs: Optional[str] = None

class AITableUserUpdateInput(BaseModel):
    category: Optional[str] = None
    introductions: Optional[str] = None
    contents: Optional[str] = None
    logs: Optional[str] = None

class AITableUserUpdate(BaseModel):
    category: Optional[str] = None
    introductions: Optional[str] = None
    contents: Optional[str] = None
    logs: Optional[str] = None

class AITableUsageUpdate(BaseModel):
    usage: Optional[int] = 0
    total_usage: Optional[int] = 0
    collect: Optional[float] = 0

class AITableCollectUpdate(BaseModel):
    collect: Optional[float] = 0

class AITableInDB(AITableBase):
    pass

class AITableOut(AITableInDB):
    pass

class AITableListOut(BaseModel):
    ais: List[AITableBase]

    class Config:
        from_attributes = True

# AILogTable 스키마
class AILogTableBase(BaseModel):
    id: int
    aiid: Optional[str] = None
    createdat: Optional[time] = None
    log: Optional[str] = None
    txurl: Optional[str] = None
    faissid: Optional[str] = None
    

class AILogTableCreate(BaseModel):
    aiid: Optional[str] = None
    log: Optional[str] = None
    txurl: Optional[str] = None
    faissid: Optional[str] = None

class AILogTableUpdate(AILogTableBase):
    pass

class AILogTableInDB(AILogTableBase):
    pass

class AILogTableOut(AILogTableInDB):
    class Config:
        from_attributes = True

class AILogTableListOut(BaseModel):
    logs: List[AILogTableOut]

    class Config:
        from_attributes = True
# ChatTable 스키마
class ChatTableBase(BaseModel):
    chatid: str
    aiid: Optional[str] = None
    userid: Optional[str] = None
    
    class Config:
        from_attributes = True

class ChatTableCreate(BaseModel):
    aiid: Optional[str] = None
    userid: Optional[str] = None

class ChatTableUpdate(ChatTableBase):
    pass

class ChatTableInDB(ChatTableBase):
    pass

class ChatTableOut(ChatTableInDB):
    pass

class ChatTableListOut(BaseModel):
    chats: List[ChatTableBase]

    class Config:
        from_attributes = True

# ChatContentsTable 스키마
class ChatContentsTableBase(BaseModel):
    chatcontentsid: str
    chatid: Optional[str] = None
    createdat: Optional[time] = None
    senderid: Optional[str] = None
    message: Optional[str] = None
    class Config:
        from_attributes = True

class ChatContentsTableCreateInput(BaseModel):
    senderid: Optional[str] = None
    message: Optional[str] = None

class ChatContentsTableCreate(BaseModel):
    chatcontentsid: str
    chatid: Optional[str] = None
    senderid: Optional[str] = None
    message: Optional[str] = None

class ChatContentsTableUpdate(ChatContentsTableBase):
    pass

class ChatContentsTableInDB(ChatContentsTableBase):
    pass

class ChatContentsTableOut(ChatContentsTableInDB):
    pass

class ChatContentsTableListOut(BaseModel):
    chats: List[ChatContentsTableBase]

    class Config:
        from_attributes = True
