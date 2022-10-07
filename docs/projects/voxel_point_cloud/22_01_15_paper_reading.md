# [RibSeg Dataset and Strong Point Cloud Baselines for Rib Segmentation from CT Scans](https://arxiv.org/abs/2109.09521)

## Insight
Complicated 3D structures in medical images can be represented as point clouds to learn and be predicted.

## Dataset
1. Ribfrac
2. RibSeg (proposed)

## Method
1. They Manually label the point cloud of Ribfrac and name it as RibSeg
2. Build a pointnet++ to predict the points labels
3. Post-process to reconstruct the voxel predictions

## Experiment
Compare their method with pointnet++ and its deviants


# [PC-U net: Learning to jointly reconstruct and segment the cardiac walls in 3D from CT data](https://arxiv.org/pdf/2008.08194)

## Insight
Using a point cloud as an intermediate representation for voxel semantic segmentation is feasible.

## Dataset
3D cardiac CT

## Method
They plug a PointNet in a 3D mask segmentation network.

## Experiment
Compare their method with PointOutNet and PointNet deviants.

# [Rethinking Pulmonary Nodule Detection in Multi-view 3D CT Point Cloud Representation](https://link.springer.com/chapter/10.1007/978-3-030-87589-3_9)

## Insight
Using point cloud as an intermediate representation for 3D voxel detection is ok, but not as good as existing methods.

## Dataset
LUNA16

## Method
1. They learn to convert 3D voxel into point cloud 
2. Rotate point clouds to achieve data augmentation
2. Apply a point cloud detection network on rotated data
3. Fuse the detection results

## Experiment
They compare their method with different methods on LUNA16, and their method is not competitive as other methods.
