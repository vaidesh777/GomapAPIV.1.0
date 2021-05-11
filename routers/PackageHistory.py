from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



import database
from models import PackageHistoryModels
from schemas import PackageHistorySchemas

router = APIRouter()
@router.get('/packagehistory')
def all_messages(db: Session = Depends(database.get_db)):
    packagehistoryObj = db.query(PackageHistoryModels.packagehistory).all()
    return {'all reords displayed'}


@router.post('/packagehistory')
async def message(request_history: PackageHistorySchemas., db: Session = Depends(database.get_db)):
    packagehistoryObj = PackageHistoryModels.packagehistory(id=request_history.id,
                                    builder_id=request_history.device,
                                    package_id=request_history.groups,
                                    start_date=request_history.message_id,
                                    end_date=request_history.message,
                                    price=request_history.images,
                                    extra=request_history.schedule,
                                    extras=request_history.status,


                                    )
    db.add(packagehistoryObj)
    db.commit()
    return packagehistoryObj


