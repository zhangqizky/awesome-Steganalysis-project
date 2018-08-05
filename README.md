## 隐写分析的意义
隐写分析是通过对载体的统计特性进行分析，判断载体中是否隐藏有额外的信息甚至估计信息嵌入量、获取隐藏信息内容的技术。其研究对于防止机密信息泄露、打击恐怖主义与犯罪活动、维护互联网安全等方面都具有十分重要的意义。目前的隐写分析研究领域通常将隐写分析看成一个二分类问题，目标是区分正常载体和含密载体。虽然人类感知器官无法进行区分，研究者可以借助机器学习、模式识别等工具，并通过对图像统计特性进行分析来实现有效判别。根据应用范围的不同，隐写分析可以分为两种类型：专用隐写分析(SpecificSteganalysis)和通用隐写分析(Universal Steganalysis)。专用隐写分析利用某种隐写术中存在的特定的缺陷或漏洞进行针对性的攻击，检测准确率较高。但其局限性在于只对特定的一种或一类隐写术有效。由于目前的隐写算法千变万化，且新的算法层出不穷，针对性的隐写分析方法很难满足实际应用需求，因此不针对特定隐写算法的通用隐写分析技术受到了更多的重视，并成为了目前隐写分析领域主流的研究方向。通用隐写分析的基本思想是利用隐写算法对载体图像统计特性造成的改变中存在的共性来进行检测，可以对多种隐写术进行攻击，更接近实际应用需求。

### 著名期刊
* IEEE Transactions on Information Forensics and Security (TIFS)
* Information Hiding and Multimedia Security(IH&MMSec)
* Media Watermarking, Security, and Forensic (MWSF)
* International Workshop on Information Forensics and Security (WIFS)
* International Workshop on Digital Watermarking (IWDW)


