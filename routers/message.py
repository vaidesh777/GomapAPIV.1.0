import random
import string
from typing import Optional



# from schemas import city
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



import database
from models import MessageModels
from schemas import MessageSchemas

router = APIRouter()
@router.get('messages')
def all_messages(db: Session = Depends(database.get_db)):
    messageObj = db.query(MessageModels.message).all()
    return {'all reords displayed'}


@router.post('/messages')
async def message(request_message: MessageSchemas.message, db: Session = Depends(database.get_db)):
    messageObj = MessageModels.City(id=request_message.id,
                                    device=request_message.device,
                                    groups=request_message.groups,
                                    message_id=request_message.message_id,
                                    message=request_message.message,
                                    images=request_message.images,
                                    schedule=request_message.schedule,
                                    status=request_message.status,
                                    created=request_message.created,

                                    )
    db.add(messageObj)
    db.commit()
    return messageObj


