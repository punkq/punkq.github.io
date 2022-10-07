# [Live Tracking and Dense Reconstruction for Handheld Monocular Endoscopy (T-MI, Jan/19)](https://ieeexplore.ieee.org/abstract/document/8410942/?casa_token=8dLpCJlnIhwAAAAA:fenkrcEM_HvLYlplNRvWZNTYg3rHiefRQSYHE1PhCq6KNDs9FxxJ5CVLUv3ArmnfaqAmZuv4JFsvrg)

## Insight
1. A dense monocular liver tracking and reconstruction method for handheld monocular endoscopy
2. Inspired by [ORB-SLAM (SLAM based quasi dense reconstruction for minimally invasive surgery scenes)](https://arxiv.org/abs/1705.09107)
3. Trick: carefully choose keyframes, divide video into a set of clusters based on keyframes each

## Challendges for vision-based endoscopy reconstrustion
1. Illumination variability
2. Specular reflection (because of the mucosa surface)
3. Irregular textures
4. Occlusion
5. Discontinous and non-rigid (deformation)

## Method
Proposed SLAM method:
1. Sparse Tracking
  - Feature Detection
  - Map Matching
  - Pose Estimation
2. Sparse Reconstruction
  - Sparse Points Creation
  - Keyframe Extraction
  - Bundle Adjustment
3. Dense Reconstruction
  - Frame Clusters Selection
  - Inverse Depth Discretization
  - Depth Estimation and Alignment

## Experiment
 - Liver reconstruction based on laparoscopy
 - Gold-standard: CT suface

## Notes
 - Current monocular SLAM methods can be divided into sparse and dense methods. 
   - The sparse methods utilize sparse features and reconstruct relatively incomplete results. These methods often consider salient images and estimate poses by minisizing the re-projection errors.
   - The dense methods can build real-time dense results on non-medical scenes. These methods requires constant illumination and unchange pixel brightness in different views.
 - To deal with the illumination, rotation and deformation problems, which are typical problems in endoscopy, discriminative and rotation-invariant features are used in some methods.


# [Deep learning and conditional random fields-based depth estimation and topographical reconstruction from conventional endoscopy (MIA Jul/18)](https://www.sciencedirect.com/science/article/pii/S1361841518303761)

## Insight
First deep learning-based method for endoscopy Depth Estimation: CNN + conditional random field (CNN-CRF) framework for monocular endoscopy depth estimation

## Data and Methods
1. Training data are synthetic: around a half of data are rendering on a 3D colon model, the other half are from pig colon segment
2. Learn from data above and use a CNN to generate conditional random fields estimating the depth
3. Validate on the real endoscopy images, Gold-standard: CT

## Notes
1. Polyps are easily ignored due to the deformation of mucosa.
2. Chromoendoscopy can inscrease the contrast of lesion

# [Global and Local Panoramic Views for Gastroscopy: An Assisted Method of Gastroscopic Lesion Surveillance (EMB Aug/15)](https://pubmed.ncbi.nlm.nih.gov/25910000/)

## Insight


## Methods

## Data

## Experiments

## Notes




