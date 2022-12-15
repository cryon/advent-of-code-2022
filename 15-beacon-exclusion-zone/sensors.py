import re
from collections import namedtuple as nt

from util import lines

INF = 10_000_000

Point = nt("Point", "x y")
Sensor = nt("Sensor", "position radius")


def parse_input(path):
    sensor_circles = set()
    for line in lines(path):
        matches = re.findall("-?\\d+", line)
        center = Point(int(matches[0]), int(matches[1]))
        radius = abs(center.x - int(matches[2])) + abs(center.y - int(matches[3]))
        sensor_circles.add(Sensor(center, radius))
    return sensor_circles


def sensor_range_on_line(sensor, y):
    distance = abs(y - sensor.position.y)
    if distance > sensor.radius: return None
    return sensor.position.x - (sensor.radius - distance), sensor.position.x + (sensor.radius - distance)


def merge_ranges(ranges, limit=None):
    merged = []
    ranges.sort(key=lambda r: r[0])
    for r in ranges:
        if limit:
            if r[1] < limit[0] or r[0] > limit[1]:
                continue
            r = max(limit[0], r[0]), min(limit[1], r[1])
        if not merged or merged[-1][1] < r[0]:
            merged.append(r)
        else:
            merged[-1] = merged[-1][0], max(merged[-1][1], r[1])
    return merged


if __name__ == "__main__":
    sensors = parse_input("input")

    part1_ranges = [r for r in [sensor_range_on_line(s, y=2000000) for s in sensors] if r]
    part1_merged = merge_ranges(part1_ranges).pop()
    print(f"Part 1: {part1_merged[1] - part1_merged[0]}")

    for y in range(4000000):
        ranges = [r for r in [sensor_range_on_line(s, y=y) for s in sensors] if r]
        ranges_merged = merge_ranges(ranges, limit=(0, 4000000))
        if len(ranges_merged) > 1:
            print(f"Part 2: {(ranges_merged[0][1] + 1) * 4000000 + y}")
            break
