from utils import Grid
from .gridmap import GridMap
from .base_object import BaseObject, EmptyObject
from queue import PriorityQueue
from dataclasses import dataclass


@dataclass
class Node:
    row: int
    col: int
    parent: object = None
    g: int = 0
    h: int = 0
    f: int = 0

    def __repr__(self):
        return f'[{self.row:2}, {self.col:2}] F: {self.f} G: {self.g} H: {self.h}'

    def __eq__(self, other):
        other_t = type(other)
        if other_t is Grid or other_t is Node:
            return other.row == self.row and other.col == self.col
        return False

    def __hash__(self):
        return hash(f'{self.row}{self.col}')

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def __ne__(self, other):
        return self.f != other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f


class PathFinder:

    COST_DIAGONAL = 14
    COST_STRAIGHT = 10

    def __init__(self):
        self.gridmap: GridMap = None
        self.src: Grid = None
        self.dst: Grid = None

    def _get_distance(self, src: Grid, dst: Grid) -> int:
        dr = abs(src.row - dst.row)
        dc = abs(src.col - dst.col)

        straight = abs(dr - dc)
        diagonal = max(dr, dc) - straight

        distance = diagonal * PathFinder.COST_DIAGONAL
        distance += straight * PathFinder.COST_STRAIGHT
        return distance

    def _make_node(self, grid: Grid, parent: Node = None,
                   cost: int = 0) -> Node:

        distance_to_dst = self._get_distance(grid, self.dst)

        if parent is None:
            distance_to_src = self._get_distance(grid, self.src)
        else:
            distance_to_src = parent.G + cost

        return Node(
                g=distance_to_src,
                h=distance_to_dst,
                f=distance_to_src + distance_to_dst,
                row=grid.row,
                col=grid.col,
                parent=parent
            )

    def _get_neighbours(self, node: Node) -> list:
        end = len(self.gridmap)
        nodes = []

        for row in range(node.row-1, node.row+2):
            for col in range(node.col-1, node.col+2):
                grid = Grid(row, col)

                if (row < 0 or row >= end or col < 0 or col >= end
                   or (row == node.row and col == node.col)):
                    continue

                if self._is_traversable(grid):
                    new_node = Node(row, col, node)
                    nodes.append(new_node)

        return nodes

    def _is_traversable(self, grid: Grid) -> bool:
        return self.gridmap[grid.row, grid.col] == 0

    def _get_from_queue(self, queue: PriorityQueue, node: Node) -> Node:
        for n in queue.queue:
            if n == node:
                return n

    def _less_than(self, old_n: Node, new_n: Node) -> bool:
        if old_n is None:
            return False
        return old_n < new_n

    def _build_path(self, end_node: Node) -> list:
        path = []
        node = end_node
        while node.parent is not None:
            path.append(node)
            node = node.parent
        return path

    def find(self, gridmap: GridMap, src: Grid, dst: Grid) -> list:
        """ Finds a path from src to dst grid on the map.
            This methods uses A* to find the shortest path.

            Returns None if no path can be found.
        """
        self.gridmap = gridmap
        self.src = src
        self.dst = dst

        if not self._is_traversable(dst):
            return None

        opened = PriorityQueue()
        opened.put(Node(src.row, src.col))
        closed = set()
        found_path = False

        while not opened.empty():
            curr_node = opened.get()

            if curr_node.row == dst.row and curr_node.col == dst.col:
                found_path = True
                break

            for neighbour in self._get_neighbours(curr_node):

                if neighbour in closed:
                    continue

                old_n = self._get_from_queue(opened, neighbour)

                if (self._less_than(old_n, neighbour)
                   or neighbour not in opened.queue):

                    neighbour.g = neighbour.parent.g
                    neighbour.g += self._get_distance(neighbour,
                                                      neighbour.parent)
                    neighbour.h = self._get_distance(neighbour, self.dst)
                    neighbour.f = neighbour.g + neighbour.h

                    if neighbour not in opened.queue:
                        opened.put(neighbour)

            closed.add(curr_node)

        if found_path:
            return self._build_path(curr_node)
        else:
            return None
