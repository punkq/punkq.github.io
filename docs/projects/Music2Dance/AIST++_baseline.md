<!--
 * @Author: PunkQ
 * @Date: 2022-10-07 13:02:06
 * @LastEditTime: 2022-10-07 16:59:25
 * @LastEditors: PunkQ
 * @Description: The basic introduction of AIST++ baseline
 * @FilePath: /punkq.github.io/docs/projects/Music2Dance/AIST++_baseline.md
-->

# [AIST++ (ICCV 21)](https://openaccess.thecvf.com/content/ICCV2021/papers/Li_AI_Choreographer_Music_Conditioned_3D_Dance_Generation_With_AIST_ICCV_2021_paper.pdf)


## Contribution
0. Brief [description](https://ai.googleblog.com/2021/09/music-conditioned-3d-dance-generation.html) by authors
1. Annotate the 3D joint coordinates in [AIST (ISMIR 19)](https://archives.ismir.net/ismir2019/paper/000060.pdf)
2. Build a baseline for 3D dance pose sequence annotation with music input:
 - data input: starting motion and music audio
 - output: a sequence of 22 smpl joint coordinates 
 - method: autoregressor
 - evaluation: FID, diversity and Beat Alignment Score (convert 22 joints into 35 key points through smpl)

## [Data](https://google.github.io/aistplusplus_datasetl) Outline
### refer data formats in [AIST](https://aistdancedb.ongaaccel.jp/data_formats/): 
 - eg. gBR_sBM_c01_d04_mBR0_ch07.mp4
 - **gBR -- 10 genres**: Old School (Break, Pop, Lock and Waack) and New School (Middle Hip-Hop, LA-style Hip-Hop, House, Krump, Street Jazz and Ballet Jazz)
 - g: BR, PO, LO, WA, MH, LH, HO, KR, JS & JB, respectively
 - **s -- 2 situations**: BM for basic dance, FM for advanced dance 
 - **c -- 10 cameras**: camera id 01-10, or All for multi-view fusion results 
 - **d -- 10 dancers**: only single dancers are considered
 - dancer ID: from d20 d31 d21 d32 d33 d34 d35 d22 d23 to d24 
 - **m -- music**: every genre has 6 pieces of music from 
 - m: "BR0" to "BR5" for example, 60 songs in total for about 40 sec to 60 sec 
 - tempo: 0-5 stands for 80, 90, 100, 110, 120, 130 expect HO
 - tempo for HO (house): 0-5 stands for 80, 90, 100, 110, 120, 130
 - **ch -- 10 choreos**: every genre has 10 choreographies 01-10

## Baseline
1. Method looks like
     - given a piece of music and a starting motion (2 seconds)
     - predict N future motions

2. 3D motion sequence as:
     - joint rotation 
     - global translation
