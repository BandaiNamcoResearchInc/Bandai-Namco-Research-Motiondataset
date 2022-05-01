# Bandai-Namco-Research-Motiondataset-2
Bandai-Namco-Research-Motiondataset-2は株式会社バンダイナムコ研究所によって収集されたモーションキャプチャのデータです。  Bandai-Namco-Research-Motiondataset-1と比較すると、このデータセットはコンテンツやスタイルの多様性が少ないですが、
フレーム数が多く収録されています。

## Dataset
'data.zip'にBVH形式のモーションとJSON形式の注釈が含まれています。注釈にはコンテンツのIDが含まれており、ファイル名内のモーションのスタイルと対応するラベルは、'cfg/'ディレクトリ内に'content_label.txt'および'style_label.txt'に記載があります。

次のような命名規則で名前が付けられています: `dataset-2_{MOTION}_{STYLE}_{ID}`  
例 : `dataset-2_raise-up-both-hands_active`

### Basic Info
|Basic Info||
|--|--|
|Number of Data|175|
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

代表的なモーションを可視化したものを以下に示します。`videos.zip`にすべてのモーションの動画が入っています.

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
