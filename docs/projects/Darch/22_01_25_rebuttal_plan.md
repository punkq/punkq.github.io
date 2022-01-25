# Darch Rebuttal Plan

## [Review.pdf](files/review.pdf)

## 补充实验

1. 需要补充和其他更多方法的比较
 - reviewer1 weakness1.1(comparative experiment lacks extensiveness)
 - reviewer2 weakness5, justification(needs naive segmentation methods to be compared with)
2. 补充ablation study第一阶段对第二阶段的影响，为什么tseg检测结果很接近，但是分割结果却差很差
 - reviewer1: weakness ablation(how much the error in the first stage will affect the second stage)
 - reviewer2 weakness4(not difference between 99.68 and 99.41)
其他小的实验：
3. ablation study牙弓线学习具体参数设置
 - reviewer1 weakness ablation(the analysis of hparams are lacking)
4. 去掉特定牙齿的时候，牙齿模型的分割情况 
 - reviewer2 justification
5. 不同距离阈值参数的情况下，牙齿检测的指标情况 
 - reviewer2-weakness4 99.68 vs 99.41

## Reviewer 1
1. Question: Summary - This is a highly specific work, and the proposed method lacks influence in the field.
 - Answer：这确实是一个针对性的任务，但是牙科模型的自动分割是intral-oral检查之后的最基本task,是非常重要的任务
2. Question: weakness1.1- not compare with the work in "related work"
 - Answer：确实存在一些现有的方法我们没有比较. 我们在做实验的时候发现 A.大部分牙齿分割的方法针对的是存在牙齿class标注的数据集,并不是我们这种情况,如123; B.目前最新的点云实例方法不适用于牙齿分割,如pointgroup,牙齿作为object在空间中的排列是密集且难以区分的
3. Question: Weakness1.2-The analysis of hparams are lacking. 
 - Answer：我们有详细的APS的ablation study,详情请参考附件, (再补充一下实验)
4. Question: Weakness1.3-Neither the data nor the code is public.
 - Answer：虽然目前现存的牙科模型的数据没有公开的版本, 但是我们的代码已经准备好了,将在camera ready的版本公开, 如果被录用的话
4. Weakness2- The author's mesleading of some concepts.
 - Answer：我们在写作上确实存在公式4的typo,正确的表示应当是.. ,我们并没有误导centroids和bbox的概念, 实际过程仅仅计算了中心点的loss

## Reviewer 2
1. Question: weakness 1(novelty) 
 - Answer：我们认可采样策略是我们的贡献之一，但是我们的novelty是减少标注精力的pipeline 和 学习并利用牙弓线. 可以认为combined several sota是我们的baseline,但是A.实验证明了baseline的效果并不理想. B.加上了我们的novel的方法之后, baseline有显著的提升
2. Question: weakness2+3 
 - Answer：A.我们进行的实验设定遵循了工作123..的设置，B.我们使用的数据集的大小是4773个模型，相比现有的其他牙齿分割方法，我们的收集了足够多的数据，是使用了最多牙齿模型的数据集。
3. Question: weakness4 
 - Answer：99.68和99.41的区分小的原因是 距离阈值的设定在这两组数据下宽松，我们现在给出其他阈值设定下的结果：...
4. Question: weakness5
 - Answer: refer to Reviewer1 Answer1
5. Question: weakness6
 - Answer：是的,随机均匀的选取可见的mask,每个epoch内这些不同的tooth是都存在的. 我们没有具体对去掉特定类别的mask来观察结果,我们可以补充这部分的实验:...
6. Question: Justification-data setup is not clear
 - Answer： 我们的数据集拥有4773组牙齿模型，分别来自3000个病人的intra-oral扫描图像，包含了龋齿，牙齿缺失，牙齿错位等多种情况，采样的设备标准有超过6种，数据量大且丰富，能覆盖牙科医生检查病人的各种intra-oral models的情况，我们实验时选取了800个模型作为validation，3973个模型作为训练集。

## Reviewer 3

1. Question: weakness1-typo
 - Answer：Refer to reviewer1-Answer5
2. Question: weakness2-description of dental arch prediction
 - Answer： 需要重新组织语言阐述一下这个牙弓预测部分
3. Question: weakness3
 - Answer: (a).这两个模块是不同的. distance-aware detection是基于最邻近牙齿中心的距离预测offset，而APS是利用牙列信息在接近的牙弓的位置采样点，采样的点是通过试验证明是容易区分的.定性(supplementary A.1)和定量(supplementary A.4)结果都证明APS采样是可以得到更好的检测结果的 (b)在弱标注情况下, 提供的牙齿的信息有限的,tsegnet拥有一个较大的分割网络,需要更足量的数据来保持泛化性能, 而我们的方法分割网络轻量且有效