"""
Example 1. Drawing a teapot from multiple viewpoints.
"""
import os
import argparse

import torch
import numpy as np
import tqdm
import imageio

import neural_renderer as nr

bVerbose = True

current_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(current_dir, 'data')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--filename_input', type=str, default=os.path.join(data_dir, 'teapot.obj'))
    parser.add_argument('-o', '--filename_output', type=str, default=os.path.join(data_dir, 'example1.gif'))
    parser.add_argument('-g', '--gpu', type=int, default=0)
    args = parser.parse_args()

    # other settings
    camera_distance = 2.732
    elevation = 30
    texture_size = 2

    # load .obj
    vertices, faces = nr.load_obj(args.filename_input)
    vertices = vertices[None, :, :]  # [num_vertices, XYZ] -> [batch_size=1, num_vertices, XYZ]
    faces = faces[None, :, :]  # [num_faces, 3] -> [batch_size=1, num_faces, 3]

    # create texture [batch_size=1, num_faces, texture_size, texture_size, texture_size, RGB]
    textures = torch.ones(1, faces.shape[1], texture_size, texture_size, texture_size, 3, dtype=torch.float32).cuda()

    # to gpu

    # create renderer
    if bVerbose:
        print('100')
        pass
    renderer = nr.Renderer(camera_mode='look_at')
    if bVerbose:
        print('101');
        pass

    # draw object
    # loop = tqdm.tqdm(range(0, 360, 4))
    loop = range(0, 4, 4)
    writer = imageio.get_writer(args.filename_output, mode='I')
    if bVerbose:
        # print(f'type(writer): {type(writer)}')
        pass
    for num, azimuth in enumerate(loop):
        # loop.set_description('Drawing')
        renderer.eye = nr.get_points_from_angles(camera_distance, elevation, azimuth)
        if bVerbose:
            pass
            # print(f'renderer.eye: {renderer.eye}')
        if bVerbose:
            print('102');
            pass
        # 4/29/2023 6:06:05 PM: multiply vertices, faces, and textures by scalar: start
        # vertices = torch.mul(vertices,.5)
        # faces = torch.mul(faces,.1)
        textures = torch.mul(textures,.1)
        # 4/29/2023 6:06:05 PM: multiply vertices, faces, and textures by scalar: end
        images, _, _ = renderer(vertices, faces, textures)  # [batch_size, RGB, image_size, image_size]
        if bVerbose:
            print('103');
            pass
        image = images.detach().cpu().numpy()[0].transpose((1, 2, 0))  # [image_size, image_size, RGB]
        writer.append_data((255*image).astype(np.uint8))
    writer.close()

if __name__ == '__main__':
    main()
