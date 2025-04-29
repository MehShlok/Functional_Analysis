import numpy as np
import matplotlib.pyplot as plt
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, iradon
from sklearn.linear_model import Lasso

# Generate phantom
image = shepp_logan_phantom()[:512, :512]
n_angles = 100 # Number of projection angles

# Simulate random angle sampling
theta = np.linspace(0., 180., n_angles, endpoint=False)
np.random.shuffle(theta)

# Create sinogram
sinogram = radon(image, theta=theta, circle=True)

# Add noise
noise_level = 0.05
sinogram_noisy = sinogram + noise_level * np.random.randn(*sinogram.shape)

# --------------------------
# Shearlet-based reconstruction
# (Simplified using wavelet transform as example)
# For actual shearlets, use ShearLab/pyshearlab
# --------------------------
from skimage.restoration import denoise_wavelet

# Reconstruction using wavelet-regularized least squares
def shearlet_reconstruction(sinogram, theta, alpha=0.1):
    reconstruction = iradon(sinogram, theta=theta)

    # Iterative reconstruction with thresholding
    for _ in range(10):
        # Wavelet denoising (replace with shearlet transform)
        reconstruction = denoise_wavelet(
            reconstruction,
            method='BayesShrink',
            mode='soft',
            wavelet_levels=3,
            rescale_sigma=True
        )

        # Data consistency step
        residual = radon(reconstruction, theta) - sinogram
        reconstruction -= 0.1 * iradon(residual, theta)

        # Non-negativity constraint
        reconstruction[reconstruction < 0] = 0

    return reconstruction

# Perform reconstruction
recon = shearlet_reconstruction(sinogram_noisy, theta)

# Plot results
fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original Phantom')
ax[1].imshow(sinogram_noisy, cmap='gray')
ax[1].set_title('Noisy Sinogram')
ax[2].imshow(recon, cmap='gray')
ax[2].set_title('Reconstruction')
plt.show()
