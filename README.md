# BUPT-Course-of-VTON
  基于AI的虚拟换装技术研究
  --------------------
  by：刘丽欣&何晶&洪翱
  
  指导老师：张宪林
  
  数媒2021
  
## [**A Curated List of Awesome Virtual Try-on (VTON) Research!**](https://github.com/minar09/awesome-virtual-try-on)

## DataSets：
1、[**VITON-HD**](https://github.com/shadow2496/VITON-HD)

白色背景模特图的单件单品试衣（上衣）

已实现复现任务

包含：
agnostic-mask、agnostic-v3.2、cloth_mask、gt_cloth_warped_mask、image-densepose、image-parse-agnostic-v3.2、image-parse-v3、openpose_img、openpose_json

2、[**DressCode**](https://github.com/aimagelab/dress-code)

和VITON-HD一样是白色背景模特图的单件单品试衣的benchmark。但是Dress Code同时包括了上衣，下装和裙子三个品类，可以更加完善的验证虚拟试衣算法的有效性。

## Papers:

1、Multimodal Garment Designer: Human-Centric Latent Diffusion Models for Fashion Image Editing

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2304.02051.pdf)
[![GitHub Stars](https://img.shields.io/github/stars/aimagelab/multimodal-garment-designer?style=social)](https://github.com/aimagelab/multimodal-garment-designer)

- 无'''train code'''
- sketch & prompt & image & keypoints

  

2、StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2312.01725.pdf)
[![GitHub Stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=social)](https://github.com/rlawjdghek/StableVITON?tab=readme-ov-file)

- 含'''train code'''
- sketch & prompt & image & keypoints
  


3、Person Image Synthesis via Denoising Diffusion Model

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2211.12500.pdf)
[![GitHub Stars](https://img.shields.io/github/stars/ankanbhunia/PIDM?style=social)](https://github.com/ankanbhunia/PIDM)

- 含'''train code'''
  


4、OOTDiffusion

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2403.01779.pdf)
[![GitHub Stars](https://img.shields.io/github/stars/levihsu/OOTDiffusion?style=social)](https://github.com/levihsu/OOTDiffusion)

- 无'''train code'''
- 测试结果如下：
！[PIDM](https://imgur.com/Id7jTLa)

## Models：
1、虚拟试衣：

StableVITON: Learning Semantic Correspondence with Latent Diffusion Model for Virtual Try-On

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/pdf/2312.01725.pdf)
[![GitHub Stars](https://img.shields.io/github/stars/rlawjdghek/StableVITON?style=social)](https://github.com/rlawjdghek/StableVITON?tab=readme-ov-file)

2、生成新中式服装：

Lora/GAN

To be continued

## TODO
- [x] 确定模型
- [x] 爬数据
- [x] Viton-HD数据预处理复现
- [ ] 训练生成模型
- [ ] 训练换衣模型
      
