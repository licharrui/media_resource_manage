import os
from fastapi import APIRouter, File, UploadFile
from travel_of_the_life.config import CONFIG

from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/media_resource",
    tags=["media_resource"],
    responses={404: {"description": "Not found"}},
)


@router.post("/list/{resource_type}")
async def resource_upload(file: UploadFile = File(...), resource_type: str = "image"):
    """
    上传资源
    """
    if file is None:
        return JSONResponse(
            {"code": 400, "msg": "请上传文件", "data": None}, status_code=400
        )
    match resource_type:
        case "image":
            resource_dir = CONFIG.media_resource.image_dir
        case "video":
            resource_dir = CONFIG.media_resource.video_dir
        case "audio":
            resource_dir = CONFIG.media_resource.audio_dir
        case "document":
            resource_dir = CONFIG.media_resource.document_dir
        case _:
            return JSONResponse(
                {"code": 400, "msg": "资源类型错误", "data": None}, status_code=400
            )

    save_path = os.path.join(CONFIG.media_resource.dir_name, resource_dir)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    save_file = os.path.join(save_path, file.filename)

    with open(save_file, "wb") as f:
        f.write(file.file.read())

    return JSONResponse(
        {
            "code": 200,
            "message": "上传成功",
            "data": {
                "file": f"{CONFIG.media_resource.dir_name}/{resource_dir}/{file.filename}"
            },
        },
        status_code=200,
    )
