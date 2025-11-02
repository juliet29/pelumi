from polymap.layout.interfaces import create_layout_from_json
from pelumi.paths import DynamicPaths
from rich import print
from polymap.layout.interfaces import Layout
from replan2eplus.ops.zones.user_interface import Room
from replan2eplus.geometry.ortho_domain import OrthoDomain
from replan2eplus.ezcase.ez import EZ
import matplotlib.pyplot as plt

HEIGHT = 3  # m

if __name__ == "__main__":
    path = DynamicPaths.init_data
    layout: Layout = create_layout_from_json(path.stem, folder_path=path.parent)
    layout.domains = [i for i in layout.domains if len(i.coords) >= 4]
    coords = [i.normalized_coords for i in layout.domains]
    sorted_data = sorted(layout.domains, key=lambda x: x.shapely_polygon.bounds[0])

    # layout.plot_layout()
    # plt.show()

    # print([len(i.coords) for i in layout.domains])
    print(sorted_data)
    # rooms = [
    #     Room(id=int(i.name), name=i.name, domain=OrthoDomain(i.coords), height=3)  # pyright: ignore[reportArgumentType]
    #     for i in res.domains
    # ]
    # # print(rooms)
    # case = EZ().add_zones(rooms)
    # print(case)