## 基于传统特征的图像隐写分析方法
### 概述
传统的图像通用隐写分析方法一般包括特征提取和训练分类器两个步骤。其中，隐写分析中的特征是对正常图像和载密图像具有区分能力的统计量。而分类器则是机器学习中常用的 SVM、集成分类器(Ensemble Classifier)等可训练优化的类别判别工具。两个步骤中，特征表达是研究中的关键问题，其对检测性能起到决定性的作用。在传统的方法中，特征表达主要依赖于人工设计，且特征设计的基本思想是找到隐写操作前后图像中具有明显差异的统计量
### 传统特征方法整理
#### 早期低纬图像特征
- [Harmsen和Pearlman提出的基于直方图特征函数质心(histogram characteristic function center of mass, HCFCOM)特征](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/5020/1/Steganalysis-of-additive-noise-modelable-information-hiding/10.1117/12.476813.full?SSO=1)
- [Ker 等[3]引入校准技术后提出的邻接直方图特征函数质心 (adjacency histogram characteristic function center of mass, AHCFCOM)特征](https://doi.org/10.1109/LSP.2005.847889)
- [Shi 等[5]提出的基于图像小波系数直方图各阶统计矩的 CF 特征](https://doi.org/10.1109/itcc.2005.138)
- [Goljan 等[6] 提出的基于小波绝对矩(wavelet absolute moment, WAM)特征](http://www.ws.binghamton.edu/fridrich/research/EI06-6072-1.pdf)
#### 近年来图像隐写术的发展也是层出不穷，从LSB(最低有效位)到LSB-Match，再到HUGO, SUNIWARD, WOW, HILL-CMD, MiPOD等内容自适应隐写术可以自动的将隐秘信嵌入到纹理、噪声丰富的图像区域，从而保持复杂的图像高阶统计特性。隐写术的快速进步使得早期提 出的基于简单统计量的特征很难取得有效的检测效果。
#### 针对复杂的隐写术提出的基于高维图像特征的隐写分析
 为了对抗更先进的自适应隐写术，隐写分析领域特征设计过程中需要考虑更复杂的图像统计特性， 并且特征也逐渐朝着复杂化、高维化发展。目前，基于对图像邻域复杂相关性进行建模的高阶统计量特 征称为隐写分析领域的主流特征。该类特征提取方法包括如下两步:第一步是预处理，即对相邻的像素 或者DCT系数用不同种类高通滤波核进行滤波操作得到不同的残差图像;第二步分别从各个残差图像中 计算描述邻近像素或系数间相关性的共生矩阵、投影直方图、LBP (Local Binary Pattern)等作为特征，进而通过组合不同残差图像上得到的特征得到最终的高维特征集.
 该类特征可统称为“富模型” 特征，其中“富”字体现在其通过组合相异的子特征集使得特征可以表达丰富的统计特性。同时该类特 征这些特征在维度上相比于早期的特征有了大幅度的提升,例如下面两种模型，所提取的图像特征均超过了10000维。
- [SRM (Spatial Rich Model)](http://www.ws.binghamton.edu/fridrich/Research/TIFS2012-SRM.pdf)
- [PSRM (Projection Spection Rich Model)](https://doi.org/10.1109/TIFS.2013.2286682)
#### 针对富模型的改进
- [Tang首先提出了利用选择信道信息的自适应隐写分析(Adaptive Steganalysis)，且主要针对的是 WOW 隐写算法](https://doi.org/10.1145/2600918.2600935)
主要针对的是 WOW 隐写算法。其思想是首先从图像中筛选出可疑区域，然后只从可疑区域中提特征。筛选可疑区域 的方式是首先用 WOW 算法中的方法计算每个像素的嵌入代价(embedding cost) ρij，ρij 越小表示该像素被 修改的概率越大。通过一定的比例 p 选出 ρij 较小的像素集作为可疑区域，其中 p 为可调参数。最终在筛 选出的可疑区域上计算残差并提取共生矩阵作为特征。该方法对 WOW 的检测相对传统特征提取方式有 了一定的提升。
- [Denemark 等[21]在 Tang 等工作的基础上提出了一种新的通用的自适应隐写分析特征](https://doi.org/10.1109/wifs.2014.7084302)
该方法所提的 特征可看成是传统 Rich Model 的变体。提特征所用到的残差、量化截短等操作均与传统 Rich Model 中的 相同。不同点在于共生矩阵的计算。传统 Rich Model 在从残差上计算四维共生矩阵时，同等的看待每个 四元组(d1, d2, d3, d4)的贡献，即每次四元组出现时对应的共生矩阵中的 bin 值加 1，其中 d1, d2, d3, d4 为残 差图像中的元素。而该文的作者认为应当对图像中每个元素对最终特征的贡献有所区分，修改概率大的 位置应赋予更大的权重。该方法中，每次四元组出现时，对应的共生矩阵中的 bin 值加四元组元素对应 的修改概率 βij 的最大值，其中 βij 是根据相应隐写术中的计算方式得到。该方法相比 HUGO、WOW、 SUNIWARD 等自适应隐写术的检测效果较传统方法都有所提升。
## 基于深度学习的图像隐写分析方法
### 概述
虽然基于人工设计特征的通用隐写分析技术近些年取得发展较快，但仍面临诸多困难及挑战。首先，人工设计特征是一种非常费力、启发式的方法，有效特征的设计选取更多的依赖于人的经验，且需要花费大量的时间精力。其次，作为互相对抗的两种技术，在隐写分析发展的同时，隐写术也在不断地进步。新型的隐写术层出不穷，且新提出的隐写术往往可以保持图像中更复杂的统计特性，这也给隐写分析提出了越来越高的要求。为了进行有效的检测，隐写分析特征也需要考虑更复杂的统计特性，特征设计难度不断加大。

### 深度学习的方法整理
- [2015年的Deep learning for steganalysis via convolutional neural networks](http://xueshu.baidu.com/s?wd=paperuri%3A%281c85f9edc52b10af1f6157d44667da57%29&filter=sc_long_sign&tn=SE_xueshusource_2kduw22v&sc_vurl=http%3A%2F%2Fadsabs.harvard.edu%2Fcgi-bin%2Fnph-data_query%3Fbibcode%3D2015SPIE.9409E..0JQ%26amp%3Bdb_key%3DPHY%26amp%3Blink_type%3DABSTRACT%26amp%3Bhigh%3D567107244204418&ie=utf-8&sc_us=10775830153732577606)。
- [Pibre等提出了一 种新的基于适应于隐写分析的 CNN 的网络结构模型Deep Learning is a Good Steganalysis Tool when Embed- ding Key is Reused for Different Images, even if there is a Cover Source-Mismatch](http://www.lirmm.fr/~chaumont/publications/IST_ELECTRONIC_IMAGING_Media_Watermarking_Security_Forensics_2016_PIBRE_PASQUET_IENCO_CHAUMONT_Deep_Learning_Artificial_Experimental_Protocol_Slides.pdf)
- [Structural Design of Convolutional Neural Networks for Steganalysis](https://doi.org/10.1109/LSP.2016.2548421)
- 迁移学习，针对低嵌入率图像
[Learning and Transferring Representations for Image Steganalysis Using Convolutional Neural Network](https://doi.org/10.1109/ICIP.2016.7532860)
- 正则化，利用传统特征
[Learning Representations for Steganalysis from Regularized CNN Model with Auxiliary Tasks.](http://ir.ia.ac.cn/handle/173211/12307)
- 不同模型融合
[Ensemble of CNNs for Steganalysis: an Empirical Stud](https://doi.org/10.1145/2909827.2930798)


### 目前研究重点和展望
近年来隐写分析得到了快速的发展，并不断有新的成果涌现。本文着重讨论了近几年图像通用隐写分析领域发展情况，包括传统基于人工特征的方法的新进展以及基于深度学习在隐写分析方法新思路。今后隐写分析的进一步发展可以从以下几个方面考虑：
1) 特征表达仍将是隐写分析中的研究重点。基于深度学习的方法的提出开辟了隐写分领域的新范式，也将是接下来的研究重心所在。但目前基于深度学习的隐写分析研究仍是在初步阶段，仍有很多问题需要进一步的考虑与解决。首先，目前的基于深度学习的隐写分析框架中仍需要人工设计的高通滤波核进行图像预处理，未来是否能不需要依赖人工预处理，实现端到端学习是一个值得继续研究的问题；其次，目前基于深度学习的隐写分析模型的检测性能仍没有完全超过目前最好的基于人工设计特征的方
法，有待进一步提高；最后，目前提出的针对隐写分析的深度学习模型相对较简单，未来能否结合迁移学习，增强学习，对抗生成网络等深度学习领域内的研究热点提出更适合隐写分析的模型也值得关注。
2) 目前的通用隐写分析技术仍需要用到隐写算法、嵌入量等先验信息，例如在构建分类器时仍需要与待检测隐写术对应的载密图像进行训练，并不能真正做到“盲”检测。考虑到新的隐写算法层出不穷，因此研究独立于隐写术的通用隐写分析十分重要。
3) 面向实际应用的隐写分析，特别是社交网络平台大数据环境下的隐写分析研究是一个很值得关注的问题。目前的隐写分析研究大多局限在特定的小规模数据库等实验室条件下。而实际应用环境下隐写分析面临的则是社交网络背景下大数据、异质图像源等复杂的图像数据，实验室条件下取得成功的方法往往很难成功的进行实际应用。目前面向实际应用的隐写分析研究较少，但需求迫切，尚待进一步的研究。
4) 目前的隐写分析研究目标主要停留在检测隐写存在性这一层次上，而更高层次的定位隐写嵌入位置、提取出隐写信息等目标目前仍没有有效的方法，其也是今后隐写分析需要努力的方向。
### 一些开源项目和工具
1. [一个Steganaysis的python工具包](https://github.com/cedricbonhomme/Stegano)
2. [A steganalysis tool for detecting LSB steganography in images ](https://github.com/b3dk7/StegExpose)
3. [Least Significant Bit Steganography for bitmap images (.bmp and .png), WAV sound files, and byte sequences. Simple LSB Steganalysis (LSB extraction) for bitmap images.](https://github.com/ragibson/Steganography)
4. [Image steganalysis using state-of-the-art machine learning techniques](https://github.com/daniellerch/aletheia)
5. [caffe_deep_learning_for_steganalysis](https://github.com/GuanshuoXu/caffe_deep_learning_for_steganalysis)
6. [code of our paper entitled: Improving Blind Steganalysis in Spatial Domain using a Criterion to Choose the AppropriateSteganalyzer between CNN and SRM+EC ](https://github.com/rcouturier/steganalysis_with_CNN_and_SRM)
7. [Audio and image steganalysis with tensorflow1.3 or later](https://github.com/Charleswyt/tf_audio_steganalysis)
8. [Tensorflow implementation of "Deep Learning Hierarchical Representation for Image Steganalysis" ](https://github.com/Caenorst/YeNet-Tensorflow)
9. [Machine learning steganographic image detection. ](https://github.com/rokkuran/stegasawus)
10. [steganalysis_with_CNN_for_same_key_images](https://github.com/rcouturier/steganalysis_with_CNN_for_same_key_images)
11. [some code for deep steganalysis](https://github.com/jiangszzzzz/CAECNNcode)
12. [Steganalysis of JPEG images with CUDA optimizations ](https://github.com/id23cat/cujpgstego)
