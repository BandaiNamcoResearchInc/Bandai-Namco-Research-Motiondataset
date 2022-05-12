# Bandai-Namco-Research-Motiondataset-2

Find [here](README_Japanese.md) for a READEME in Japanese.

Bandai-Namco-Research-Motiondataset-2 is collected by Bandai Namco Research Inc. Compared with Bandai-Namco-Research-Motiondataset-1, this dataset contains a single, uniform expression per style, and a rich assortment of data per content.

## Dataset
The dataset contains motion in BVH format with annotations in JSON format within `data.zip`.  The annotations contain the ID of the content, and the style of the motion within the filename and corresponding labels can be found in `content_label.txt` and `style_label.txt`under the `cfg/` directory.

The data is named in correspondence to the following: `dataset-2_{MOTION}_{STYLE}_{ID}`  
For instance: `dataset-2_raise-up-both-hands_active`

### Basic Info
|Basic Info||
|--|--|
|Number of Data|2,902|
|Number of frame|384,931|
|Number of styles|7|
|Number of contents|10|
|Frame Rate|30|

### Contents
- walk
- walk-turn-left
- walk-turn-right
- run
- wave-both-hands
- wave-left-hand
- wave-right-hand
- raise-up-both-hands
- raise-up-right-hand
- raise-up-right-hand

### Styles
- active
- elderly
- exhausted
- feminine
- masculine
- normal
- youthful


## Visualization
The visualizations of the main motions are shown below. All combinations can be found in `videos.zip`.

### walk
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_walk.gif" width="100%">

### walk-turn-left
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_walk-turn-left.gif" width="100%">

### walk-turn-right
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_walk-turn-right.gif" width="100%">

### run
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_run.gif" width="100%">

### wave-both-hands
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_wave-both-hands.gif" width="100%">

### wave-left-hand
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_wave-left-hand.gif" width="100%">

### wave-right-hand
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_wave-right-hand.gif" width="100%">

### raise-up-both-hands
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_raise-up-both-hands.gif" width="100%">

### raise-up-left-hand
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_raise-up-left-hand.gif" width="100%">

### raise-up-right-hand
<img src="../../src/Bandai-Namco-Research-Motiondataset-2/movie_raise-up-right-hand.gif" width="100%">


&copy;  [2022] Bandai Namco Research Inc. All Rights Reserved
