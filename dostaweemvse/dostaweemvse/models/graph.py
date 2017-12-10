from heapq import heappush, heappop


class Graph:
    @staticmethod
    def build_route(order):
        from_id = order.from_id
        to_id = order.to_id

        path = find_path(from_id, to_id)

        if path is None:
            order.route_id = None
        else:
            # TODO


    @staticmethod
    def find_path(self, from_location, to_location):
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
            return None

        path = []
        cur = to_location
        while cur != from_location:
            edge = came_from[cur.id]
            path.append(edge)
            cur = edge.start_location
        return reversed(edges)
