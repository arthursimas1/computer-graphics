class Object:
    def __init__(self, path: str):
        self.vertexes = []
        self.faces = []
        with open(path, 'r') as fp:
            for line in fp.readlines():
                line_type, *elements = line.split()

                if line_type == 'v':
                    self.vertexes.append(list(map(float, elements)))
                elif line_type == 'f':
                    self.faces.append(list(map(lambda x: int(x) - 1, elements)))
