from typing import List
from pydantic import BaseModel, Field, field_validator


class VlpIprData(BaseModel):
    """
    Схема для валидации данных Vlp и Ipr кривых
    """

    p_wf: List[float] = Field(title="Забойные давления, атм")
    q_liq: List[float] = Field(title="Дебиты жидкости, м3/сут")

    @field_validator("p_wf", "q_liq")
    def check_positive_numbers(cls, v, values, **kwargs):
        for node in v:
            if node < 0:
                raise ValueError("Числа должны быть больше 0")
        return v


class NodalRequest(BaseModel):
    """
    Схема для валидации запроса на нахождение точек пересечения Vlp и Ipr кривых
    """

    vlp: VlpIprData = Field(title="VLP")
    ipr: VlpIprData = Field(title="IPR")

    model_config = {
        "json_schema_extra": {
            "example": {
                "vlp": {
                    "p_wf": [200, 190, 185, 180, 175, 185, 200],
                    "q_liq": [0, 30, 45, 60, 90, 120, 150],
                },
                "ipr": {
                    "p_wf": [200, 180, 180, 180, 140, 120, 100],
                    "q_liq": [0, 30, 45, 60, 90, 120, 150],
                },
            }
        }
    }


class NodalResponse(BaseModel):
    """
    Схема для валидации точек пересечения Vlp и Ipr кривых
    """

    p_wf: float = Field(title="Забойные давления, атм", ge=0)
    q_liq: float = Field(title="Дебиты жидкости, м3/сут", ge=0)

    model_config = {"json_schema_extra": {"example": {"p_wf": 200, "q_liq": 0}}}
