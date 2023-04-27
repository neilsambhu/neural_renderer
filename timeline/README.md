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