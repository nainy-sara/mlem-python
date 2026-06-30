
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon, rescale

import matplotlib.pyplot as plt
import numpy as np


plt.ion()

true_object = shepp_logan_phantom();
true_object = rescale(true_object, 0.5)


fig, axs = plt.subplots(2, 3, figsize = (20 , 10))

axs[0,0].imshow(true_object, cmap='Greys_r');     axs[0,0].set_title("object")

azi_angle = np.linspace(0.0, 180, 180, endpoint=False)
sinogram = radon(true_object, azi_angle, circle =False)

axs[0,1].imshow(sinogram.T, cmap="Greys_r");    axs[0,1].set_title("sinogram")
#

#filter back projection:
#measure_data=iradon(sinogram, theta=azi_angle, filter_name='ramp')
#axs[0,2].imshow(measure_data, cmap="Greys_r");    axs[0,2].set_title("measure_data")
#plt.show(block = True)

# mlem iterative filter

mlem_rec = np.ones(true_object.shape); #iteration = 0
sino_one = np.ones(sinogram.shape);
sens_image = iradon(sino_one, azi_angle, circle=False, filter_name=None) 
for iter in range(20):
    fp = radon(mlem_rec, azi_angle,circle=False)
    ratio = sinogram / (fp + 0.0000001)
    coreation = iradon(ratio, azi_angle, circle=False, filter_name=None)/sens_image
    axs[1,1].imshow(fp.T, cmap="Greys_r");    axs[1,1].set_title("fp of recon")
    axs[0,2].imshow(ratio.T, cmap="Greys_r");    axs[0,2].set_title("ratio sinogram")
    axs[1,0].imshow(mlem_rec, cmap="Greys_r");    axs[1,0].set_title("mlem_rec")
    axs[1,2].imshow(coreation, cmap="Greys_r");    axs[1,2].set_title("Bp of ration")

    mlem_rec = mlem_rec*coreation
    axs[1,0].imshow(mlem_rec, cmap="Greys_r");    axs[1,0].set_title("mlem recon image It=%d" % (iter+1))
    plt.show()
    plt.pause(0.5)

plt.show(block = True)