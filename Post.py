from conexao_orm import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    authorId = Column(Integer, ForeignKey('author'))
    posts = relationship('Post', back_populates='author')
    
    def __init__(self, title, content, author ):
        self.title = title
        self.content = content
        self.author = author