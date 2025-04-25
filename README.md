# Functional Analysis
Official repository for functional analysis course project, offered in 3rd year by Prof. JK Sahoo

An attempt to critically analyse and present the paper: [**Shearlet-based regularization in statistical inverse learning with an application to x-ray tomography**](https://iopscience.iop.org/article/10.1088/1361-6420/ac59c2/pdf), *Tatiana A Bubba, Luca Ratti*. We also compare it to the latest State-of-The-Art deep learning methods utilised for X-ray tomography.

## Overview:
The paper advances the theoretical and practical understanding of statistical inverse learning by introducing and analyzing shearlet-based regularization, particularly for applications in x-ray tomography. The work extends previous results on convergence rates for convex, p-homogeneous regularizers {with p∈(1,2]}, moving beyond wavelet-based [Besov spaces] methods to the more general and powerful shearlet framework [Shearlet-Coorbit space], and addresses both theoretical and numerical aspects, including the challenging case p→1 (i.e., ℓ1-regularization).

### Key concepts:
1. Statistical Inverse Learning: The intersection of inverse problems [recovering an unknown f from an indirect, noisy measurements g] and statistical learning [estimating functions from sampled, noisy data].
2. Regularization: Stabilizes ill-posed problems by minimizing a functional combiing data fidelity and a regularization term R(f), often prompting sparsity in a transform domain [wavelet, shearlet].
3. Shearlets: A multiscale, directional representation system particularly suited for images with anisotropic features, outperforming wavelets in capturing such structures.

## Contributions:
1. Extension of Convergence rates to Shearlets [non-tight banach frames]
2. Extensive convergence rate analysis in the symmetric Bregman distance
3. Limiting behaviour as p→1 is addressed using Γ-convergence

An earlier work of TA Bubba on Shearlet-Deep Learning integrated methods for reconstruction can be observed in [Learning the Invisible: A hybrid deep learning-shearlet framework for limited angle computed tomography](https://iopscience.iop.org/article/10.1088/1361-6420/ab10ca/pdf)

## Methodology:
1. Uses variational regularization: Combines a data-fidelity term and a regularizer.
2. Considers both bounded noise and random sampling settings.
3. Applies l<sub>p</sub>-norm minimization [1<p<2] to wavelet and shearlet frames.
4. Leverages Γ-convergence to transition results as p→1.

This paper is an excellent example of interdisciplinary integration Math, Computer science, Information theory and Digital imaging techniques. We try to present the paper in a way that it touches every course covered in a general MSc Mathematics degree, such as:
- Abstract courses: Real analysis, Topology, Functional Analysis, Probability theory, Harmonic analysis, Measure theory
- Applicative courses: Numerical analysis, Optimization, Statistical learning, Computational imaging, Partial Differential equations

## Takeaway:
1. How abstract math supports image reconstruction
2. How practical tools [like shearlets, algos like VMILA] improve reconstructions in medical imaging
3. How regularization and statistical models help balance noise, sparsity and accuracy

We also show a live demo of sparse reconstruction in tomography at the end
