from Camera import Camera
from Object import Object
from Scene import Scene

if __name__ == '__main__':
    s1 = Scene()
    s2 = Scene()

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj')
    obj1.translate(1, 0, 0)
    obj1.scale(50)
    s1.add_object(obj1)

    obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj')
    obj2.translate(2, -1, 0)
    obj2.scale(50)
    obj2.rotate_y(-45)
    s1.add_object(obj2)

    obj3 = Object('./3d-obj-examples/coarseTri.rockerArm.obj')
    obj3.scale(50)
    obj3.rotate_y(60)
    s2.add_object(obj3)

    cam1 = Camera(s1)
    cam1.rotate_y(45)
    cam1.rotate_z(45)
    cam1.translate(-150, 100, 0)

    cam2 = Camera(s1)
    cam2.translate(100, 0, 0)

    cam3 = Camera(s2)
    cam3.translate(-150, -100, 10)

    Scene.main_loop()
