from typing import List
from schemas import NodalRequest, NodalResponse, VlpIprData
from shapely.geometry import LineString


def __convert_dict_to_linestring_form(data: VlpIprData) -> LineString:
    converted_form = [[p_wf, q_liq] for p_wf, q_liq in zip(data.p_wf, data.q_liq)]
    return LineString(converted_form)


async def calculate_intersection_points(
    nodes_data: NodalRequest,
) -> List[NodalResponse]:
    vlp_nodes = __convert_dict_to_linestring_form(nodes_data.vlp)
    ipr_nodes = __convert_dict_to_linestring_form(nodes_data.ipr)
    intersection_nodes = list(vlp_nodes.intersection(ipr_nodes).convex_hull.coords)

    return [NodalResponse(p_wf=p_wf, q_liq=q_liq) for p_wf, q_liq in intersection_nodes]
