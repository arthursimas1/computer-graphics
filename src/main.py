from Camera import Camera
from Object import Object
from Scene import Scene

if __name__ == '__main__':
    s1 = Scene()
    s2 = Scene()

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj', '#4070a0')
    obj1.translate(-0.5, 0, 0)
    obj1.scale(100)
    s1.add_object(obj1)

    obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj', '#e74c3c')
    obj2.translate(0.5, 0, 0)
    obj2.scale(100)
    s1.add_object(obj2)

    obj3 = Object('./3d-obj-examples/coarseTri.rockerArm.obj', '#208050')
    obj3.scale(100)
    obj3.rotate_y(90)
    obj3.rotate_x(30)
    s2.add_object(obj3)

    cam1 = Camera(s1)
    cam1.rotate_y(45)
    cam1.rotate_z(45)
    #cam1.translate(-100, -100, 0)

    cam2 = Camera(s1)
    cam2.translate(-100, -100, 0)

    cam3 = Camera(s2)
    cam3.translate(-100, -100, 10)

    Scene.main_loop()
