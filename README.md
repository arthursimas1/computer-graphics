# computer-graphics
Some experiments about computer graphics.

It implements a Camera, Object, Scene and some transformation functions. The Camera windowing system is based on
wxPython.

<p align="center">
  <img src="static/demo-screenshot.png" width="40%">
  <br><em>Demo using two scenes, Scene 1 with two cameras and Scene 2 with just one camera.</em>
</p>

## requirements.txt:
- [numpy==1.20](https://pypi.org/project/numpy/1.20.0/): uses `np.array`, `np.full` and `p.matmul`;
- [webcolors==1.11](https://pypi.org/project/webcolors/1.11/): converts HEX code to RGB;
- [wxPython==4.1](https://pypi.org/project/wxPython/4.1.0/): windowing system which provides a bitmap canvas to freely
  draw.

## Installation

Usually one can just run the following command and get it ready:

```shell
$ pip3 install -r requirements.txt
```

But if you encounter any error, it probably might be related to *wxPython*, as there's no wheels available for each 
platform. Some alternatives are using conda/anaconda distribution, 

## Usage

Usage as in [src/main.py](src/main.py):

```python3
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
    cam1.translate(-100, -100, 0)

    cam2 = Camera(s1)
    cam2.translate(-100, -100, 0)

    cam3 = Camera(s2)
    cam3.translate(-100, -100, 10)

    Scene.main_loop()
```

It can be simply run as `python3 src/main.py`. To terminate the execution you can close all windows one by one or hit 
`CTRL + C` on the terminal.

You can interact with each Camera using the following commands:
- `RIGHT`: right (`translate(C, 0, 0)`)
- `LEFT`: left (`translate(-C, 0, 0)`)
- `UP`: front (`translate(0, 0, C)`)
- `DOWN`: back (`translate(0, 0, -C)`)
- `SHIFT + UP`: up (`translate(0, C, 0)`)
- `SHIFT + DOWN`: down (`translate(0, -C, 0)`)
- `CTRL + RIGHT`: positive pitch (`rotate_y(D)`)
- `CTRL + LEFT`: negative pitch (`rotate_y(-D)`)
- `CTRL + UP`: positive roll (`rotate_x(D)`)
- `CTRL + DOWN`: negative roll (`rotate_x(-D)`)
- `CTRL + SHIFT + RIGHT`: positive yaw (`rotate_z(D)`)
- `CTRL + SHIFT + LEFT`: negative yaw (`rotate_z(-D)`)

## TODO
- [x] Reading at least one 3D object
- [x] Resizing and positioning of the objects in a virtual scene
- [x] Camera
- [ ] Z-buffer
- [ ] Projection
- [ ] Object rendering (currently draws vertexes instead of the faces)
- [x] Export or view the rendered scene
- [ ] Define at least one light source
- [ ] Implement *Phong* and/or *Gouraud* shading techniques
- [ ] Export docstrings to Markdown documentation
