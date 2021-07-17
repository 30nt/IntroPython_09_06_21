import random

MIN_LIMIT = -1
MAX_LIMIT = 1


def create_point(min_limit: int = MIN_LIMIT, max_limit=MAX_LIMIT) -> dict:
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name_str: str) -> dict:
    return {key: create_point() for key in points_name_str}


def print_triangles_list(triangles_list: list) -> None:
    print("-----------------------------------------------------------------")
    for triangle in triangles_list:
        print(triangle)
    print("-----------------------------------------------------------------")


















triangles_list = []
names = ["ABC", "MNK", "QWE", "ZSD"]
for name in names:
    triangle = create_triangle(name)
    triangles_list.append(triangle)
print_triangles_list(triangles_list)

# triangle_ABC = create_triangle("ABC")
# triangle_MNK = create_triangle("MNK")
# triangle_QWE = create_triangle("QWE")
#
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)
