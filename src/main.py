from Camera import Camera
from Object import Object
from Scene import Scene
from LightSource import LightSource

if __name__ == '__main__':
    s1 = Scene(.1)
    s2 = Scene(.4)

    ls1 = LightSource([5_000., 5_000., -5_000.], 1.)
    s1.add_light_source(ls1)

    ls2 = LightSource([5_000., 5_000., -5_000.], 1.)
    ls3 = LightSource([-5_000., -5_000., -5_000.], .3)
    s2.add_light_source(ls2)
    s2.add_light_source(ls3)

    obj1 = Object('./3d-obj-examples/coarseTri.fandiskAuto.obj', '#4070a0')
    obj1.translate(-0.5, 0, 0)
    obj1.scale(200)
    s1.add_object(obj1)

    obj2 = Object('./3d-obj-examples/coarseTri.egea1.obj', '#e74c3c', .7, 1., 5)
    obj2.translate(0.5, 0, 0)
    obj2.scale(200)
    s1.add_object(obj2)

    obj3 = Object('./3d-obj-examples/coarseTri.rockerArm.obj', '#208050', .3, 1., 5)
    obj3.scale(200)
    obj3.rotate_y(90)
    obj3.rotate_x(30)
    s2.add_object(obj3)

    cam1 = Camera(s1)
    cam1.rotate_y(-50)
    cam1.rotate_x(20)

    cam2 = Camera(s1)
    cam2.rotate_x(20)

    cam3 = Camera(s2)

    Scene.main_loop()
