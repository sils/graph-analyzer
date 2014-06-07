# Copyright 2014 by Lasse Schuirmann, License: GPL v3

from mpl_toolkits.axisartist.axis_artist import UnimplementedException

class RawGraph:
    def __init__(self):
        self.knot_count = 0
        self.knots = {}

    def from_file(self, filename):
        with open(filename, 'r') as file:
            for i, line in enumerate(file):
                if i == 0:
                    self.knot_count = int(line)
                else:
                    self.__parse_line(i, line)

    def __parse_line(self, line_number, line):
        arr = []
        numbers = line.strip().split(',')
        for elem in numbers:
            if elem:
                arr.append(int(elem))
        self.knots[line_number] = arr

    def get_connected_components(self):
        done_knots = []
        result = []
        for key, val in self.knots.items():
            if key in done_knots:
                continue
            tmp = self.__get_connected(key)
            for elem in tmp:
                done_knots.append(elem)
            result.append(tmp)
        return result

    def __get_connected(self, key, res=None):
        if res is None:
            res = []
        if key in res:
            return res

        res.append(key)
        for elem in self.knots[key]:
            if elem in res:
                continue
            res = self.__get_connected(elem, res)

        return res

    def is_two_colorizable(self, components):
        for component in components:
            if len(component) < 3:
                continue
            col1=[]
            col2=[]
            res = self.__colorize(col1, col2, component[0])
            if not res:
                return False
        return True

    def __colorize(self, col1, col2, key):
        if key in col1:
            return True
        if key in col2:
            return False
        col1.append(key)
        for elem in self.knots[key]:
            res = self.__colorize(col2, col1, elem)
            if not res:
                return False
        return True

    def get_distance(self, v, w, components):
        for component in components:
            if v in component:
                if w not in component:
                    return -1

        dist = -1
        vs = [[v]]
        d = 0
        while dist == -1:
            [dist, vs, d] = self.__minimal_distance(vs, w, d)
        return d

    def __minimal_distance(self, vs, w, dist):
        newvs = []
        for elem in (vs[-1]):
            if elem == w:
                return [1, vs, dist]
            val = self.knots[elem]
            for el in val:
                init = False
                for hist in vs:
                    if el in hist:
                        init=True
                if not init:
                    newvs.append(el)
        vs.append(newvs)
        return [-1, vs, dist+1]



    def lonely_knot_count(self):
        count = 0
        for val in self.knots.values():
            if self.__is_lonely(val):
                count += 1
        return count

    def maximum_degree(self):
        maxdeg = 0
        for key, val in self.knots.items():
            maxdeg = max(maxdeg, self.__degree(key, val))
        return maxdeg

    def __is_lonely(self, val):
        return len(val) == 0

    def __degree(self, key, knot):
        res = 0
        for elem in knot:
            if int(elem) == int(key):
                print("Warning: found self reference!")
                res += 2
            else:
                res += 1
        return res
