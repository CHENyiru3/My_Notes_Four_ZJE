# ZJE Collection

大家好，欢迎来本存储库。这个网站是仓库内容的在线前端，方便在线查阅课程笔记，并通过资源中心下载 GitHub 镜像或浏览 OneDrive 共享文件夹。

我是 ZJE 22 级的 yr 同学，希望仓库能帮到你。如果你也想为本仓库的持续发展做出贡献，欢迎随时 pull request，或者和我联系帮忙整理！只要有时间都会两日内进行处理。

## Quick Links

- [Resource Center](resources/index.md) - 查看 GitHub 镜像与 OneDrive 文件夹入口
- [Code Cheatsheet](Code_Cheatsheet/index.md) - R、Python、Java、SQL 查询表
- [Contribution Guide](CONTRIBUTING.md) - 投稿格式、资源路线和注意事项

## 下一步的想法

听说学院的代码课很多允许考试时候使用 online AI 甚至 agent 了。虽然我本人对此可操作性和公平性表示一定怀疑，但是从应试的角度来说，资料的收集和 Skill 蒸馏似乎是一个有效的方法。关于 skill，请查看 [Claude Code 的官方网站说明](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)。

简而言之，将考试需要的代码模块和流程提前 distill to skill bundle，考试的时候直接加载安装，基本完成了考试的一半。目前已经完成了一个版本的 skill set for ADS2，因为很久没考试了所以仅供参考：[ADS2](ADS2/index.md)。

## Courses by Year

### Year 1

| Course | Description |
|--------|-------------|
| [CHEM1](CHEM1/index.md) | Chemistry; compulsory course |
| [IBI1](IBI1/index.md) | Introduction to Bioinformatics; elective course |
| [IBMS1](IBMS1/index.md) | Integrated Biomedical Sciences 1; compulsory course |
| [ICMB1](ICMB1/index.md) | Introduction to Cell & Molecular Biology; compulsory course |
| [MATH1](MATH1/index.md) | Mathematics; compulsory course |

### Year 2

| Course | Description |
|--------|-------------|
| [ADS2](ADS2/index.md) | Applied Data Science, about R; elective course for BMI |
| [BG2](BG2/index.md) | Genetics; compulsory course |
| [BaO2](BaO2/index.md) | Biology of Organs; elective course for BMS |
| [DST2](DST2/index.md) | Java; elective course for BMI |
| [GP2](GP2/index.md) | Genomics & Proteomics; elective course for BMI |
| [IFBS2](IFBS2/index.md) | Compulsory course |
| [MI2](MI2/index.md) | Microbiology; elective course for BMS |

### Year 3

| Course | Description |
|--------|-------------|
| [BMI3](BMI3/index.md) | Biomedical Informatics; elective course for BMI |
| [CMML3 (previously CBSB3)](CBSB3/index.md) | Computational modeling; elective course for BMI |
| [IBMS3](IBMS3/index.md) | Compulsory course |
| [IN3](IN3_full/index.md) | Immunology; elective course for both BMI and BMS |
| [MBE3](MBE3/index.md) | Molecular Biology and Epigenetics; elective course for both BMI and BMS |
| [PoN3](PoN3/index.md) | Principles of Neuroscience; elective course for both BMI and BMS |

### Year 4

| Course | Description |
|--------|-------------|
| [BIA4](BIA4/index.md) | Biomedical Imaging; elective course for both BMI and BMS |
| [IBMS4](IBMS4/index.md) | Biomedical Sciences; elective course for both BMI and BMS |
| [IID_4](IID_4/index.md) | More immunology; elective course for both BMI and BMS |

## 贡献指南

2026-5-21 进行了网站重构，发生了较大变动：网站仅仅作为资源的前端；资源等实际内容被分别存档到 GitHub repo，存放小的文件（pdf、md），以及一个统一管理的 OneDrive Cloud Folder，存放所有的资源文件。

1. **Markdown 或 PDF**：欢迎直接添加文件到 [awesome_ZJE_resource](https://github.com/CHENyiru3/awesome_ZJE_resource)。这个仓库是专门存放资源的，理论上可以在线添加（虽然更推荐 clone 后拖进来然后正常 pull request），此时系统会自动添加你到 contributor；或者，觉得比较麻烦的话可以联系网站维护者，然后发送过来后，网站维护者会进行手动上传和更新。这类上传就是 GitHub 镜像，网站就可以直接下载了！
2. **DOCX/PPTX/XLSX/ZIP/ONENOTE 等资源文件入口转到 OneDrive**：不是说不接受这类格式，只是通常这类格式第一可能很大，第二可能有些专有格式。允许公开分享后，网站会通过 manifest 展示可用下载路线：适合 GitHub 镜像的资源会显示 GitHub 链接，同时保留 OneDrive 文件夹入口；大型或混合格式（onenote 或者思维导图等软件资源）优先通过 OneDrive 浏览。
3. **课上的作业和期末考试内容**：很遗憾，这个其实是一个学校不太允许的事，为了网站持续运行，暂时不支持公开，也请不要因此原因联系网站管理者。推荐联系比较熟悉了的学长学姐。本网站主要欢迎大家分享期末总结的笔记，或者课程中学习总结的笔记。
4. **零碎课堂记录**：可能网站收录优先度不是很高，因为信息不集中的话比较难以用于整理和快速复习。当然，也可以存档到 OneDrive 中，如果有同学有需要，细致的笔记也是很有帮助的。
5. **不知道怎么贡献**：欢迎联系我，有任何不明白的地方或者你想分享课程之外的知识笔记！比如说，Coding 考试的一些窍门之类的，也很欢迎分享投稿。
6. **课程笔记重复了**：这是肯定会发生的。但是我相信没有任何人的笔记是完美的，不管谁提供笔记，总能带来新的视角！网站已经在尽力建设分类体系，也非常希望能补全网站的空白。

See [Contributing](CONTRIBUTING.md) for a more operational checklist.

## 目前内容

- Code Cheatsheet（包含 R、Python、Java、SQL 的查询表）
- 大一：MATH1，CHEM1，IBMS1，IBI1，ICMB1
- 大二：ADS2，IFBS2，BG2，GP2，MI2，BaO2，DST2
- 大三：MBE3，PoN3，IBMS3，IN3，BMI3，CMML3
- 大四：IID4，IBMS4，BIA4

...持续进化中

## Contributors

- **Yicheng_22**: IBMS3
- **Tianze_22**: File recovery
- **Xiaoran_22**: Multiple courses
- **Yue_22**: Multiple courses
- **Boxiang_21**: Multiple courses

非常高兴越来越多的同学参与到了本仓库的构建和笔记的提供！感谢大家！

本仓库内容已经使用严格非商用许可的 LICENSE 保护，未经允许请勿修改少许后，用作生财之道。

**招募资源站继任学弟学妹！本人马上就毕业了，可能之后时间就没有那么多投入了，更新也会不那么及时**
