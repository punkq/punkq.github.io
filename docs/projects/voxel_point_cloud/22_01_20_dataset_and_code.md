# Fast Validation

## Codes

1. [mmdetection](https://github.com/open-mmlab/mmdetection): detect the 2D slices and get the bbox 
2. manually sample points on the bboxs
3. [VoteNet](https://github.com/facebookresearch/votenet): apply 3D detection on the sampled points

## Dataset

Test and Validate on a small subdata first
 - ~~[RibFrac](https://ribfrac.grand-challenge.org/)~~ Evaluation on segmentation mask 
 - [LUNA 16](https://luna16.grand-challenge.org/Home/): Target is nodule centers and their radius

## Evaluation
 - FROC: similar as ROC, but replace the false positive rate with 
 - The highest FROC score for RibFrac: [85.87](https://ribfrac.grand-challenge.org/evaluation/challenge/leaderboard/)
 - FROC can both measure the detection results and segmentation results. It depends on the annotation form. 

