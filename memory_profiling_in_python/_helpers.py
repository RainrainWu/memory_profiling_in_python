from inspect import FrameInfo
from typing import Iterable


def view_frames(frame_infos: Iterable[FrameInfo]) -> None:

    for _ in map(view_frame, frame_infos): pass


def view_frame(frame_info: FrameInfo) -> None:

    arrange_code_context = lambda code_context: (
        "".join(f"\t\t{ctx}" for ctx in code_context)
    )

    print(
        (
            f"[ {frame_info.function} ]\n\n"
            f"\tfilename: {frame_info.filename}\n"
            f"\tposition: {frame_info.positions}\n"
            f"\tcontext:\n"
            f"{arrange_code_context(frame_info.code_context)}\n"
        )
    )