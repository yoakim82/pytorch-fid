
from pytorch_fid.fid_score import fid, fid_single


def paths():
    a = ["/data/synthetic_cs/world_0_cars_1/out_rgb", "/data/synthetic_cs/world_0_cars_2/out_rgb",
         "/data/synthetic_cs/world_0_cars_3/out_rgb", "/data/synthetic_cs/world_0_cars_4/out_rgb"]
    b = ["/data/synthetic_cs/world_1_cars_1/out_rgb", "/data/synthetic_cs/world_1_cars_2/out_rgb",
         "/data/synthetic_cs/world_1_cars_3/out_rgb", "/data/synthetic_cs/world_1_cars_4/out_rgb"]

    val = fid([a, b])

    print(f"Fid: {val}")


def tests():
    a = ["/data/synthetic_cs/world_0_cars_1/out_rgb"]
    b = ["/data/synthetic_cs/world_1_cars_1/out_rgb"]
    val = fid([a, b])
    print(f"Fid: {val}")

    val2 = fid_single([a[0], b[0]])
    print(f"Fid: {val}, fid_single: {val2}")


def test2():
    a = ["/data/synthetic_cs/world_0_cars_1/out_rgb"]
    b = ["/data/synthetic_cs/world_1_cars_1/out_rgb", "/data/synthetic_cs/world_1_cars_2/out_rgb"]
    val = fid([a, b])
    print(f"Fid: {val}")

    val2 = fid_single([a[0], b[0]])
    val3 = fid_single([a[0], b[1]])
    avg = (val2+val3)/2
    print(f"Fid: {val}, fid_single 1: {val2}, fid_single 2: {val3}, average: {avg}")



test2()
