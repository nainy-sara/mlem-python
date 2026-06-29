# MLEM - Maximum Likelihood Expectation Maximization in Python

A Python implementation of the **MLEM (Maximum Likelihood Expectation Maximization)** iterative reconstruction algorithm for computed tomography (CT) image reconstruction.

## Overview

This project implements the MLEM algorithm, an iterative statistical method commonly used in medical imaging for reconstructing images from sinogram data (projection data). The algorithm is particularly useful for improving image quality in CT imaging by iteratively refining the reconstruction based on the Radon transform and its inverse.

## What is MLEM?

The Maximum Likelihood Expectation Maximization algorithm is a popular iterative reconstruction technique that:
- Reconstructs images from sinogram (Radon) projections
- Improves image quality iteratively through statistical optimization
- Handles noise better than direct inversion methods like the Filtered Back Projection (FBP)
- Converges to a maximum likelihood estimate of the original object

## Features

- ✅ Full MLEM iterative reconstruction implementation
- ✅ Visualization of reconstruction progress at each iteration
- ✅ Real-time display of intermediate results (object, sinogram, reconstructions)
- ✅ Support for configurable number of iterations
- ✅ Interactive Jupyter Notebook implementation

## Requirements

```
numpy
matplotlib
scikit-image
IPython
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nainy-sara/mlem-python.git
cd mlem-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib scikit-image ipython
```

## Usage

The main implementation is in `mlem.ipynb`, a Jupyter notebook that demonstrates the MLEM algorithm step-by-step.

### Running the Notebook

1. Launch Jupyter:
```bash
jupyter notebook
```

2. Open `mlem.ipynb` and run all cells

3. Watch as the algorithm iteratively reconstructs the Shepp-Logan phantom image over 20 iterations

### What the Code Does

1. **Loads the Shepp-Logan Phantom**: A standard test image used in CT imaging
2. **Computes the Sinogram**: Radon transform of the object (forward projection)
3. **Initializes MLEM**: Starts with a uniform image estimate
4. **Iterative Reconstruction**: For each iteration:
   - Computes forward projection of current estimate
   - Calculates the ratio of actual sinogram to computed sinogram
   - Computes backprojection of the ratio
   - Updates the reconstruction
5. **Visualizes Results**: Displays 6 subplots showing:
   - Original object
   - Sinogram (projection data)
   - Ratio sinogram
   - Forward projection of reconstruction
   - Current MLEM reconstruction
   - Backprojection of ratio

## Algorithm Details

### MLEM Update Formula

```
$$n_{i}^{[k+1]}=\frac{n_{i}^{[k]}}{\sum_{j}w_{ij}}\sum_{j}w_{ij}\frac{P_{j}}{\sum_{i}w_{ij}n_{i}^{[k]}}$$
```

Where:
- `FP` = Forward Projection (Radon transform)
- `BP` = Backprojection (Inverse Radon transform)
- `SensitivityImage` = Backprojection of all-ones sinogram
- `m_n` = Reconstruction at iteration n

### Key Components

- **Forward Projection**: `skimage.transform.radon()`
- **Backprojection**: `skimage.transform.iradon()` with no filter
- **Sensitivity Correction**: Prevents division by zero and normalizes the update
- **Iterations**: 20 iterations (configurable)

## Output

The notebook generates real-time visualizations showing:
- Progressive improvement in image quality
- Convergence of the reconstruction algorithm
- Detailed views of intermediate calculations (sinogram ratios, forward projections)

## Parameters

You can modify these parameters in the notebook:

```python
# Number of iterations
iter_range = range(20)

# Projection angles
azi_angle = np.linspace(0.0, 180, 180, endpoint=False)

# Rescaling factor for phantom
rescale_factor = 0.5

# Small epsilon to avoid division by zero
epsilon = 0.0000001
```

## Applications

- **Medical Imaging**: CT scan reconstruction
- **Industrial Testing**: Non-destructive testing (NDT)
- **Scientific Research**: Tomographic reconstruction in various fields
- **Image Processing**: Solving ill-posed inverse problems

## References

- Shepp, L. A., & Logan, B. F. (1974). "The Fourier reconstruction of a head section". IEEE Transactions on Nuclear Science.
- Hudson, H. M., & Larkin, R. S. (1994). "Accelerated image reconstruction using ordered subsets of projection data".
- scikit-image documentation: https://scikit-image.org/

## Notes

- The algorithm converges gradually; you may see improvement plateau after several iterations
- A small epsilon (0.0000001) is added to the forward projection to avoid division by zero
- The sensitivity image acts as a normalization factor in the update step
- Each iteration involves one forward and one backward projection

## License

[Add your license here]

## Author

Zeinab Motevalli Bashi Naini

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

For questions or feedback, please open an issue in the repository.
