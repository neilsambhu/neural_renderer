# Neural Renderer
4/25/2023 12:31:30 PM: TODO: run example1.py  
4/25/2023 4:13:40 PM: I am unable to install PyTorch 0.4.0. I tried to install PyTorch 2.0.0 `conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia`. I was unable to install neural_renderer_pytorch using `pip install neural_renderer_pytorch`. TODO: run example1.py using dualattentionattack environment.  
4/25/2023 4:17:44 PM: TODO: make a copy of conda environment dualattentionattack.  
4/25/2023 4:26:10 PM: environment works.  
4/26/2023 12:27:27 PM: running example1.py outputs `examples/data/example1.gif`. TODO: export single frame.  
4/27/2023 11:49:52 AM: command for example.py
```
python examples/example1.py --filename_input examples/data/audi_et_te.obj --filename_output examples/data/example1-02.gif |& tee out.txt
```
4/27/2023 12:36:01 PM: VS Code on SAMBHU20 gives me the source code when I right click the "Renderer" constructor; SAMBHU15 does not. TODO: grep to find "Renderer" constructor. 
```
grep -r --exclude-dir=timeline --exclude *README.md --exclude outgrep.txt -e "Renderer(" |& tee outgrep.txt
```
```
neural_renderer/renderer.py:class Renderer(nn.Module):
```
4/27/2023 12:58:03 PM: `example1.py renderer = nr.Renderer(camera_mode='look_at')` does not call `renderer.py`  
4/27/2023 1:00:39 PM: TODO: grep to find parameter "camera_mode" of Renderer constructor. 
```
grep -r --exclude-dir=timeline --exclude *README.md --exclude outgrep.txt -e "camera_mode" |& tee outgrep.txt
```
4/27/2023 1:36:07 PM: find source file of neural_renderer
```
(neural_renderer_from_DAS) [nsambhu@localhost github]$ python
Python 3.7.13 (default, Mar 29 2022, 02:18:16) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import neural_renderer
>>> import inspect
>>> inspect.getfile(neural_renderer)
'/home/nsambhu/anaconda3/envs/neural_renderer_from_DAS/lib/python3.7/site-packages/neural_renderer/__init__.py'
>>> inspect.getsourcefile(neural_renderer)
'/home/nsambhu/anaconda3/envs/neural_renderer_from_DAS/lib/python3.7/site-packages/neural_renderer/__init__.py'
```
4/28/2023 4:18:45 PM: TODO: find `example1.py renderer(vertices, faces, textures)` function call in `/home/nsambhu/anaconda3/envs/neural_renderer_from_DAS/lib/python3.7/site-packages/neural_renderer/renderer.py`  
4/28/2023 4:29:41 PM: TODO: in `/home/nsambhu/anaconda3/envs/neural_renderer_from_DAS/lib/python3.7/site-packages/neural_renderer/renderer.py`,  print parameters of `def render(self, vertices, faces, textures, K=None, R=None, t=None, dist_coeffs=None, orig_size=None):`  
4/29/2023 5:51:32 PM: input parameters
```
vertices: tensor([[[-0.7776,  0.3186,  0.1152],
         [-0.7831,  0.2075,  0.1097],
         [-0.7725,  0.3181,  0.1123],
         ...,
         [-0.7480, -0.1746,  0.2385],
         [-0.7616, -0.2010,  0.2161],
         [-0.7448, -0.1904,  0.2323]]], device='cuda:0')
faces: tensor([[[    0,     1,     2],
         [    1,     0,     3],
         [    4,     3,     0],
         ...,
         [ 7660, 13447, 13445],
         [13446, 13445, 13448],
         [13448, 13445, 13447]]], device='cuda:0', dtype=torch.int32)
textures: tensor([[[[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]],



         [[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]],



         [[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]],



         ...,



         [[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]],



         [[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]],



         [[[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]],


          [[[1., 1., 1.],
            [1., 1., 1.]],

           [[1., 1., 1.],
            [1., 1., 1.]]]]]], device='cuda:0')
```
```
vertices.shape: torch.Size([1, 13449, 3])
faces.shape: torch.Size([1, 23145, 3])
textures.shape: torch.Size([1, 23145, 2, 2, 2, 3])
```
4/29/2023 6:10:08 PM: `vertices` affects the zoom in or out from the object.  
4/29/2023 6:11:49 PM: `faces` affects the quality of the curves of the object (i.e. smaller values result in a lower quality render).  
4/29/2023 6:13:36 PM: `textures` affects the contrast in the appearance of the object (i.e. smaller values result in a light gray render; larger values result in a black-and-white render).  
4/29/2023 8:04:12 PM: `elevation` affects rotation like a gas station hot dog. `azimuth` affects rotation like a toy top.  