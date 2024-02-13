from typing import List
from fastapi import APIRouter, Body
from schemas import NodalRequest, NodalResponse
from controllers import nodal_analysis as nodal_analysis_controller

router = APIRouter(prefix="/nodal_analysis", tags=["nodal_analysis_service"])


@router.post("", response_model=List[NodalResponse])
async def calculate_intersection_points(
    nodes_data: NodalRequest = Body(...),
):
    """
    Вычисляет точки пересечения двух кривых
    """
    return await nodal_analysis_controller.calculate_intersection_points(
        nodes_data=nodes_data
    )
