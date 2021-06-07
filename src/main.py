from Object import Object
from Scene import Scene

if __name__ == '__main__':
    s = Scene()

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj')
    s.add_object(obj1)

    obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj')
    s.add_object(obj2)
