from heapq import heappush, heappop


class Graph:
    @staticmethod
    def build_route(order):
        path, sum_cost = find_best_path(order.from_location, order.to_location)

        if path is None or sum_cost > order.max_cost:
            order.route = None
        else:
            order.route = Route(edges=path, active_edge_index=0)


    @staticmethod
    def find_best_path(self, from_location, to_location):
        best_path_to = {}
        dist_heap = [(0, from_location, None)]

         while len(dist_heap) > 0:
            cost, cur_location, best_last_edge = heappop(dist_heap)
            if cur_location.id in best_path_to:
                pass
            best_path_to[cur_location.id] = best_last_edge
            if cur_location == to_location:
                break
            for edge in Edge.objects.filter(start_location=cur_location):
                if edge.end_location.id in best_path_to:
                    continue
                if edge.cost:
                    heappush(heap, (cost + edge.cost,
                        edge.end_location, edge))
        else:
            return None, None

        path = []
        cur = to_location
        sum_cost = 0
        while cur != from_location:
            edge = came_from[cur.id]
            path.append(edge)
            sum_cost += edge.cost
            cur = edge.start_location
        return reversed(edges), sum_cost
